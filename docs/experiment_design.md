# Project 1 experiment design — review draft

Status: CTX-01–03 accepted for the first trial; experiment design remains a review draft.

## Research question

How does access to curated data layers, semantic metrics, and business context affect AI answer correctness and consistency on the same frozen data?

Correctness and repeatability are primary; latency, tool use, and cost are secondary. Results describe this dataset and configuration.

The benchmark author can inspect all layers to create questions, reference SQL, and expected answers. Evaluated agents receive only their assigned arm's access. Gold SQL/results are kept outside agent access.

## Treatments

B is the curated base; marts and semantics are parallel additions.

| Arm | SQL access in `ZOMATO_DLR` | Additional access | Comparison |
| --- | --- | --- | --- |
| A — source | Seven `SOURCES` tables | Schema discovery | Baseline |
| B — curated base | A + staging, intermediate, core | Same discovery | B vs A |
| C — marts | B + four additive marts | Same discovery | C vs B |
| D — semantic | B | MetricFlow discovery/queries for 19 metrics | D vs B |
| E — semantic + context | Same as D | Same semantic tools + business context | E vs D |

Semantic declarations share each core/dimension model's YAML file. They describe the core tables for MetricFlow; they do not create another SQL layer. A–C cannot read those files or call the semantic tools.

B includes staging, intermediate, and core together. The five-arm comparison can be revisited after the first trial.

## Context contract

- Only E receives [`business_glossary.md`](../context/v1/business_glossary.md), pinned by version/hash.
- Context supplies reporting defaults, scope rules, and interpretation; metric formulas stay in semantic metadata.
- CTX-01–03 were accepted for the first trial; review any later policy changes before using them in a comparison.
- A–D cannot read the context or review reports. D/E receive identical semantic metadata.
- Questions can draw on the approved policies. Questions and gold answers stay outside the context payload.
- Policy-required questions are reported separately: A–D can correctly ask for a missing rule; E is expected to apply the supplied rule. This distinguishes added business information from data-querying ability.

## Access enforcement

- Dedicated read-only identities enforce explicit object allowlists; agents do not use the dbt build role.
- SQL tools reject writes, role changes, and unlisted objects. D/E metric tools expose discovery and queries only.
- Project 0, archives, credentials, repository files, and gold answers are unavailable to evaluated agents. The time spine is semantic backend support.

## Shared run conditions for later arm comparisons

- Same exact model/version, prompt, answer format, and inference settings.
- Same frozen snapshot, session settings, budgets, and retry policy.
- Fresh conversation/session for every repetition; no previous answers or evaluator feedback.
- Randomized question/arm order with a recorded scheduling seed.
- Record total latency, query time, retries, tool calls, tokens, and model cost.
- Keep warehouse/cache settings consistent where possible; label estimated warehouse costs.

For the first trial, record the model and settings used. Keep them fixed when comparing arms later.

## Evaluation plan

- First trial: **5 questions × 1 arm (E) × 1 run = 5 answers**. E has core data, semantic metrics, and the reviewed business context. This checks whether the full path works and produces inspectable answers; it cannot measure the effect of adding each layer.
- For each trial question, write the expected answer and a SQL query used to check it before running the agent. Keep both out of the agent's view. Review the five answers, queries, and errors manually.
- A larger five-arm comparison is a later decision. Its earlier 25-question × 5-arm × 3-run size is a possible expansion, not a commitment.
- Cover joins/aggregation, metric interpretation, order/item grain, approved context policies, and insufficient-data cases. Tag mart coverage and policy dependence.
- Author and review gold SQL/results on the frozen snapshot. Each item specifies population, date/currency scope, expected output, numeric tolerance, and valid clarification/abstention behavior by arm.
- In the first trial, report correctness, appropriate clarification/abstention, query errors, and latency for each question. For a later repeated comparison, also report consistency across runs and cost.
- Keep failed attempts and infrastructure retries visible. Treat findings as an exploratory case study.

## First trial preparation

1. Use the reviewed CTX-01–03 policies. Pick five questions with explicit date range, currency, and order population. The `_utc` labels do not establish timezone conversion.
2. Record the snapshot, context version, model, and settings used for these five answers. Keep the expected answers separate from the agent.

## Next steps

1. Use the accepted context policies and arm E for the first trial; choose one model and record its settings.
2. Prepare one read-only path for arm E and save its queries and answers. Extra arm-specific access can wait until an arm comparison.
3. Write five questions with their expected answers and checking SQL, then run each question once with arm E. Review the results together.
4. Decide from those five results whether to revise the questions or expand to multiple arms and repetitions.
