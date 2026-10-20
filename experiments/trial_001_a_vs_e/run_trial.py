"""Full-answer runner for A vs E trial.

Two-turn flow per attempt:
  1. Model receives question + arm schema description, returns a plan (SQL / MetricFlow / clarify).
  2. Evaluator executes the plan against Snowflake or MetricFlow.
  3. Model receives the result and writes the final answer.
Each attempt is saved atomically to run.local/attempts/<id>.json.
Re-running skips attempts already marked completed.

Prerequisites:
  pip install snowflake-connector-python sqlglot PyYAML
  Authenticated Codex CLI on PATH or CODEX_CLI_PATH env var.
  MetricFlow on PATH or MF_BIN env var (only required for arm E).
  Project 1 dbt profile at DBT_PROFILES_DIR (default /tmp/zomato-dlr-dbt-profile).
  Snowflake credentials: DBT_SNOWFLAKE_ACCOUNT, DBT_SNOWFLAKE_USER, DBT_ENV_SECRET_SNOWFLAKE_PASSWORD.

Usage:
  python run_trial.py                          # Q01-Q05, both arms, 1 attempt each
  python run_trial.py --arm A                  # arm A only
  python run_trial.py --questions Q01 Q03      # specific questions
  python run_trial.py --attempts 3             # three independent attempts per question-arm pair
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import snowflake.connector
import sqlglot
from sqlglot import exp
from project1_profile import profile as load_profile


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RUN_DIR = HERE / "run.local"
ATTEMPTS_DIR = RUN_DIR / "attempts"
ISOLATED = Path("/tmp/zomato-dlr-trial-runner")

CLI = Path(os.environ.get("CODEX_CLI_PATH") or shutil.which("codex") or "")
MF = Path(os.environ.get("MF_BIN") or shutil.which("mf") or "")
MODEL = "gpt-6.1-sol"

METRICS = {p.stem for p in (ROOT / "dbt_zomato/models/metrics").rglob("*.yml")}

TABLES_A = {
    "SOURCES": ["ORDERS", "ORDER_ITEMS", "RESTAURANTS", "FOOD", "USERS", "MENU", "REVIEWS"],
    "STAGING": ["STG_ZOMATO__ORDER", "STG_ZOMATO__ORDER_ITEM", "STG_ZOMATO__RESTAURANT",
                "STG_ZOMATO__FOOD", "STG_ZOMATO__USER", "STG_ZOMATO__MENU", "STG_ZOMATO__REVIEW"],
}
TABLES_E = {
    **TABLES_A,
    "INTERMEDIATE": ["INT_ORDER_BASE", "INT_ORDER_FINANCIALS", "INT_ORDER_FULFILLMENT",
                     "INT_ORDER_ITEM_ROLLUP", "INT_DATE_SPINE", "INT_DATE_FEATURES"],
    "CORE": ["FACT_ORDER", "FACT_ORDER_ITEM", "DIM_CUSTOMER", "DIM_RESTAURANT", "DIM_FOOD", "DIM_DATE"],
    "MARTS": ["MART_ORDER_CITY_CURRENCY_DAY_UTC", "MART_DELIVERY_CITY_HOUR_UTC",
              "MART_ORDER_RESTAURANT_CURRENCY_DAY_UTC", "MART_ORDER_ITEM_CITY_CURRENCY_DAY_UTC"],
}

PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "kind": {"type": "string", "enum": ["sql", "metricflow", "clarify"]},
        "query": {"type": "string"},
        "metric": {"type": "string"},
        "group_by": {"type": "string"},
        "reason": {"type": "string"},
    },
    "required": ["kind", "query", "metric", "group_by", "reason"],
    "additionalProperties": False,
}

A_SCHEMA = """\
SQL objects for arm A — SOURCES (all columns TEXT, raw values) and STAGING (typed, cleaned):

ZOMATO_DLR.SOURCES.ORDERS (ORDER_ID, ORDER_TIMESTAMP, ORDER_DATE, USER_ID, R_ID, RESTAURANT_CITY,
  CUISINE, ITEMS_COUNT, SALES_QTY, SUBTOTAL, DISCOUNT, DELIVERY_FEE, GST, SALES_AMOUNT, CURRENCY,
  PAYMENT_METHOD, ORDER_STATUS, CUSTOMER_RATING, DELIVERY_TIME_MIN — all TEXT)
ZOMATO_DLR.SOURCES.ORDER_ITEMS (ORDER_ITEM_ID, ORDER_ID, R_ID, F_ID, PRICE, QUANTITY,
  LINE_AMOUNT — all TEXT)
ZOMATO_DLR.SOURCES.RESTAURANTS (ID, NAME, CITY, RATING, RATING_COUNT, COST, CUISINE,
  LIC_NO — all TEXT)
ZOMATO_DLR.SOURCES.FOOD (F_ID, ITEM, VEG_OR_NON_VEG — all TEXT)
ZOMATO_DLR.SOURCES.USERS (USER_ID, NAME, EMAIL, AGE, GENDER, MARITAL_STATUS, OCCUPATION,
  MONTHLY_INCOME, EDUCATIONAL_QUALIFICATIONS, FAMILY_SIZE — all TEXT)
ZOMATO_DLR.SOURCES.MENU (MENU_ID, R_ID, F_ID, CUISINE, PRICE — all TEXT)
ZOMATO_DLR.SOURCES.REVIEWS (REVIEW_ID, ORDER_ID, USER_ID, RESTAURANT_ID, RATING, COMMENT,
  REVIEW_DATE — all TEXT)

ZOMATO_DLR.STAGING.STG_ZOMATO__ORDER (ORDER_ID NUMBER, ORDER_TIMESTAMP TIMESTAMP, ORDER_DATE DATE,
  CUSTOMER_ID NUMBER, RESTAURANT_ID NUMBER, CITY TEXT, CUISINE TEXT, ITEMS_COUNT NUMBER,
  SALES_QTY NUMBER, SUBTOTAL NUMBER, DISCOUNT NUMBER, DELIVERY_FEE NUMBER, GST NUMBER,
  SALES_AMOUNT NUMBER, CURRENCY TEXT, PAYMENT_METHOD TEXT, ORDER_STATUS TEXT,
  IS_DELIVERED BOOLEAN, IS_CANCELLED BOOLEAN, IS_REFUNDED BOOLEAN,
  CUSTOMER_RATING NUMBER, DELIVERY_TIME_MIN NUMBER)
ZOMATO_DLR.STAGING.STG_ZOMATO__ORDER_ITEM (ORDER_ITEM_ID NUMBER, ORDER_ID NUMBER,
  RESTAURANT_ID NUMBER, F_ID TEXT, PRICE NUMBER, QUANTITY NUMBER, LINE_AMOUNT NUMBER)
ZOMATO_DLR.STAGING.STG_ZOMATO__RESTAURANT (RESTAURANT_ID NUMBER, RESTAURANT_NAME TEXT,
  CITY TEXT, CUISINE TEXT, RATING NUMBER, RATING_COUNT NUMBER, COST_FOR_TWO NUMBER,
  LICENSE_NO TEXT)
ZOMATO_DLR.STAGING.STG_ZOMATO__FOOD (FOOD_ID TEXT, FOOD_NAME TEXT, VEG_OR_NON_VEG TEXT)
ZOMATO_DLR.STAGING.STG_ZOMATO__USER (CUSTOMER_ID NUMBER, CUSTOMER_NAME TEXT, EMAIL TEXT,
  AGE NUMBER, GENDER TEXT, MARITAL_STATUS TEXT, OCCUPATION TEXT, INCOME_BAND TEXT,
  EDUCATION TEXT, FAMILY_SIZE NUMBER)
ZOMATO_DLR.STAGING.STG_ZOMATO__MENU (MENU_ID TEXT, RESTAURANT_ID NUMBER, FOOD_ID TEXT,
  CUISINE TEXT, PRICE NUMBER)
ZOMATO_DLR.STAGING.STG_ZOMATO__REVIEW (REVIEW_ID NUMBER, ORDER_ID NUMBER, CUSTOMER_ID NUMBER,
  RESTAURANT_ID NUMBER, RATING NUMBER, COMMENT TEXT, REVIEW_DATE DATE)

Grain: STG order = one row per ORDER_ID; STG order item = one row per ORDER_ITEM_ID.
ORDER_DATE is the recorded order date in the source; it is not converted to UTC.
IS_DELIVERED / IS_CANCELLED / IS_REFUNDED are derived from ORDER_STATUS.
DELIVERED_SALES_AMOUNT is not available; use SALES_AMOUNT filtered to delivered orders.
AGE_SEGMENT is not available; derive from AGE: <25 Gen Z, <40 Millennial, <55 Gen X,
  null→Unknown, else Boomer.
"""

E_EXTRA = """\

Additional SQL objects for arm E — INTERMEDIATE, CORE, and MARTS:

ZOMATO_DLR.INTERMEDIATE.INT_ORDER_BASE (ORDER_ID, ORDER_TIMESTAMP_SOURCE TIMESTAMP, ORDER_DATE DATE,
  ORDER_HOUR_SOURCE, CUSTOMER_ID, RESTAURANT_ID, CITY, CUISINE, CURRENCY, PAYMENT_METHOD,
  SOURCE_ITEMS_COUNT, SOURCE_SALES_QTY)
ZOMATO_DLR.INTERMEDIATE.INT_ORDER_FINANCIALS (ORDER_ID, SUBTOTAL, DISCOUNT, DELIVERY_FEE, GST,
  SALES_AMOUNT, CALCULATED_SALES_AMOUNT, SALES_AMOUNT_DELTA, DELIVERED_SALES_AMOUNT)
ZOMATO_DLR.INTERMEDIATE.INT_ORDER_FULFILLMENT (ORDER_ID, ORDER_STATUS, IS_DELIVERED, IS_CANCELLED,
  IS_REFUNDED, CUSTOMER_RATING, DELIVERY_TIME_MIN)
ZOMATO_DLR.INTERMEDIATE.INT_ORDER_ITEM_ROLLUP (ORDER_ID, ITEM_LINE_COUNT, ITEM_QUANTITY,
  DISTINCT_FOOD_COUNT, ITEM_LINE_AMOUNT, CALCULATED_ITEM_AMOUNT, ITEM_AMOUNT_DELTA)
ZOMATO_DLR.INTERMEDIATE.INT_DATE_SPINE (DATE_DAY DATE)
ZOMATO_DLR.INTERMEDIATE.INT_DATE_FEATURES (DATE_DAY DATE, YEAR, MONTH, MONTH_NAME TEXT,
  DAY_NAME TEXT, IS_WEEKEND BOOLEAN)

ZOMATO_DLR.CORE.FACT_ORDER (ORDER_ID, ORDER_TIMESTAMP TIMESTAMP, ORDER_DATE DATE, ORDER_HOUR,
  CUSTOMER_ID, RESTAURANT_ID, CITY, CUISINE, CURRENCY, PAYMENT_METHOD, ORDER_STATUS,
  IS_DELIVERED BOOLEAN, IS_CANCELLED BOOLEAN, IS_REFUNDED BOOLEAN, ITEMS_COUNT, SALES_QTY,
  ITEM_LINE_COUNT, ITEM_QUANTITY, DISTINCT_FOOD_COUNT, SUBTOTAL, DISCOUNT, DELIVERY_FEE, GST,
  SALES_AMOUNT, CALCULATED_SALES_AMOUNT, SALES_AMOUNT_DELTA, DELIVERED_SALES_AMOUNT,
  ITEM_LINE_AMOUNT, CALCULATED_ITEM_AMOUNT, ITEM_AMOUNT_DELTA, CUSTOMER_RATING, DELIVERY_TIME_MIN)
ZOMATO_DLR.CORE.FACT_ORDER_ITEM (ORDER_ITEM_ID, ORDER_ID, RESTAURANT_ID, FOOD_ID, ORDER_TS TIMESTAMP,
  ORDER_DATE DATE, CITY, PRICE, QUANTITY, LINE_AMOUNT, CALCULATED_LINE_AMOUNT, LINE_AMOUNT_DELTA)
ZOMATO_DLR.CORE.DIM_CUSTOMER (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, AGE, AGE_SEGMENT TEXT, GENDER,
  MARITAL_STATUS, OCCUPATION, INCOME_BAND, EDUCATION, FAMILY_SIZE)
ZOMATO_DLR.CORE.DIM_RESTAURANT (RESTAURANT_ID, RESTAURANT_NAME, CITY, CUISINE, RATING,
  RATING_COUNT, COST_FOR_TWO)
ZOMATO_DLR.CORE.DIM_FOOD (FOOD_ID, FOOD_NAME, VEG_OR_NON_VEG)
ZOMATO_DLR.CORE.DIM_DATE (DATE_DAY DATE, YEAR, MONTH, MONTH_NAME TEXT, DAY_NAME TEXT,
  IS_WEEKEND BOOLEAN)

ZOMATO_DLR.MARTS.MART_ORDER_CITY_CURRENCY_DAY_UTC (ORDER_DATE_UTC DATE, CITY, CURRENCY,
  ORDER_COUNT, DELIVERED_ORDER_COUNT, CANCELLED_ORDER_COUNT, REFUNDED_ORDER_COUNT,
  DELIVERED_SALES_AMOUNT)
ZOMATO_DLR.MARTS.MART_ORDER_RESTAURANT_CURRENCY_DAY_UTC (ORDER_DATE_UTC DATE, RESTAURANT_ID,
  CURRENCY, ORDER_COUNT, DELIVERED_ORDER_COUNT, CANCELLED_ORDER_COUNT, REFUNDED_ORDER_COUNT,
  DELIVERED_SALES_AMOUNT, CUSTOMER_RATING_SUM, CUSTOMER_RATING_OBSERVATION_COUNT,
  DELIVERY_TIME_SUM_MIN, DELIVERY_TIME_OBSERVATION_COUNT)
ZOMATO_DLR.MARTS.MART_ORDER_ITEM_CITY_CURRENCY_DAY_UTC (ORDER_DATE_UTC DATE, CITY, CURRENCY,
  ORDER_ITEM_COUNT, ORDERED_QUANTITY, SOURCE_LINE_AMOUNT, CALCULATED_LINE_AMOUNT, LINE_AMOUNT_DELTA)
ZOMATO_DLR.MARTS.MART_DELIVERY_CITY_HOUR_UTC (ORDER_HOUR_UTC TIMESTAMP, CITY,
  DELIVERED_ORDER_COUNT, DELIVERY_TIME_SUM_MIN, DELIVERY_TIME_OBSERVATION_COUNT)

Grain: FACT_ORDER = one row per order; FACT_ORDER_ITEM = one row per item line.
DELIVERED_SALES_AMOUNT = SALES_AMOUNT when IS_DELIVERED is TRUE, else 0.
AGE_SEGMENT in DIM_CUSTOMER: Gen Z (<25), Millennial (<40), Gen X (<55), Unknown (null), Boomer (55+).
MART tables are pre-aggregated by date/city/restaurant/currency; prefer them for city or restaurant
  summaries. JOIN DIM_RESTAURANT on RESTAURANT_ID when restaurant name or cuisine is needed.
MetricFlow metrics available: {metrics}
MetricFlow uses CORE models with a 2025 date window. Use group_by="order_id__currency" for INR slice.
"""

TURN1_TEMPLATE = """\
You are a data analyst in arm {arm}. Use only the SQL objects listed below.
Do not call shell, file, web, or any other tools. Return one JSON action.

Choose kind=sql and write a single read-only Snowflake SELECT.
Choose kind=metricflow with the exact metric name if a MetricFlow metric is the right tool (arm E only).
Choose kind=clarify only if the information is genuinely absent from all accessible tables
  (a column or concept that does not exist in this dataset). Do not clarify because a query is complex.

For SQL: fully qualify every table as CATALOG.SCHEMA.TABLE. Use only the listed columns.
  Return the rows needed to answer the question — do not collapse to a scalar unless the
  question asks for exactly one number.
For MetricFlow: set metric to the exact metric name. Set group_by="order_id__currency" only
  when an INR slice is needed; leave it empty otherwise. The tool applies 2025-01-01 to
  2025-12-31 automatically.
Leave unused JSON fields as empty strings.

{schema}
Question: {question}"""

TURN2_TEMPLATE = """\
You are a data analyst in arm {arm}. You were asked:

{question}

You selected this approach:
{plan_summary}

The query returned:
{result_table}

Write your complete final answer. State all requested values with their units, scope, and date range.
If the question asks for a comparison, state which side is higher or lower.
If the data does not support a causal claim, say so explicitly.
If the data was unavailable, explain what is missing and why the question cannot be answered."""


def _connect_snowflake(p: dict) -> snowflake.connector.SnowflakeConnection:
    for attempt in range(2):
        try:
            return snowflake.connector.connect(
                account=p["account"], user=p["user"], password=p["password"],
                warehouse="ZOMATO_WH", database="ZOMATO_DLR", schema="STAGING",
                role="DBT_LAYER_REFACTOR_ROLE", login_timeout=30,
                session_parameters={"STATEMENT_TIMEOUT_IN_SECONDS": 120},
            )
        except snowflake.connector.errors.NonRetryableTlsError:
            if attempt:
                raise
            time.sleep(1)
    raise RuntimeError("Snowflake connection failed")


def _codex_call(prompt: str, tag: str, schema_path: Path | None) -> tuple[str, dict]:
    ISOLATED.mkdir(exist_ok=True)
    answer_path = ISOLATED / f"{tag}.out"
    answer_path.unlink(missing_ok=True)
    cmd = [str(CLI), "exec", "--ephemeral", "--ignore-user-config", "--skip-git-repo-check",
           "-C", str(ISOLATED), "-s", "read-only", "-m", MODEL,
           "-c", 'model_reasoning_effort="low"', "-o", str(answer_path), "--json", "-"]
    if schema_path:
        cmd += ["--output-schema", str(schema_path)]
    started = time.monotonic()
    run = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=180)
    events = []
    for line in run.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    if run.returncode or not answer_path.exists():
        raise RuntimeError(f"Codex {tag} failed (rc={run.returncode}): {run.stderr[-400:]}")
    tool_items = [e.get("item", {}).get("type") for e in events
                  if e.get("item", {}).get("type") not in (None, "agent_message", "reasoning")]
    if tool_items:
        raise RuntimeError(f"Codex {tag} used tools unexpectedly: {tool_items}")
    usage = next((e.get("usage", {}) for e in events if e.get("type") == "turn.completed"), {})
    return answer_path.read_text().strip(), {
        "seconds": round(time.monotonic() - started, 2), "usage": usage,
    }


def _check_sql(query: str, arm: str) -> None:
    allowed = TABLES_A if arm == "A" else TABLES_E
    trees = sqlglot.parse(query, read="snowflake")
    if len(trees) != 1 or not isinstance(trees[0], exp.Select):
        raise ValueError("Only one SELECT statement is allowed")
    tree = trees[0]
    if any(tree.find(t) for t in (exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop, exp.Command)):
        raise ValueError("Write or DDL operation rejected")
    ctes = {x.alias.upper() for x in tree.find_all(exp.CTE)}
    for table in tree.find_all(exp.Table):
        if table.name.upper() in ctes and not table.db:
            continue
        schema = table.db.upper() if table.db else ""
        catalog = table.catalog.upper() if table.catalog else "ZOMATO_DLR"
        if catalog != "ZOMATO_DLR" or table.name.upper() not in allowed.get(schema, []):
            raise ValueError(f"Object outside arm {arm}: {catalog}.{schema}.{table.name}")


def _run_sql(query: str, arm: str, conn: snowflake.connector.SnowflakeConnection) -> dict:
    _check_sql(query, arm)
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchmany(50)
        cols = [d[0] for d in cur.description]
        return {
            "columns": cols,
            "rows": [[str(v) if v is not None else None for v in row] for row in rows],
            "row_count": len(rows),
            "query_id": cur.sfqid,
        }


def _run_metricflow(metric: str, group_by: str, p: dict) -> dict:
    if metric not in METRICS:
        raise ValueError(f"Unknown metric: {metric!r}")
    if group_by not in ("", "order_id__currency"):
        raise ValueError(f"Unsupported group_by: {group_by!r}")
    env = os.environ.copy()
    env.update(
        DBT_PROFILES_DIR=os.environ.get("DBT_PROFILES_DIR", "/tmp/zomato-dlr-dbt-profile"),
        DBT_SNOWFLAKE_ACCOUNT=p["account"],
        DBT_SNOWFLAKE_USER=p["user"],
        DBT_ENV_SECRET_SNOWFLAKE_PASSWORD=p["password"],
    )
    out_file = Path("/tmp") / f"mf-{metric}-{group_by or 'overall'}.csv"
    out_file.unlink(missing_ok=True)
    cmd = [str(MF), "query", "--metrics", metric,
           "--start-time", "2025-01-01", "--end-time", "2025-12-31",
           "--csv", str(out_file), "--quiet"]
    if group_by:
        cmd += ["--group-by", group_by]
    for attempt in range(2):
        run = subprocess.run(cmd, cwd=ROOT / "dbt_zomato", env=env,
                             capture_output=True, text=True, timeout=90)
        if run.returncode == 0:
            with out_file.open(newline="") as f:
                rows = list(csv.DictReader(f))
            if group_by == "order_id__currency":
                rows = [r for r in rows if r.get("ORDER_ID__CURRENCY") == "INR"]
            cols = list(rows[0].keys()) if rows else []
            return {
                "columns": cols,
                "rows": [[r[c] for c in cols] for r in rows],
                "row_count": len(rows),
                "retries": attempt,
            }
        if attempt == 0 and ("EPIPE" in run.stdout + run.stderr):
            continue
        raise RuntimeError(f"MetricFlow failed: {(run.stdout + run.stderr)[-300:]}")
    raise RuntimeError("MetricFlow exhausted retries")


def _format_result(result: dict | None, plan: dict, result_error: str | None) -> str:
    if plan["kind"] == "clarify":
        return f"No data available — you indicated: {plan['reason']}"
    if result_error:
        return f"The query failed with error: {result_error}"
    if not result or not result.get("rows"):
        return "The query returned no rows."
    cols = result["columns"]
    rows = result["rows"]
    header = " | ".join(str(c) for c in cols)
    sep = "-" * len(header)
    lines = [header, sep]
    for row in rows[:25]:
        lines.append(" | ".join("NULL" if v is None else str(v) for v in row))
    if result["row_count"] > 25:
        lines.append(f"... (showing first 25 of {result['row_count']} rows)")
    return "\n".join(lines)


def _plan_summary(plan: dict) -> str:
    if plan["kind"] == "sql":
        return f"SQL query:\n{plan['query']}"
    if plan["kind"] == "metricflow":
        gb = f", group_by={plan['group_by']!r}" if plan.get("group_by") else ""
        return f"MetricFlow metric: {plan['metric']}{gb}"
    return f"Clarification: {plan['reason']}"


def _load_questions(here: Path) -> dict[str, dict]:
    q1 = json.loads((here / "questions.json").read_text())
    q2 = json.loads((here / "questions_q06_q25.json").read_text())
    return {f"Q{int(q['id'][1:]):02d}": q for q in q1 + q2}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm", choices=["A", "E"],
                        help="Run a single arm; omit for both A and E")
    parser.add_argument("--questions", nargs="+", metavar="QID",
                        help="Question IDs to run e.g. Q01 Q03 Q26; default Q01-Q05")
    parser.add_argument("--attempts", type=int, default=1,
                        help="Independent attempts per question-arm pair (default 1)")
    args = parser.parse_args()

    if not CLI.is_file():
        raise FileNotFoundError("Authenticated Codex CLI not found. "
                                "Set CODEX_CLI_PATH or ensure codex is on PATH.")

    all_questions = _load_questions(HERE)
    if args.questions:
        questions = [all_questions[qid] for qid in args.questions if qid in all_questions]
    else:
        questions = [all_questions[f"Q{i:02d}"] for i in range(1, 6)]

    arms = [args.arm] if args.arm else ["A", "E"]
    needs_mf = "E" in arms and any(
        all_questions.get(f"Q{i:02d}", {}).get("metric") for i in range(1, 6)
    )

    ISOLATED.mkdir(exist_ok=True)
    schema_file = ISOLATED / "plan_schema.json"
    schema_file.write_text(json.dumps(PLAN_SCHEMA))
    ATTEMPTS_DIR.mkdir(parents=True, exist_ok=True)

    p = load_profile()
    conn = _connect_snowflake(p)
    metrics_list = sorted(METRICS)

    try:
        for arm in arms:
            schema_text = A_SCHEMA + (E_EXTRA.format(metrics=", ".join(metrics_list))
                                      if arm == "E" else "")
            for q in questions:
                qid = f"Q{int(q['id'][1:]):02d}"
                for rep in range(1, args.attempts + 1):
                    attempt_id = f"{arm}-{qid}-r{rep}"
                    attempt_file = ATTEMPTS_DIR / f"{attempt_id}.json"

                    if attempt_file.exists():
                        saved = json.loads(attempt_file.read_text())
                        if saved.get("status") == "completed":
                            print(f"skip  {attempt_id}", flush=True)
                            continue

                    attempt: dict = {
                        "id": attempt_id, "arm": arm, "question_id": qid,
                        "question": q["question"], "repetition": rep,
                        "model": MODEL, "status": "in_progress",
                    }
                    attempt_file.write_text(json.dumps(attempt, indent=2) + "\n")
                    t_start = time.monotonic()

                    # Turn 1 — plan selection
                    t1_prompt = TURN1_TEMPLATE.format(
                        arm=arm, schema=schema_text, question=q["question"])
                    try:
                        plan_text, t1_stats = _codex_call(t1_prompt, f"{attempt_id}-t1", schema_file)
                        plan = json.loads(plan_text)
                    except Exception as exc:
                        attempt.update(status="failed", error=f"turn1: {exc}")
                        attempt_file.write_text(json.dumps(attempt, indent=2) + "\n")
                        print(f"FAIL  {attempt_id}  turn1: {exc}", flush=True)
                        continue

                    attempt["plan"] = plan
                    attempt["turn1_stats"] = t1_stats

                    # Execute plan
                    result: dict | None = None
                    result_error: str | None = None
                    if plan["kind"] == "sql":
                        try:
                            result = _run_sql(plan["query"], arm, conn)
                        except Exception as exc:
                            result_error = str(exc)
                    elif plan["kind"] == "metricflow":
                        if arm != "E":
                            result_error = "MetricFlow is not available in arm A"
                        elif not MF.is_file():
                            result_error = "MetricFlow binary not found; set MF_BIN"
                        else:
                            try:
                                result = _run_metricflow(
                                    plan["metric"], plan.get("group_by", ""), p)
                            except Exception as exc:
                                result_error = str(exc)

                    attempt["result"] = result
                    attempt["result_error"] = result_error

                    # Turn 2 — final answer
                    result_table = _format_result(result, plan, result_error)
                    t2_prompt = TURN2_TEMPLATE.format(
                        arm=arm, question=q["question"],
                        plan_summary=_plan_summary(plan),
                        result_table=result_table,
                    )
                    try:
                        final_answer, t2_stats = _codex_call(t2_prompt, f"{attempt_id}-t2", None)
                        attempt["final_answer"] = final_answer
                        attempt["turn2_stats"] = t2_stats
                    except Exception as exc:
                        attempt.update(status="failed", error=f"turn2: {exc}")
                        attempt_file.write_text(json.dumps(attempt, indent=2) + "\n")
                        print(f"FAIL  {attempt_id}  turn2: {exc}", flush=True)
                        continue

                    attempt["status"] = "completed"
                    attempt["total_seconds"] = round(time.monotonic() - t_start, 2)
                    attempt_file.write_text(json.dumps(attempt, indent=2) + "\n")
                    print(f"OK    {attempt_id}  plan={plan['kind']}"
                          f"  {attempt['total_seconds']}s", flush=True)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
