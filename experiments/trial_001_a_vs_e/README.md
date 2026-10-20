# Trial 001: A vs E

Five fixed questions compare **A (source + staging)** with **E (A + intermediate, core, marts, and semantic metrics)**. Both use `gpt-6.1-sol`, low reasoning effort, and one plan per question. This is a small illustrative comparison; it cannot isolate semantic uplift from the three other layers added between A and E.

`questions.json` defines the exact prompts; [`questions.md`](questions.md) lists them for review. The ignored `reference.local.md` records answers, definitions, and tolerances, backed by `gold.local.sql`. Prepare both local files before grading. `generate_plans.py` sends the questions and selected schema/metric metadata from the committed repository to the model. It does not open Snowflake credentials, request warehouse data, or permit model tool calls. `evaluate_plans.py` executes those stored plans against the Project 1 snapshot and grades scalar results locally. Generated `plans.json`, `results.local.json`, and `report.local.md` stay outside Git.

The model selects one SQL query, one MetricFlow metric with an optional currency grouping, or a clarification. The local evaluator checks SQL table references against each arm's allowlist and accepts one scalar result. MetricFlow receives the 2025 window; monetary metric queries can group by `order_id__currency` and select INR. The evaluator uses the Snowflake build role for this prototype, so the SQL allowlist is a harness check rather than a database-enforced role boundary.

Gold numeric tolerances are zero for order count, 0.01 INR for GMV, and 0.0001 for the remaining quantities. Clarification is recorded separately from numeric correctness. The first E plan pass exposed an incomplete MetricFlow tool description for currency filtering; it was corrected and E was rerun before grading. A remained on its first pass. A later formal comparison should freeze that interface and rerun both arms.

The full answer-generation loop was not run: automatic approval review rejected sending Snowflake-derived query results to the external model. This trial measures generated query/metric choice and its local numeric outcome; it does not measure the final wording of agent answers. Results are in ignored local files for the workspace owner.

Run with a Python environment containing `snowflake-connector-python`, `sqlglot`, and `PyYAML`, plus authenticated Codex CLI and MetricFlow. Set `CODEX_CLI_PATH` and `MF_BIN` if the binaries are not on `PATH`; the Project 1 dbt profile must be available locally. From the repo root:

```bash
python experiments/trial_001_a_vs_e/generate_plans.py
python experiments/trial_001_a_vs_e/evaluate_plans.py
```
