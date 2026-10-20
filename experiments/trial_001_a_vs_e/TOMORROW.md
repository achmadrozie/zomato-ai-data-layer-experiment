# Experiment handoff

Project 1 repository: `zomato-dbt-layer-refactor`; Snowflake database: `ZOMATO_DLR`. The experiment work is on branch `codex/experiment-a-e-trial` and draft PR #7. Project 0 is separate.

## Read first

1. [`docs/experiment_design.md`](../../docs/experiment_design.md) — six cumulative arms and output-first scoring.
2. [`README.md`](README.md) — implemented A/E pilot, commands, and limitations.
3. [`questions.md`](questions.md) and [`questions_q06_q25.md`](questions_q06_q25.md) — public question bank; the JSON files contain the exact prompts.
4. Local, author-only `questions_and_answers_25.local.md` — all 25 prompts and reference answers. This file and the gold SQL are ignored by Git and must remain outside evaluated agents' access.
5. [`context/v1/business_glossary.md`](../../context/v1/business_glossary.md) — F-arm reporting policies; Q22–Q24 depend on context.

## Current result and boundary

- The exploratory 5-question A/E pilot produced locally checked query outputs: A 2/5, E 5/5. Its model selected SQL or MetricFlow plans; it did **not** receive query results or write final answers. A vs E adds intermediate, core, marts, and semantic access together, so this result does not isolate any one layer's uplift.
- `generate_plans.py` and `evaluate_plans.py` implement only that five-question A/E plan pilot. `run_gold_additional.py` verifies reference queries for Q06–Q25; it is not an agent experiment runner. Do not present a 25-question or six-arm result until those runs exist.
- The full-answer path needs a reviewed way to expose Snowflake results to the evaluated model. Automatic approval review previously rejected a runner that sent private Snowflake-derived results to an external model. Do not bypass that decision; obtain appropriate authorization or use an approved local route.
- Primary future score: final answer values/tables, scope, units, and interpretation. Different valid SQL may pass. Keep query traces for diagnosis and access checks. Freeze model/settings, snapshot, prompt, and evaluator before arm comparisons.

## Suggested prompt for a fresh chat

> Continue Project 1 in this repository from `experiments/trial_001_a_vs_e/TOMORROW.md`. Review the design, public questions, local author-only reference, and existing A/E pilot. Start with a small five-question A/E **full-answer** experiment, scoring the final answers against the local reference. Keep gold answers outside agent access, preserve the same settings across arms, and report query-output correctness separately from final-answer correctness. Address the prior approval block before sending Snowflake results to an external model. Show per-question results and limitations. Then propose the next run toward the six-arm, 25-question ladder; do not claim uplift for layers that have not been separately tested.
