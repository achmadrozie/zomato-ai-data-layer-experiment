# Zomato dbt layer refactor

Project 1 compares how access to successive data layers affects AI answer correctness and consistency. This repository is separate from Project 0, which remains in [`zomato-ai-analytics-pipeline`](https://github.com/achmadrozie/zomato-ai-analytics-pipeline).

## Scope

- Target Snowflake database: `ZOMATO_DLR`.
- Refactor path: source → staging → intermediate → core → marts; semantic models and metrics branch from core. A context layer can be added for the experiment.
- The initial import of `aws/`, `snowflake/`, and `dbt_zomato/` matched the Git-tracked files in Project 0 at commit `74198bd1a3fd29ebf7dc39c067b8af15d64ccde0`. Project 1 configuration changes are tracked in this repository.

## Project 1 setup

The original scripts in `snowflake/01_setup.sql` through `05_copy_into.sql` are retained as the Project 0 baseline. [`snowflake/project1/01_initialize.sql`](snowflake/project1/01_initialize.sql) creates `ZOMATO_DLR`, clones six `ZOMATO.SOURCES` tables, and copies `USERS` without its `PASSWORD` column. It also creates the dbt schemas and `DBT_LAYER_REFACTOR_ROLE`, then grants that role to the Snowflake user executing the script. Re-running it preserves the first snapshot; it does not refresh existing tables.

**Initialized on 20 October 2026:** the six project schemas and seven source tables exist in `ZOMATO_DLR`. Row counts matched their Project 0 sources at initialization, `SOURCES.USERS` has no `PASSWORD` column, and `dbt debug` passed using `DBT_LAYER_REFACTOR_ROLE`.

**Current refactor checkpoint:** seven staging and six intermediate views have been built in `ZOMATO_DLR`. The source audit, layer contracts, validation results, and example output are in [the staging and intermediate review](docs/staging_intermediate_review.md). Core, marts, and semantic models have not been rebuilt as part of this checkpoint.

Each SQL-based dbt model lives in its own folder with matching `.sql`, `.md`, and `.yml` files. The SQL defines the transformation, Markdown explains its grain and purpose, and YAML holds its dbt description and tests. Source and semantic declarations that have no SQL model remain YAML configuration files.

Set `DBT_SNOWFLAKE_ACCOUNT`, `DBT_SNOWFLAKE_USER`, and `DBT_ENV_SECRET_SNOWFLAKE_PASSWORD` in your shell. Copy [`dbt_zomato/profiles.yml.example`](dbt_zomato/profiles.yml.example) to a private profiles directory such as `.local/dbt/profiles.yml`, then run dbt with `--profiles-dir .local/dbt --project-dir dbt_zomato`. The Project 1 profile and run guard require `ZOMATO_DLR`, so the existing Project 0 profile cannot accidentally direct this project to `ZOMATO`.

The copied AI enrichment mart is disabled because its source table belongs to Project 0. No Snowflake objects are created by committing this setup code.

Local credentials, ignored policy files, dbt logs, generated targets, and installed packages are not part of this repository.
