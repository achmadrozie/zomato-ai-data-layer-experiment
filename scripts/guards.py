"""SQL guardrails for the experiment runner: arm allowlists and query validation."""

from __future__ import annotations

import time

import sqlglot
from sqlglot import exp


SCHEMAS = {
    "A": ("SOURCES", "STAGING"),
    "B": ("SOURCES", "STAGING", "INTERMEDIATE"),
    "C": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE"),
    "D": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
    "E": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
    "F": ("SOURCES", "STAGING", "INTERMEDIATE", "CORE", "MARTS"),
}
SENSITIVE_COLUMNS = {"PASSWORD", "EMAIL", "NAME", "CUSTOMER_NAME", "COMMENT",
                     "LIC_NO", "LICENSE_NO"}
SENSITIVE_RESULT_COLUMNS = {"USER_ID", "CUSTOMER_ID", "ORDER_ID", "ORDER_ITEM_ID",
                            "REVIEW_ID", "EMAIL", "NAME", "CUSTOMER_NAME", "COMMENT"}

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
