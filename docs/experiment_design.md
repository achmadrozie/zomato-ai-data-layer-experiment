# Project 1 experiment design — review draft

Status: context policies and run settings are under review. Benchmark authoring follows this review.

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

B currently tests staging/intermediate/core together. Separate effects would need more arms. A marts + semantics combination is also outside this five-arm design.

## Context contract

- Only E receives [`business_glossary.md`](../context/v1/business_glossary.md), pinned by version/hash.
- Context supplies reporting defaults, scope rules, and interpretation; metric formulas stay in semantic metadata.
- The proposed CTX-01–03 policies need business review before they become benchmark requirements.
- A–D cannot read the context or review reports. D/E receive identical semantic metadata.
- Questions can draw on the approved policies. Questions and gold answers stay outside the context payload.
- Policy-required questions are reported separately: A–D can correctly ask for a missing rule; E is expected to apply the supplied rule. This distinguishes added business information from data-querying ability.

## Access enforcement

- Dedicated read-only identities enforce explicit object allowlists; agents do not use the dbt build role.
- SQL tools reject writes, role changes, and unlisted objects. D/E metric tools expose discovery and queries only.
- Project 0, archives, credentials, repository files, and gold answers are unavailable to evaluated agents. The time spine is semantic backend support.

## Shared run conditions

- Same exact model/version, prompt, answer format, and inference settings.
- Same frozen snapshot, session settings, budgets, and retry policy.
- Fresh conversation/session for every repetition; no previous answers or evaluator feedback.
- Randomized question/arm order with a recorded scheduling seed.
- Record total latency, query time, retries, tool calls, tokens, and model cost.
- Keep warehouse/cache settings consistent where possible; label estimated warehouse costs.

Proposed defaults: 20 tool calls per answer, 60-second query timeout, 1,000-row cap, and one infrastructure retry per failed call within the budget. Model and inference settings still need selection.

## Evaluation plan

- Pilot two questions to check tools/logging; exclude them from the main benchmark.
- Main run: 25 fixed questions × 5 arms × 3 repetitions = **375 runs**.
- Cover joins/aggregation, metric interpretation, order/item grain, approved context policies, and insufficient-data cases. Tag mart coverage and policy dependence.
- Author and review gold SQL/results on the frozen snapshot. Each item specifies population, date/currency scope, expected output, numeric tolerance, and valid clarification/abstention behavior by arm.
- Score correctness, correct in all three repetitions, appropriate clarification/abstention, and query errors. Compare paired results on the same questions; report latency/cost alongside them.
- Keep failed attempts and infrastructure retries visible. Treat findings as an exploratory case study.

## Before benchmark authoring

1. **Agree on business context:** review CTX-01–03, then approve or replace them.
2. **Check dates and currency:** inspect missing/inconsistent dates and available currencies so each question has a clear scope. The `_utc` rename does not establish timezone conversion.
3. **Define populations:** distinguish all orders, Delivered orders, and orders containing a selected food when writing gold SQL.
4. **Check exposed metadata:** confirm each arm receives its intended information; overlapping context/semantic descriptions are acceptable and documented.
5. **Freeze the setup:** record snapshot identity/checks, context/semantic versions, model/settings, and tool limits.

The [additive-mart correction](mart_contract_review.md) is complete. All four marts expose additive components, and 25 data tests passed. The fine-grained restaurant mart offers limited compression; its performance benefit is measured rather than assumed.

## Next steps

1. Review the context policies and design; decide whether B needs separate layer arms and select the model/settings.
2. Check remaining data assumptions and implement the controlled tools/access/logging.
3. Run the excluded pilot, then author/review and freeze the main questions and gold answers.
4. Execute the 375 runs and report results.
