# Zomato dbt layer refactor

Project 1 compares how access to successive data layers affects AI answer correctness and consistency. This repository is separate from Project 0, which remains in [`zomato-ai-analytics-pipeline`](https://github.com/achmadrozie/zomato-ai-analytics-pipeline).

## Scope

- Target Snowflake database: `ZOMATO_LAYER_REFACTOR`.
- Refactor path: source → staging → intermediate → core → marts; semantic models and metrics branch from core. A context layer can be added for the experiment.
- The initial contents of `aws/`, `snowflake/`, and `dbt_zomato/` are an unchanged, Git-tracked baseline copied from Project 0 at commit `74198bd1a3fd29ebf7dc39c067b8af15d64ccde0`.

## Baseline status

The copied SQL and dbt source definitions still refer to the Project 0 database `ZOMATO`. They have not yet been adapted to `ZOMATO_LAYER_REFACTOR`, and no Snowflake objects have been created by this repository setup. Review and update the database and source settings before running any setup SQL or dbt build for Project 1.

Local credentials, ignored policy files, dbt logs, generated targets, and installed packages are not part of this baseline.
