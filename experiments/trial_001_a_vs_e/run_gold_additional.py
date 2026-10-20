"""Run local, author-only gold SQL for Q06–Q25; never calls an LLM."""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

import snowflake.connector
import yaml


HERE = Path(__file__).resolve().parent
SQL_FILE = HERE / 'gold_q06_q25.local.sql'
OUTPUT = HERE / 'answers_q06_q25.local.json'


def main() -> None:
    statements = {}
    for match in re.finditer(r'^-- (Q\d{2})\n(.*?)(?=^-- Q\d{2}\n|\Z)',
                             SQL_FILE.read_text(), re.MULTILINE | re.DOTALL):
        statements[match.group(1)] = match.group(2).strip()
    questions = json.loads((HERE / 'questions_q06_q25.json').read_text())
    ids = {q['id'] for q in questions}
    if set(statements) != ids or len(ids) != 20:
        raise ValueError('Question and SQL IDs do not match exactly')

    profile = yaml.safe_load(Path.home().joinpath('.dbt/profiles.yml').read_text())[
        'dbt_zomato']['outputs']['dev']
    for attempt in range(2):
        try:
            connection = snowflake.connector.connect(
                account=profile['account'], user=profile['user'], password=profile['password'],
                role='DBT_LAYER_REFACTOR_ROLE', warehouse='ZOMATO_WH',
                database='ZOMATO_DLR', schema='CORE', login_timeout=30,
                session_parameters={'STATEMENT_TIMEOUT_IN_SECONDS': 180},
            )
            break
        except snowflake.connector.errors.NonRetryableTlsError:
            if attempt:
                raise
            time.sleep(1)

    results = {'database': 'ZOMATO_DLR', 'questions': questions, 'results': {}}
    for question in questions:
        qid = question['id']
        started = time.monotonic()
        try:
            with connection.cursor() as cursor:
                cursor.execute(statements[qid])
                rows = cursor.fetchmany(101)
                if len(rows) > 100:
                    raise ValueError('Gold result exceeds 100 rows')
                results['results'][qid] = {
                    'columns': [column[0] for column in cursor.description],
                    'rows': [[str(value) if value is not None else None for value in row]
                             for row in rows],
                    'query_id': cursor.sfqid,
                }
        except Exception as exc:
            results['results'][qid] = {'error': str(exc)[-500:]}
        results['results'][qid]['seconds'] = round(time.monotonic() - started, 2)
        OUTPUT.write_text(json.dumps(results, indent=2) + '\n')
        print(qid, 'rows', len(results['results'][qid].get('rows', [])),
              'error', results['results'][qid].get('error'), flush=True)
    connection.close()


if __name__ == '__main__':
    main()
