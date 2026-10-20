# Zomato dbt layer refactor

Project 1 compares how access to successive data layers affects AI answer correctness and consistency. This repository is separate from Project 0, which remains in [`zomato-ai-analytics-pipeline`](https://github.com/achmadrozie/zomato-ai-analytics-pipeline).

## Scope

- Target Snowflake database: `ZOMATO_DLR`.
- Refactor path: source → staging → intermediate → core → marts; semantic models and metrics branch from core. A context layer can be added for the experiment.
- The initial import of `aws/`, `snowflake/`, and `dbt_zomato/` matched the Git-tracked files in Project 0 at commit `74198bd1a3fd29ebf7dc39c067b8af15d64ccde0`. Project 1 configuration changes are tracked in this repository.

## Project 1 setup

The original scripts in `snowflake/01_setup.sql` through `05_copy_into.sql` are retained as the Project 0 baseline. [`snowflake/project1/01_initialize.sql`](snowflake/project1/01_initialize.sql) creates `ZOMATO_DLR`, clones six `ZOMATO.SOURCES` tables, and copies `USERS` without its `PASSWORD` column. It also creates the dbt schemas and `DBT_LAYER_REFACTOR_ROLE`, then grants that role to the Snowflake user executing the script. Re-running it preserves the first snapshot; it does not refresh existing tables.

**Initialized on 20 October 2026:** the six project schemas and seven source tables exist in `ZOMATO_DLR`. Row counts matched their Project 0 sources at initialization, `SOURCES.USERS` has no `PASSWORD` column, and `dbt debug` passed using `DBT_LAYER_REFACTOR_ROLE`.

**Current refactor checkpoint:** seven staging and six intermediate views plus six core tables have been built in `ZOMATO_DLR`. The source audit and intermediate examples are in [the staging and intermediate review](docs/staging_intermediate_review.md). Core grains, relationships, validation, and examples are in [the core review](docs/core_review.md). All six cores now have semantic definitions, with 19 metrics and four simple aggregate marts described in [the semantic and marts review](docs/semantic_marts_review.md).

The next checkpoint is the [context-layer candidate](context/README.md) and [experiment-design review draft](docs/experiment_design.md). Context is implemented as a versioned Markdown glossary. Benchmark questions and gold answers follow the design review.

Each SQL-based dbt model lives in its own folder with matching `.sql`, `.md`, and `.yml` files. The SQL defines the transformation, Markdown explains its grain and purpose, and YAML holds its dbt description and tests. Metric declarations have no SQL model and remain YAML plus Markdown configuration files. Semantic declarations for SQL-based core models live in the corresponding model YAML.

Set `DBT_SNOWFLAKE_ACCOUNT`, `DBT_SNOWFLAKE_USER`, and `DBT_ENV_SECRET_SNOWFLAKE_PASSWORD` in your shell. Copy [`dbt_zomato/profiles.yml.example`](dbt_zomato/profiles.yml.example) to a private profiles directory such as `.local/dbt/profiles.yml`, then run dbt with `--profiles-dir .local/dbt --project-dir dbt_zomato`. The Project 1 profile and run guard require `ZOMATO_DLR`, so the existing Project 0 profile cannot accidentally direct this project to `ZOMATO`.

The copied AI enrichment mart and its source declaration are archived in [`archive/project0/`](archive/project0/README.md). Current mart grains and additive components are documented in [the mart contract review](docs/mart_contract_review.md). `snowflake/project1/02_retire_legacy_marts.sql` preserves superseded Project 1 mart tables in `SNAPSHOTS` after their replacements pass validation.

Local credentials, ignored policy files, dbt logs, generated targets, and installed packages are not part of this repository.
