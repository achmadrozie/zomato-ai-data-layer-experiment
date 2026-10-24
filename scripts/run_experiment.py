"""Run the 25-question A–F data-layer experiment with one fixed model.

The evaluated model only receives its arm's catalog, the question, and tool
results. Author references and gold SQL are deliberately never opened here.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import re
import shutil
import socket
import subprocess
import tempfile
import time
from datetime import date, datetime, timezone
from pathlib import Path

import snowflake.connector
import sqlglot
import yaml
from dotenv import load_dotenv
from openai import OpenAI
from sqlglot import exp


# The local network advertises unreachable IPv6 routes to api.openai.com.
# Prefer reachable IPv4 addresses when both address families are available.
_getaddrinfo = socket.getaddrinfo


def _ipv4_first(*args, **kwargs):
    addresses = _getaddrinfo(*args, **kwargs)
    ipv4 = [address for address in addresses if address[0] == socket.AF_INET]
    return ipv4 + [address for address in addresses if address[0] != socket.AF_INET]


socket.getaddrinfo = _ipv4_first


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
QUESTIONS = EXPERIMENTS / "questions_25.json"
CONTEXT = ROOT / "context/v1/business_glossary.md"
METRIC_ROOT = ROOT / "dbt_zomato/models/metrics"
RUN_DIR = EXPERIMENTS / "run.local" / "new_run"
MODEL = "gpt-4.1"
SCHEMAS = {
    "A": ("SOURCES", "STAGING"),
    "B": ("SOURCES", "STAGING", "INTERMEDIATE"),
    "C": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE"),
    "D": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
    "E": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
    "F": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
}
EXCLUDED = {("STAGING", "METRICFLOW_TIME_SPINE")}
SENSITIVE_COLUMNS = {"PASSWORD", "EMAIL", "NAME", "CUSTOMER_NAME", "COMMENT",
                     "LIC_NO", "LICENSE_NO"}
SENSITIVE_RESULT_COLUMNS = {"USER_ID", "CUSTOMER_ID", "ORDER_ID", "ORDER_ITEM_ID",
                            "REVIEW_ID", "EMAIL", "NAME", "CUSTOMER_NAME", "COMMENT"}
GRAINS = {
    "ORDERS": "one order", "ORDER_ITEMS": "one item line",
    "STG_ZOMATO__ORDER": "one order", "STG_ZOMATO__ORDER_ITEM": "one item line",
    "INT_ORDER_BASE": "one order", "INT_ORDER_FINANCIALS": "one order",
    "INT_ORDER_FULFILLMENT": "one order", "INT_ORDER_ITEM_ROLLUP": "one order",
    "INT_DATE_SPINE": "one calendar date", "INT_DATE_FEATURES": "one calendar date",
    "FACT_ORDER": "one order", "FACT_ORDER_ITEM": "one item line",
    "DIM_CUSTOMER": "one customer", "DIM_RESTAURANT": "one restaurant",
    "DIM_FOOD": "one food item", "DIM_DATE": "one calendar date",
    "MART_ORDER_CITY_CURRENCY_DAY_UTC": "order date × order city × currency",
    "MART_DELIVERY_CITY_HOUR_UTC": "source order hour × order city",
    "MART_ORDER_RESTAURANT_CURRENCY_DAY_UTC": "order date × restaurant × currency",
    "MART_ORDER_ITEM_CITY_CURRENCY_DAY_UTC": "order date × order city × currency",
}
ACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "kind": {"type": "string", "enum": ["sql", "metricflow", "answer", "clarify"]},
        "query": {"type": "string"},
        "metrics": {"type": "string"},
        "group_by": {"type": "string"},
        "start_time": {"type": "string"},
        "end_time": {"type": "string"},
        "answer": {"type": "string"},
        "reason": {"type": "string"},
    },
    "required": ["kind", "query", "metrics", "group_by", "start_time", "end_time",
                 "answer", "reason"],
    "additionalProperties": False,
}


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def save(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temp.replace(path)


def metric_docs() -> dict[str, str]:
    result: dict[str, str] = {}
    for config in sorted(METRIC_ROOT.rglob("*.yml")):
        source = yaml.safe_load(config.read_text()) or {}
        for metric in source.get("metrics", []):
            description = config.with_suffix(".md")
            lines = description.read_text().splitlines() if description.exists() else []
            result[metric["name"]] = " ".join(
                line.strip() for line in lines
                if line.strip() and not line.strip().startswith("{%")
            )
    return result


def get_catalog(conn) -> dict[tuple[str, str], list[tuple[str, str]]]:
    catalog: dict[tuple[str, str], list[tuple[str, str]]] = {}
    with conn.cursor() as cur:
        cur.execute("""
            SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE
            FROM ZOMATO_DLR.INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA IN ('SOURCES','STAGING','INTERMEDIATE','CORE','MARTS')
            ORDER BY TABLE_SCHEMA, TABLE_NAME, ORDINAL_POSITION
        """)
        for schema, table, column, typ in cur:
            if (schema, table) in EXCLUDED:
                continue
            if column.upper() in SENSITIVE_COLUMNS:
                continue
            catalog.setdefault((schema, table), []).append((column, typ))
    expected = {"SOURCES": 7, "STAGING": 7, "INTERMEDIATE": 6,
                "CORE": 6, "MARTS": 4}
    actual = {schema: sum(s == schema for s, _ in catalog) for schema in expected}
    if actual != expected:
        raise RuntimeError(f"Warehouse object inventory changed: {actual}")
    return catalog


def system_prompt(arm: str, catalog: dict, metrics: dict[str, str], context: str) -> str:
    object_lines = []
    for (schema, table), columns in sorted(catalog.items()):
        if schema not in SCHEMAS[arm]:
            continue
        grain = GRAINS.get(table, "source or dimension grain; verify joins")
        column_text = ", ".join(f"{name}:{typ}" for name, typ in columns)
        object_lines.append(f"ZOMATO_DLR.{schema}.{table} [{grain}] — {column_text}")
    instructions = (
        "You are an analytics agent answering one question on the frozen ZOMATO_DLR "
        "snapshot. Use only the SQL objects listed below. Return one JSON action at a time. "
        "You may issue up to three read-only queries, then answer or clarify. "
        "For SQL, use a single Snowflake SELECT with fully qualified table names; "
        "return only the rows needed for the requested answer (maximum 40), not raw "
        "identifiers or personal information. Keep sums at their proper grain: joining "
        "item lines to orders repeats order amounts. A 2025 recorded order date means "
        "ORDER_DATE >= '2025-01-01' AND ORDER_DATE < '2026-01-01'. Money has source "
        "currency, with no conversion. _UTC mart names are labels, not proven timezone "
        "conversion. If a business policy is needed but has not been supplied, choose "
        "clarify and name the missing rule. If data is unavailable, say so; do not "
        "invent it. A correlation or decomposition alone does not prove causation. "
        "In the final answer include every requested value, population, unit, and "
        "interpretation. Keep at least six decimals for non-integer rates and averages. "
        "Leave unused JSON fields empty.\n\nACCESSIBLE SQL OBJECTS:\n"
        + "\n".join(object_lines)
    )
    if arm in ("E", "F"):
        instructions += (
            "\n\nMETRICFLOW: You may choose kind=metricflow using comma-separated exact "
            "metric names. Optional group_by is comma-separated dimensions. The "
            "tool accepts an inclusive start_time/end_time in 2025, defaulting to the "
            "full year. For the full year, leave both date fields empty or use "
            "2025-01-01 and 2025-12-31. Valid group_by examples from this semantic "
            "model include order_id__city (recorded order city), "
            "restaurant_id__city (restaurant city), order_id__cuisine, "
            "restaurant_id__cuisine, order_id__currency, order_id__order_status, "
            "customer_id__age_segment, food_id__veg_or_non_veg, "
            "calendar_date__day_name, calendar_date__calendar_month, and "
            "metric_time__month. The available dimensions vary by metric. "
            "Use SQL for filters or calculations the metric tool cannot express. "
            "Governed metric definitions:\n"
            + "\n".join(f"- {name}: {description}"
                        for name, description in sorted(metrics.items()))
        )
    if arm == "F":
        instructions += "\n\nBUSINESS CONTEXT FOR THIS ARM ONLY:\n" + context
    return instructions


def validate_sql(query: str, arm: str, catalog: dict) -> None:
    trees = sqlglot.parse(query, read="snowflake")
    if len(trees) != 1 or not isinstance(trees[0], exp.Select):
        raise ValueError("Expected exactly one SELECT")
    tree = trees[0]
    forbidden = (exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop,
                 exp.Alter, exp.Merge, exp.Command)
    if any(tree.find(kind) for kind in forbidden):
        raise ValueError("Write, DDL, and commands are forbidden")
    for star in tree.find_all(exp.Star):
        if not isinstance(star.parent, exp.Count):
            raise ValueError("SELECT * is forbidden")
    for column in tree.find_all(exp.Column):
        if column.name.upper() in SENSITIVE_COLUMNS:
            raise ValueError(f"Sensitive column forbidden: {column.name}")
    ctes = {cte.alias.upper() for cte in tree.find_all(exp.CTE)}
    tables = list(tree.find_all(exp.Table))
    if not tables:
        raise ValueError("SQL must query an allowed object")
    for table in tables:
        if not table.db and table.name.upper() in ctes:
            continue
        name = (table.db.upper(), table.name.upper())
        if (table.catalog.upper() != "ZOMATO_DLR" or
                name not in catalog or name[0] not in SCHEMAS[arm]):
            raise ValueError(f"Object outside arm {arm}: {table.sql()}")


def run_sql(conn, query: str, arm: str, catalog: dict) -> dict:
    validate_sql(query, arm, catalog)
    started = time.monotonic()
    with conn.cursor() as cur:
        cur.execute(query)
        columns = [item[0] for item in cur.description]
        if set(map(str.upper, columns)) & SENSITIVE_RESULT_COLUMNS:
            raise ValueError("Result includes a row-level identifier or sensitive column")
        rows = cur.fetchmany(41)
        if len(rows) > 40:
            raise ValueError("Result exceeds 40 rows; return a smaller aggregate")
        return {
            "columns": columns,
            "rows": [[str(value) if value is not None else None for value in row]
                     for row in rows],
            "query_id": cur.sfqid,
            "seconds": round(time.monotonic() - started, 2),
        }


def validate_date(value: str, default: str) -> str:
    if not value:
        return default
    parsed = date.fromisoformat(value)
    if parsed.year != 2025:
        raise ValueError("MetricFlow date must be in 2025")
    return value


def run_metricflow(action: dict, metrics: dict[str, str], mf_bin: Path,
                   mf_pythonpath: str) -> dict:
    names = [part.strip() for part in action["metrics"].split(",") if part.strip()]
    if not names or any(name not in metrics for name in names):
        raise ValueError("Unknown or missing MetricFlow metric")
    group_by = action["group_by"].strip()
    if group_by and not re.fullmatch(r"[A-Za-z0-9_,]+", group_by):
        raise ValueError("Invalid MetricFlow group_by")
    start = validate_date(action["start_time"], "2025-01-01")
    end = validate_date(action["end_time"], "2025-12-31")
    if start > end:
        raise ValueError("MetricFlow end date precedes start date")
    if not mf_bin.is_file():
        raise FileNotFoundError(f"MetricFlow CLI unavailable: {mf_bin}")
    env = os.environ.copy()
    env.update(
        DBT_PROFILES_DIR=env.get("DBT_PROFILES_DIR", "/tmp/zomato-dlr-dbt-profile"),
        DBT_SNOWFLAKE_ACCOUNT=env["SNOWFLAKE_ACCOUNT"],
        DBT_SNOWFLAKE_USER=env["SNOWFLAKE_USER"],
        DBT_ENV_SECRET_SNOWFLAKE_PASSWORD=env["SNOWFLAKE_PASSWORD"],
    )
    if mf_pythonpath:
        env["PYTHONPATH"] = mf_pythonpath
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
        output = Path(tmp.name)
    cmd = [str(mf_bin), "query", "--metrics", ",".join(names),
           "--start-time", start, "--end-time", end, "--csv", str(output),
           "--quiet"]
    if group_by:
        cmd += ["--group-by", group_by]
    started = time.monotonic()
    try:
        run = subprocess.run(cmd, cwd=ROOT / "dbt_zomato", env=env,
                             capture_output=True, text=True, timeout=180)
        if run.returncode:
            detail = run.stdout.strip() or run.stderr.strip()
            raise RuntimeError("MetricFlow query failed: " + detail[:1200])
        with output.open(newline="") as file:
            rows = list(csv.DictReader(file))
        if len(rows) > 40:
            raise ValueError("MetricFlow result exceeds 40 rows; use SQL or coarser grain")
        columns = list(rows[0]) if rows else []
        return {
            "columns": columns,
            "rows": [[row[column] for column in columns] for row in rows],
            "metric_definitions": {name: metrics[name] for name in names},
            "seconds": round(time.monotonic() - started, 2),
        }
    finally:
        output.unlink(missing_ok=True)


def next_action(client: OpenAI, messages: list[dict], model: str,
                reasoning_effort: str | None = None) -> tuple[dict, dict]:
    started = time.monotonic()
    kwargs: dict = {
        "model": model,
        "messages": messages,
        "response_format": {"type": "json_schema", "json_schema": {
            "name": "experiment_action", "strict": True, "schema": ACTION_SCHEMA}},
    }
    if model == "gpt-6-luna":
        if reasoning_effort:
            kwargs["reasoning_effort"] = reasoning_effort
    else:
        kwargs["temperature"] = 0
    response = client.chat.completions.create(**kwargs)
    action = json.loads(response.choices[0].message.content or "{}")
    return action, {
        "seconds": round(time.monotonic() - started, 2),
        "prompt_tokens": response.usage.prompt_tokens if response.usage else None,
        "completion_tokens": response.usage.completion_tokens if response.usage else None,
    }


def run_attempt(client: OpenAI, conn, arm: str, question: dict, catalog: dict,
                metrics: dict[str, str], context: str, args) -> dict:
    prompt = system_prompt(arm, catalog, metrics, context)
    attempt = {
        "id": f"{arm}-{question['id']}-r1", "arm": arm,
        "question_id": question["id"], "stratum": question["stratum"],
        "question": question["question"], "model": args.model,
        "temperature": None if args.model == "gpt-6-luna" else 0,
        "reasoning_effort": args.reasoning_effort if args.model == "gpt-6-luna" else None,
        "seed": args.seed,
        "prompt_sha256": sha256(prompt), "question_sha256": sha256(question["question"]),
        "context_sha256": sha256(context) if arm == "F" else None,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "status": "in_progress", "steps": [],
    }
    messages = [{"role": "system", "content": prompt},
                {"role": "user", "content": question["question"]}]
    started = time.monotonic()
    for step in range(4):
        if step == 3:
            messages.append({"role": "user", "content":
                             "No more queries. Return kind=answer with the supported final "
                             "answer, or kind=clarify if a required rule or data is missing."})
        action, stats = next_action(client, messages, args.model,
                                    reasoning_effort=getattr(args, "reasoning_effort", None))
        record = {"action": action, "model_stats": stats}
        attempt["steps"].append(record)
        kind = action["kind"]
        if kind == "answer":
            attempt.update(status="completed", final_answer=action["answer"],
                           outcome="answer")
            break
        if kind == "clarify":
            attempt.update(status="completed", final_answer=action["reason"],
                           outcome="clarification")
            break
        if step == 3:
            attempt.update(status="failed", error="Model did not give a final answer")
            break
        try:
            if kind == "sql":
                result = run_sql(conn, action["query"], arm, catalog)
            elif kind == "metricflow" and arm in ("E", "F"):
                result = run_metricflow(action, metrics, args.mf_bin,
                                        args.mf_pythonpath)
            else:
                raise ValueError(f"Tool {kind} unavailable in arm {arm}")
            record["result"] = result
            feedback = {"status": "ok", "result": result}
        except Exception as exc:
            record["tool_error"] = f"{type(exc).__name__}: {exc}"
            feedback = {"status": "error", "message": record["tool_error"]}
        messages.append({"role": "assistant", "content": json.dumps(action)})
        messages.append({"role": "user", "content":
                         "Tool response: " + json.dumps(feedback) +
                         "\nUse the result to answer all requested parts, or issue another "
                         "allowed query if needed."})
    attempt["total_seconds"] = round(time.monotonic() - started, 2)
    attempt["finished_utc"] = datetime.now(timezone.utc).isoformat()
    return attempt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--arms", nargs="+", choices=list(SCHEMAS),
                        default=list(SCHEMAS))
    parser.add_argument("--questions", nargs="+", default=None)
    parser.add_argument("--seed", type=int, default=20261021)
    parser.add_argument("--run-dir", type=Path, default=RUN_DIR)
    parser.add_argument("--mf-bin", type=Path,
                        default=Path(os.environ.get("MF_BIN") or shutil.which("mf") or "mf"))
    parser.add_argument("--mf-pythonpath", default=os.environ.get("MF_PYTHONPATH", ""))
    parser.add_argument("--reasoning-effort", default=None,
                        choices=["low", "medium", "high"],
                        help="reasoning_effort for gpt-6-luna (ignored for other models)")
    args = parser.parse_args()
    load_dotenv(ROOT / ".env")
    required = ("OPENAI_API_KEY", "SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER",
                "SNOWFLAKE_PASSWORD")
    missing = [key for key in required if not os.environ.get(key)]
    if missing:
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")
    questions = json.loads(QUESTIONS.read_text())
    if len(questions) != 25 or [q["id"] for q in questions] != [f"Q{i:02d}" for i in range(1, 26)]:
        raise ValueError("Expected exactly Q01–Q25 in order")
    if args.questions:
        unknown = set(args.questions) - {q["id"] for q in questions}
        if unknown:
            parser.error(f"Unknown questions: {sorted(unknown)}")
        questions = [q for q in questions if q["id"] in args.questions]
    metrics = metric_docs()
    if len(metrics) != 19:
        raise ValueError(f"Expected 19 MetricFlow metrics, found {len(metrics)}")
    context = CONTEXT.read_text()
    conn = snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"], user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"], warehouse="ZOMATO_WH",
        database="ZOMATO_DLR", schema="CORE", role="DBT_LAYER_REFACTOR_ROLE",
        login_timeout=30, session_parameters={"STATEMENT_TIMEOUT_IN_SECONDS": 180},
    )
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], timeout=90)
    args.run_dir.mkdir(parents=True, exist_ok=True)
    try:
        catalog = get_catalog(conn)
        jobs = [(arm, question) for arm in args.arms for question in questions]
        random.Random(args.seed).shuffle(jobs)
        for arm, question in jobs:
            identifier = f"{arm}-{question['id']}-r1"
            path = args.run_dir / "attempts" / f"{identifier}.json"
            if path.exists() and json.loads(path.read_text()).get("status") == "completed":
                print("skip", identifier, flush=True)
                continue
            try:
                attempt = run_attempt(client, conn, arm, question, catalog,
                                      metrics, context, args)
            except Exception as exc:
                attempt = {"id": identifier, "arm": arm,
                           "question_id": question["id"], "question": question["question"],
                           "model": args.model, "status": "failed",
                           "error": f"{type(exc).__name__}: {exc}",
                           "finished_utc": datetime.now(timezone.utc).isoformat()}
            save(path, attempt)
            print(attempt["status"], identifier,
                  "steps", len(attempt.get("steps", [])), flush=True)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
