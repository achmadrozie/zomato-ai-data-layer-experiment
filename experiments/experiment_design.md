# 25-question data-layer experiment

## Question and scope

How does adding curated SQL layers, semantic metrics, and business context change AI answer correctness on the same `ZOMATO_DLR` snapshot? This is an exploratory case study on one dataset and two models. The exact [25 questions](./questions_25.json) are frozen before the A–F run. Q26 from the former trial is excluded.

The author reference is [answers_25.md](./answers_25.md), supported by an ignored local SQL check file, `gold_25.local.sql`. The evaluated model receives neither the reference nor the SQL check file; the runner has no file-read tool. The answers use recorded `order_date` and the Project 1 snapshot initialized on 20 October 2026.

## Treatments

Every arm retains the previous arm's SQL access. The same question, model, tool budget, result limit, and answer rubric apply to all arms.

| Arm | Accessible SQL objects | Additional grounding |
| --- | --- | --- |
| A | Seven source tables and seven staging views | None |
| B | A plus six intermediate views | None |
| C | B plus six core facts and dimensions | None |
| D | C plus four aggregate marts | None |
| E | Same SQL access as D | 19 MetricFlow metrics and their dbt descriptions; metric queries |
| F | Same SQL and metric access as E | Pinned `context/v1/business_glossary.md` |

The MetricFlow time spine is backend support, not an agent-visible staging object. Mart names ending `_utc` do not establish a timezone conversion. The context policies CTX-01–03 are experiment rules for this snapshot, not claims about Zomato's real policies. Only F receives them.

## Run protocol

- Two models: `gpt-4.1` (temperature 0) and `gpt-6-luna` (reasoning effort high). Each model has three repetitions of 25 questions in six arms: **450 attempts per model, 900 total**. Job order is shuffled with seed `20261021`.
- Each attempt can make up to three read-only queries. The agent may use SQL in its arm's allowlist; E/F may also use MetricFlow. It can answer or request a missing rule. No question, gold answer, report, or prior attempt is fed into another attempt.
- The runner stores every action, tool result or error, final answer, model usage, and timing in the committed `experiments/run.local/af_25_v2_rep{1,2,3}/` and `af_25_luna_rep{1,2,3}/` directories. A completed attempt is not rerun on resume.
- The model has no direct database credentials or filesystem tools. The runner validates a single SELECT and an explicit table allowlist before SQL execution, blocks sensitive columns and row-level identifiers in outputs, and limits result rows. The warehouse connection currently uses the Project 1 dbt role behind this runner; dedicated read-only warehouse identities are not yet provisioned.
- MetricFlow queries use the same frozen dbt semantic project. SQL access remains available in E/F, so the comparison measures **optional semantic access**, including whether the model chooses to use it.
- E/F receive the available metric definitions plus example MetricFlow group-by names. A tool error returns its actual query-resolution message, so the model can revise an invalid group-by name within the same three-query budget.

## Scoring

The primary unit is the **final user-facing answer**, graded by `scripts/autograde.py` against `experiments/gold_25_results.json` with identical rules for every attempt and model. For each data-answerable Q01–Q21 and Q25, all requested values, ranking, scope, units, and interpretation must match the frozen author reference within its stated tolerance. Equivalent SQL is acceptable. An execution error, unsupported claim, or unrequested change in population is incorrect; record the reason separately. Report per-question outcomes and arm totals with denominators, plus query/metric use and failures.

Scoring uses ±0.01 percentage point for percentages, ±0.01 in stated units for averages/correlation, exact integer counts and identities, and the stated money/decomposition tolerances. The [reference answers](./answers_25.md), [results](RESULTS.md), and the [experiment README](./README.md) (which lists the corrections to the first manual grading) record the scores.

Q22–Q24 require policies supplied only to F. Score these separately: a justified request for the missing rule is an appropriate A–E outcome, while F is expected to apply the policy and answer. Do not count A–E clarification as a numeric success or silently remove it from the denominator. Distinguish appropriate clarification, wrong numeric answer, and tool failure.

Three repetitions per model permit descriptive repeatability estimates. This single-dataset experiment does not establish broad statistical generality. The initial five-question pilots and their old scripts are excluded from this run and its score.
