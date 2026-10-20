"""Evaluate stored query plans locally in Snowflake; never calls a model."""

from __future__ import annotations

import csv
import json
import os
import shutil
import subprocess
import time
from decimal import Decimal
from pathlib import Path

import snowflake.connector
import sqlglot
from sqlglot import exp
import yaml


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MF = Path(os.environ.get('MF_BIN') or shutil.which('mf') or '')
METRICS = {p.stem for p in (ROOT / 'dbt_zomato/models/metrics').rglob('*.yml')}
TABLES_A = {
    'SOURCES': ['ORDERS', 'ORDER_ITEMS', 'RESTAURANTS', 'FOOD', 'USERS', 'MENU', 'REVIEWS'],
    'STAGING': ['STG_ZOMATO__ORDER', 'STG_ZOMATO__ORDER_ITEM', 'STG_ZOMATO__RESTAURANT',
                'STG_ZOMATO__FOOD', 'STG_ZOMATO__USER', 'STG_ZOMATO__MENU', 'STG_ZOMATO__REVIEW'],
}
TABLES_E = {
    **TABLES_A,
    'INTERMEDIATE': ['INT_ORDER_BASE', 'INT_ORDER_FINANCIALS', 'INT_ORDER_FULFILLMENT',
                     'INT_ORDER_ITEM_ROLLUP', 'INT_DATE_SPINE', 'INT_DATE_FEATURES'],
    'CORE': ['FACT_ORDER', 'FACT_ORDER_ITEM', 'DIM_CUSTOMER', 'DIM_RESTAURANT', 'DIM_FOOD', 'DIM_DATE'],
    'MARTS': ['MART_ORDER_CITY_CURRENCY_DAY_UTC', 'MART_DELIVERY_CITY_HOUR_UTC',
              'MART_ORDER_RESTAURANT_CURRENCY_DAY_UTC', 'MART_ORDER_ITEM_CITY_CURRENCY_DAY_UTC'],
}


def profile() -> dict:
    return yaml.safe_load(Path.home().joinpath('.dbt/profiles.yml').read_text())['dbt_zomato']['outputs']['dev']


def check_sql(statement: str, arm: str) -> str:
    trees = sqlglot.parse(statement, read='snowflake')
    if len(trees) != 1 or not isinstance(trees[0], exp.Select):
        raise ValueError('Only one SELECT is allowed')
    tree = trees[0]
    if any(tree.find(t) for t in (exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop, exp.Command)):
        raise ValueError('Write or command operation rejected')
    allowed = TABLES_A if arm == 'A' else TABLES_E
    ctes = {x.alias.upper() for x in tree.find_all(exp.CTE)}
    for table in tree.find_all(exp.Table):
        if table.name.upper() in ctes and not table.db:
            continue
        schema = table.db.upper() if table.db else ''
        catalog = table.catalog.upper() if table.catalog else 'ZOMATO_DLR'
        if catalog != 'ZOMATO_DLR' or table.name.upper() not in allowed.get(schema, []):
            raise ValueError(f'Object outside arm {arm}: {catalog}.{schema}.{table.name}')
    return statement


def metric_result(name: str, group_by: str, p: dict) -> dict:
    if name not in METRICS:
        raise ValueError('Unknown MetricFlow metric')
    if group_by not in ('', 'order_id__currency'):
        raise ValueError('Unsupported MetricFlow group_by')
    env = os.environ.copy()
    env.update(DBT_PROFILES_DIR=os.environ.get('DBT_PROFILES_DIR', '/tmp/zomato-dlr-dbt-profile'),
               DBT_SNOWFLAKE_ACCOUNT=p['account'], DBT_SNOWFLAKE_USER=p['user'],
               DBT_ENV_SECRET_SNOWFLAKE_PASSWORD=p['password'])
    output_file = Path('/tmp') / f'zomato-dlr-mf-{name}-{group_by or "overall"}.csv'
    output_file.unlink(missing_ok=True)
    cmd = [str(MF), 'query', '--metrics', name, '--start-time', '2025-01-01',
           '--end-time', '2025-12-31', '--csv', str(output_file), '--quiet']
    if group_by:
        cmd.extend(['--group-by', group_by])
    for attempt in range(2):
        run = subprocess.run(cmd, cwd=ROOT / 'dbt_zomato', env=env,
                             capture_output=True, text=True, timeout=90)
        if run.returncode == 0:
            with output_file.open(newline='') as f:
                rows = list(csv.DictReader(f))
            if group_by:
                rows = [x for x in rows if x['ORDER_ID__CURRENCY'] == 'INR']
            if len(rows) != 1:
                raise ValueError(f'Expected one MetricFlow result, got {len(rows)}')
            return {'value': rows[0][name.upper()], 'infrastructure_retries': attempt,
                    'group_by': group_by}
        if attempt == 0 and ('EPIPE' in run.stdout or 'EPIPE' in run.stderr):
            continue
        raise RuntimeError(f'MetricFlow failed: {(run.stdout + run.stderr)[-220:]}')
    raise RuntimeError('MetricFlow exhausted retries')


def main() -> None:
    if not MF.is_file():
        raise FileNotFoundError('Set MF_BIN to the MetricFlow executable')
    plans = json.loads((HERE / 'plans.json').read_text())
    p = profile()
    for attempt in range(2):
        try:
            conn = snowflake.connector.connect(
                account=p['account'], user=p['user'], password=p['password'],
                warehouse='ZOMATO_WH', database='ZOMATO_DLR', schema='STAGING',
                role='DBT_LAYER_REFACTOR_ROLE', login_timeout=30,
                session_parameters={'STATEMENT_TIMEOUT_IN_SECONDS': 60})
            break
        except snowflake.connector.errors.NonRetryableTlsError:
            if attempt:
                raise
            time.sleep(1)
    with conn.cursor() as cur:
        cur.execute((HERE / 'gold.local.sql').read_text())
        gold = dict(zip([f'Q{i}' for i in range(1, 6)], map(str, cur.fetchone())))
    results = {'model': plans['model'], 'repo_revision': plans['repo_revision'],
               'gold': gold, 'runs': []}
    tolerances = {'Q1': Decimal('0'), 'Q2': Decimal('0.01'), 'Q3': Decimal('0.0001'),
                  'Q4': Decimal('0.0001'), 'Q5': Decimal('0.0001')}
    for record in plans['runs']:
        item = dict(record)
        try:
            action = item['action']
            if action['kind'] == 'clarify':
                item['result'] = {'clarification': action['reason']}
                item['numeric_correct'] = False
            elif action['kind'] == 'metricflow':
                if item['arm'] != 'E':
                    raise ValueError('MetricFlow not available in A')
                item['result'] = metric_result(action['metric'], action.get('group_by', ''), p)
            elif action['kind'] == 'sql':
                query = check_sql(action['query'], item['arm'])
                with conn.cursor() as cur:
                    cur.execute(query)
                    rows = cur.fetchmany(2)
                    if len(rows) != 1 or len(rows[0]) != 1:
                        raise ValueError('Expected one scalar result')
                    item['result'] = {'value': str(rows[0][0]), 'query_id': cur.sfqid}
            else:
                raise ValueError('Unknown action')
            if 'value' in item['result']:
                item['numeric_correct'] = abs(Decimal(item['result']['value'])
                                              - Decimal(gold[item['question_id']])) <= tolerances[item['question_id']]
        except Exception as exc:
            item['error'] = str(exc)
            item['numeric_correct'] = False
        results['runs'].append(item)
        (HERE / 'results.local.json').write_text(json.dumps(results, indent=2) + '\n')
        print(item['arm'], item['question_id'], item.get('result'),
              item['numeric_correct'], item.get('error'), flush=True)
    conn.close()


if __name__ == '__main__':
    main()
