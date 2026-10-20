# Project 1 experiment design — review draft

Status: CTX-01–03 accepted for the first trial; experiment design remains a review draft.

## Research question

How does access to curated data layers, semantic metrics, and business context affect AI answer correctness and consistency on the same frozen data?

Correctness and repeatability are primary; latency, tool use, and cost are secondary. Results describe this dataset and configuration.

The benchmark author can inspect all layers to create questions, reference SQL, and expected answers. Evaluated agents receive only their assigned arm's access. Gold SQL/results are kept outside agent access.

## Treatments

Each arm keeps the access of the previous arm and adds one layer. Run the same questions with the same model and settings in every arm. A includes source and staging as the starting point; their separate effects are outside this ladder.

| Arm | SQL access in `ZOMATO_DLR` | Additional access | Adjacent comparison |
| --- | --- | --- | --- |
| A — source + staging | Seven `SOURCES` tables and seven staging views | Schema discovery | Baseline |
| B — intermediate | A + intermediate views | Same discovery | B − A: intermediate |
| C — core | B + core facts and dimensions | Same discovery | C − B: core |
| D — marts | C + four additive marts | Same discovery | D − C: marts |
| E — semantic | Same SQL access as D | MetricFlow discovery/queries for 19 metrics | E − D: semantic metrics |
| F — context | Same SQL and semantic access as E | Business context document | F − E: context |

Semantic declarations share each core/dimension model's YAML file. They describe the core tables for MetricFlow; they do not create another SQL layer. A–D cannot read those files or call the semantic tools. E and F can still query marts through SQL; MetricFlow metrics use the defined core models. Record which objects and tools each answer actually used.

## Context contract

- Only F receives [`business_glossary.md`](../context/v1/business_glossary.md), pinned by version/hash.
- Context supplies reporting defaults, scope rules, and interpretation; metric formulas stay in semantic metadata.
- CTX-01–03 were accepted for the first trial; review any later policy changes before using them in a comparison.
- A–E cannot read the context or review reports. E/F receive identical semantic metadata.
- Questions can draw on the approved policies. Questions and gold answers stay outside the context payload.
- Policy-required questions are reported separately: A–E can correctly ask for a missing rule; F is expected to apply the supplied rule. This distinguishes added business information from data-querying ability.

## Access enforcement

- Dedicated read-only identities enforce explicit object allowlists; agents do not use the dbt build role.
- SQL tools reject writes, role changes, and unlisted objects. E/F metric tools expose discovery and queries only.
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

- First trial: **5 questions × 1 arm (F) × 1 run = 5 answers**. F has all layers and the reviewed business context. This checks whether the full path works and produces inspectable answers; it cannot measure layer uplift.
- For each trial question, write the expected answer and a SQL query used to check it before running the agent. Keep both out of the agent's view. Review the five answers, queries, and errors manually.
- Next, complete the same five questions across all six arms: **5 × 6 × 1 = 30 answers**. The five F answers from the first trial count if the questions, snapshot, model, and settings remain fixed; otherwise rerun F. Compare each arm with its immediate predecessor. With five questions, one changed answer moves the accuracy score by 20 percentage points, so this is an illustrative ladder rather than a stable uplift estimate.
- More questions and repetitions can follow after reviewing those 30 answers. Keep the questions, model, settings, and snapshot fixed across arms.
- Cover joins/aggregation, metric interpretation, order/item grain, approved context policies, and insufficient-data cases. Tag mart coverage and policy dependence.
- Author and review gold SQL/results on the frozen snapshot. Each item specifies population, date/currency scope, expected output, numeric tolerance, and valid clarification/abstention behavior by arm.
- In the first trial, report correctness, appropriate clarification/abstention, query errors, and latency for each question. For a later repeated comparison, also report consistency across runs and cost.
- Keep failed attempts and infrastructure retries visible. Treat findings as an exploratory case study.

## First trial preparation

1. Use the reviewed CTX-01–03 policies. Pick five questions with explicit date range, currency, and order population. The `_utc` labels do not establish timezone conversion.
2. Record the snapshot, context version, model, and settings used for these five answers. Keep the expected answers separate from the agent.

## Next steps

1. Use the accepted context policies and arm F for the first trial; choose one model and record its settings.
2. Prepare read-only access for F and save its queries and answers. Add the A–E access boundaries for the six-arm ladder.
3. Write five questions with their expected answers and checking SQL, then run each once with F. Review the results together.
4. Complete A–F on those five questions, compare adjacent arms, and inspect which layers the agent used. Decide whether to add questions and repetitions.
