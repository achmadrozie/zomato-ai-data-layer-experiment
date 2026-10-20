"""Generate A/E query plans from public repository metadata only.

This process never opens Snowflake credentials or sends warehouse results to
the model. The model is instructed to use no tools; tool events fail the run.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLI = Path(os.environ.get('CODEX_CLI_PATH') or shutil.which('codex') or '')
MODEL = 'gpt-6.1-sol'
ISOLATED = Path('/tmp/zomato-dlr-agent-empty')
QUESTIONS = json.loads((HERE / 'questions.json').read_text())
METRICS = sorted(p.stem for p in (ROOT / 'dbt_zomato/models/metrics').rglob('*.yml'))

PLAN_SCHEMA = {
    'type': 'object',
    'properties': {
        'kind': {'type': 'string', 'enum': ['sql', 'metricflow', 'clarify']},
        'query': {'type': 'string'},
        'metric': {'type': 'string'},
        'group_by': {'type': 'string'},
        'reason': {'type': 'string'},
    },
    'required': ['kind', 'query', 'metric', 'group_by', 'reason'],
    'additionalProperties': False,
}

# Columns below are copied from committed dbt SQL/YAML, not queried from Snowflake.
A_SCHEMA = '''Available SQL objects: all seven SOURCES tables and all seven STAGING views.
Relevant table columns:
ZOMATO_DLR.SOURCES.ORDERS (ORDER_ID TEXT, ORDER_DATE TEXT, ORDER_STATUS TEXT,
  SALES_AMOUNT TEXT, CURRENCY TEXT, CUSTOMER_RATING TEXT, DELIVERY_TIME_MIN TEXT)
ZOMATO_DLR.SOURCES.ORDER_ITEMS (ORDER_ITEM_ID TEXT, ORDER_ID TEXT, QUANTITY TEXT, LINE_AMOUNT TEXT)
ZOMATO_DLR.STAGING.STG_ZOMATO__ORDER (ORDER_ID NUMBER, ORDER_DATE DATE, ORDER_STATUS TEXT,
  SALES_AMOUNT NUMBER, CURRENCY TEXT, IS_DELIVERED BOOLEAN, IS_CANCELLED BOOLEAN)
ZOMATO_DLR.STAGING.STG_ZOMATO__ORDER_ITEM (ORDER_ITEM_ID NUMBER, ORDER_ID NUMBER, QUANTITY NUMBER,
  LINE_AMOUNT NUMBER)
STAGING order is one row per ORDER_ID; STAGING order item is one row per ORDER_ITEM_ID.
'''
E_EXTRA = '''Additional SQL objects: all INTERMEDIATE views, CORE facts/dimensions, and MARTS tables.
Relevant additional table columns:
ZOMATO_DLR.CORE.FACT_ORDER (ORDER_ID, ORDER_DATE DATE, ORDER_STATUS, SALES_AMOUNT,
  DELIVERED_SALES_AMOUNT, CURRENCY, IS_DELIVERED, IS_CANCELLED, ITEM_QUANTITY)
ZOMATO_DLR.CORE.FACT_ORDER_ITEM (ORDER_ITEM_ID, ORDER_ID, ORDER_DATE DATE, QUANTITY, LINE_AMOUNT)
ZOMATO_DLR.MARTS.MART_ORDER_CITY_CURRENCY_DAY_UTC (ORDER_DATE_UTC DATE, CITY, CURRENCY,
  ORDER_COUNT, DELIVERED_ORDER_COUNT, CANCELLED_ORDER_COUNT, DELIVERED_SALES_AMOUNT)
CORE FACT_ORDER is one row per order; FACT_ORDER_ITEM is one row per item line.
MetricFlow query is available for these governed metrics: {metrics}.
MetricFlow uses CORE models and accepts metric name with a 2025 date window.
For an INR-scoped monetary metric, group by order_id__currency and select its INR row.
'''


def model_call(prompt: str, tag: str) -> tuple[dict, dict]:
    ISOLATED.mkdir(exist_ok=True)
    schema_path = ISOLATED / 'plan_schema.json'
    answer_path = ISOLATED / f'{tag}_answer.json'
    schema_path.write_text(json.dumps(PLAN_SCHEMA))
    answer_path.unlink(missing_ok=True)
    cmd = [str(CLI), 'exec', '--ephemeral', '--ignore-user-config', '--skip-git-repo-check',
           '-C', str(ISOLATED), '-s', 'read-only', '-m', MODEL,
           '-c', 'model_reasoning_effort="low"', '--output-schema', str(schema_path),
           '-o', str(answer_path), '--json', '-']
    started = time.monotonic()
    run = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=120)
    events = []
    for line in run.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    if run.returncode or not answer_path.exists():
        raise RuntimeError(f'Model call {tag} failed: {run.stderr[-350:]}')
    tool_items = [e.get('item', {}).get('type') for e in events
                  if e.get('item', {}).get('type') not in (None, 'agent_message', 'reasoning')]
    if tool_items:
        raise RuntimeError(f'Model call {tag} used tools unexpectedly: {tool_items}')
    usage = next((e.get('usage', {}) for e in events if e.get('type') == 'turn.completed'), {})
    return json.loads(answer_path.read_text()), {
        'seconds': round(time.monotonic() - started, 2), 'usage': usage, 'tool_items': tool_items,
    }


def main() -> None:
    if not CLI.is_file():
        raise FileNotFoundError('Set CODEX_CLI_PATH to the authenticated Codex CLI')
    parser = argparse.ArgumentParser()
    parser.add_argument('--arm', choices=['A', 'E'])
    args = parser.parse_args()
    prior = HERE / 'plans.json'
    output = json.loads(prior.read_text()) if args.arm and prior.exists() else {
        'model': MODEL, 'reasoning_effort': 'low', 'repo_revision': '228c226',
        'questions': QUESTIONS, 'runs': []}
    if args.arm:
        output['runs'] = [x for x in output['runs'] if x['arm'] != args.arm]
    for arm in ((args.arm,) if args.arm else ('A', 'E')):
        exposure = A_SCHEMA + (E_EXTRA.format(metrics=', '.join(METRICS)) if arm == 'E' else '')
        for item in QUESTIONS:
            prompt = (f'You are a data analyst in arm {arm}. Use only the access described below. '
                      'Do not call shell, file, web, or any other tools. Return one JSON action. '
                      'Use kind=sql with a single read-only Snowflake SELECT, kind=metricflow with '
                      'the exact metric name, or kind=clarify if a needed business definition is '
                      'unavailable. For SQL, fully qualify each table and use only listed columns. '
                      'For MetricFlow, the tool applies the 2025 date window and accepts '
                      'group_by=order_id__currency when an INR slice is required. '
                      'Do not invent business definitions. Keep unused JSON fields as empty strings.\n\n'
                      f'{exposure}\nQuestion: {item["question"]}')
            record = {'arm': arm, 'question_id': item['id'], 'question': item['question']}
            try:
                action, stats = model_call(prompt, f'{arm}_{item["id"]}')
                record.update(action=action, stats=stats)
            except Exception as exc:
                record['error'] = str(exc)
            output['runs'].append(record)
            (HERE / 'plans.json').write_text(json.dumps(output, indent=2) + '\n')
            print(arm, item['id'], record.get('action'), record.get('error'), flush=True)


if __name__ == '__main__':
    main()
