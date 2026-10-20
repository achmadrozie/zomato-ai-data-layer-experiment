# Project 1 experiment design — review draft

Status: proposed design for review. The context candidate exists; benchmark questions, gold SQL/results, access roles, and agent runs are subsequent work.

## Research question

How does access to curated data layers, semantic metrics, and business context affect an AI agent's ability to produce correct, repeatable, verifiable answers from the same frozen data?

The experiment evaluates this repository and snapshot. It does not assume that a question answerable from a derived layer is impossible to answer from the source. Accuracy and repeatability are the primary outcomes; latency, tool use, and cost explain the practical tradeoffs.

This draft follows the [original shared brief review](https://chatgpt.com/s/cx_6ad72cc177c881919464ea99067cdf73) and the implemented checkpoint in this repository. It is a proposal, not a record of an executed experiment.

## Treatments

B is the curated base. Marts and semantic metrics are parallel additions to B.

| Arm | Agent SQL access in `ZOMATO_DLR` | Other available information/tools | Comparison |
| --- | --- | --- | --- |
| A — source | Seven snapshotted tables in `SOURCES` | Relation discovery and column names/types | Baseline |
| B — curated base | A plus the seven staging views, six intermediate views, and six core tables | Same SQL discovery interface | B vs A: combined curation effect |
| C — marts | B plus the four active aggregate marts | Same SQL discovery interface | C vs B: aggregate-mart effect |
| D — semantic | B | Metric discovery, supported dimensions, and MetricFlow queries for the 19 metrics | D vs B: semantic-interface effect |
| E — semantic + context | Same as D | Same semantic tools plus the exact glossary payload | E vs D: consolidated-context effect |

All allowlists use explicit objects. The archived AI review mart, Project 0 database, snapshots schema, and unlisted objects are excluded. The MetricFlow time spine is backend support, not a new business dataset exposed through the SQL discovery tool.

This five-arm design measures staging, intermediate, and core together in B. It cannot attribute their individual effects. If that is required, additional arms must be defined before the benchmark is frozen. A separate B + marts + semantic arm could later measure the combination; the first five arms do not establish that effect.

## Context contract

The sole E payload is `context/v1/business_glossary.md`, identified by version and SHA-256 in its manifest. It supplies business definitions, units, grains, and limits. It contains no execution instructions, tool-selection policy, worked SQL, question-specific values, benchmark items, or gold answers.

A through D do not receive that file or the repository review reports. Ordinary SQL discovery returns relation and column names/types using the same format in each arm. D and E receive the same semantic metric definitions and supported-dimension discovery. Since those definitions can overlap the glossary, E versus D measures the incremental value of the consolidated context rather than all business knowledge versus none.

The agent receives its treatment through a controlled interface, not unrestricted repository access. The context file, model metadata, tool descriptions, and exposed object lists are frozen and hashed with each run configuration. Any discovered metadata leakage is corrected before the benchmark is frozen.

## Access enforcement

The existing `DBT_LAYER_REFACTOR_ROLE` is a build role and is unsuitable for agent runs. The next implementation stage needs dedicated read-only experiment identities and sessions with explicit object grants per arm. A prompt-only allowlist does not enforce access.

The SQL service fixes the database, role, session settings, result limits, and timeout. It accepts read-only queries and rejects role changes, writes, multiple statements, and attempts to reach unlisted objects. Dedicated identities cannot inherit a broader build/admin role or switch to it. Permission-denial probes must cover forbidden schemas, Project 0, writes, and role switching before any agent run.

The D/E metric service uses the same frozen semantic manifest and a backend identity limited to core models and the time spine. Its public methods are discovery and metric queries; they do not expose a shell, profile credentials, general filesystem access, or a way to invoke arbitrary dbt commands. The semantic and SQL tools log provenance in the same run record.

No roles or agent credentials are provisioned by this documentation change.

## Shared run conditions

- One exact model/version, one system prompt, one answer format, and the same inference settings across arms. A seed is recorded if supported; it does not guarantee deterministic output.
- The same frozen snapshot, date interpretation, monetary policy, query timeout, row cap, agent tool-call budget, and retry policy across arms. The available data/tools differ only as specified by the treatment.
- Each repetition has a fresh conversation and session. Prior runs, errors from other arms, gold answers, and evaluator feedback are unavailable to the agent.
- Arm and question order are randomized with a recorded seed. The schedule balances arms across time to reduce connection and warehouse-state effects.
- The primary latency measure is wall time from the agent request to the final answer, including discovery and retries. Query duration and connection time are also recorded separately.
- Cache/warehouse settings are held constant where controllable and recorded. Uncontrolled cache state limits query-cost and latency conclusions.
- Model input/output tokens and tool-call counts are recorded. Model cost uses the run's recorded pricing/version. Warehouse credits require a separately documented attribution method; estimated credits are labeled as estimates.

Proposed pilot defaults for review are 20 tool calls per answer, a 60-second query timeout, and a 1,000-row result cap. At most one infrastructure retry per failed tool call is allowed within the same budget. Infrastructure failures are distinguished from invalid SQL and unsupported semantic requests. The exact model and inference settings remain unselected; they must be recorded before the pilot.

## Evaluation plan after design review

A two-question pilot establishes tool behavior and logging. Pilot questions are excluded from the final benchmark. The proposed main run is 25 prespecified questions × 5 arms × 3 independent repetitions = 375 agent runs.

Question strata cover source-answerable joins and aggregation, metric definitions and denominator choice, order/item grain, time and geography, and evidence-insufficient requests. Mart-covered and mart-uncovered questions are tagged before execution so aggregate-mart results can be interpreted by coverage. Multi-currency and food-specific population questions receive explicit reference semantics during gold authoring.

Gold answers come from separately reviewed reference SQL on the frozen snapshot. Every benchmark item records its expected response type, population, grain, date field, currency treatment, expected columns, ordering/tie rules, numeric tolerances, and whether an evidence-based abstention is required. Gold SQL and values remain outside the context payload and agent workspace.

Primary reports are per-question correctness and the proportion of questions correct in all three repetitions, with paired arm differences on the same items. Secondary reports include abstention quality, SQL/semantic query errors, latency, tool calls, tokens, and cost. Numeric comparison uses the prespecified tolerances; narrative claims need support from tool evidence. Unsupported claims and failure to answer an answerable question are scored separately. A repeatable wrong answer is not correct.

Question-level results and sample size accompany averages. With 25 questions, conclusions are an exploratory case study for this dataset and configuration. Infrastructure retry/failure counts remain visible in reports; attempts are not silently rerun until correct.

## Prerequisites before freezing questions and gold answers

| Finding in the current implementation | Consequence | Proposed resolution |
| --- | --- | --- |
| `order_date` and timestamp are parsed from separate source fields | Date filtering and hourly bucketing may use different source values | Audit equality and nulls; state the chosen date field for each benchmark item without inventing a timezone |
| Item fact has no currency column; the corrected item mart obtains parent-order currency | Item semantic monetary metrics still need an explicit currency scope through the order relationship | Audit source currencies and require currency-specific gold/query scopes for monetary items |
| Cross-fact ratios have an all-order denominator | A food filter does not automatically define the intended order population | Specify shared dimensions and eligible population per item; use explicit distinct-order definitions where the question requires them |
| Core/model docs and semantic metadata already contain some business definitions | Uncontrolled exposure could confound the E context treatment | Freeze and inspect the exact metadata returned by each tool before the pilot |
| Snapshot identity is presently described by initialization date and counts | Counts alone do not detect all changes before a rerun | Record source object identities/schema metadata and a suitable content-verification strategy with the run manifest |

The additive-mart prerequisite is resolved in the [mart contract correction](mart_contract_review.md): every active mart has explicit dimensions and a day/hour bucket, duration/rating averages have sum/count components, and item amounts are grouped by parent-order currency. All four replacement tables built in Snowflake and all 25 selected data tests passed. The glossary and payload hash have been refreshed accordingly. Mart names/time columns use the requested `_utc` naming convention, with existing values preserved; no UTC conversion or verification has occurred. The restaurant daily grain has 9,243,921 rows versus 10 million orders, so it provides limited compression; performance benefit remains an experimental question.

## Delivery sequence and review points

1. Context candidate: glossary, payload manifest, and source-definition review. This change implements that step.
2. Design review: settle whether the bundled B arm is sufficient, select the model/settings and budgets, and approve the treatment/metadata boundaries. This document is the review artifact.
3. Prerequisites and harness: audit date/currency assumptions, provision access, implement controlled SQL/MetricFlow tools, and establish provenance logging. The additive-mart correction is complete.
4. Pilot, then benchmark authoring: verify the interfaces with excluded pilot items; write/review the 25 main items and gold results, then freeze all artifacts.
5. Execute and report the 375 main runs with the frozen configuration.

The context candidate can be versioned independently. This design stays marked as a review draft until the decisions in step 2 are settled; no main benchmark is started by accepting the glossary.
