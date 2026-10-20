"""Load only the Project 1 Snowflake target; fail closed on missing credentials."""

from __future__ import annotations

import os
from pathlib import Path

import yaml


EXPECTED = {
    "database": "ZOMATO_DLR",
    "role": "DBT_LAYER_REFACTOR_ROLE",
    "warehouse": "ZOMATO_WH",
}


def profile() -> dict:
    profile_dir = Path(os.environ.get("DBT_PROFILES_DIR", "/tmp/zomato-dlr-dbt-profile"))
    path = profile_dir / "profiles.yml"
    settings = yaml.safe_load(path.read_text())["zomato_dbt_layer_refactor"]["outputs"]["dev"]
    for key, expected in EXPECTED.items():
        if settings.get(key) != expected:
            raise ValueError(f"Refusing non-Project-1 Snowflake target: {key}")
    credentials = {
        "account": os.environ.get("DBT_SNOWFLAKE_ACCOUNT"),
        "user": os.environ.get("DBT_SNOWFLAKE_USER"),
        "password": os.environ.get("DBT_ENV_SECRET_SNOWFLAKE_PASSWORD"),
    }
    missing = [key for key, value in credentials.items() if not value]
    if missing:
        raise EnvironmentError(f"Missing Project 1 credential environment variables: {', '.join(missing)}")
    return {**settings, **credentials}
