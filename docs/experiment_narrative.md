# Does Better Data Grounding Make AI Analytics More Reliable?

## The short version

- We ran a controlled test: one model, one frozen dataset, 25 business questions, six progressively richer data environments, three repetitions each — 450 attempts total.
- Raw source tables got 47% of answers right. A full semantic layer with business context got 76%.
- The biggest single jump wasn't adding a semantic layer. It was cleaning up the joins and adding business logic at the intermediate layer.
- Two questions failed across every arm, every rep. That's a model problem, not a data problem.
- One arm achieved zero variance across all three runs. It also got every policy question right.

---

## The mental model

Six arms, each inheriting the previous layer's SQL access:

| Arm | What the agent can see |
|-----|----------------------|
| A | Raw source + staging tables |
| B | + Intermediate (clean joins, business logic) |
| C | + Core (fact and dimension models) |
| D | + Mart (pre-aggregated summaries) |
| E | + 19 MetricFlow semantic metrics |
| F | + Business context glossary |

The question was simple: does each rung earn its place?

---

## The test

25 questions drawn from real analyst workflows — order counts, GMV, cancellation rates, delivery comparisons, customer segmentation, correlation analysis. Three questions required business eligibility rules that only arm F received. The rest were pure data questions any arm could theoretically answer.

Three repetitions per arm×question to measure consistency, not just accuracy. Temperature 0 throughout.

One thing we changed from the first run: we removed formula hints from the questions. "What was the cancellation rate?" not "cancelled orders divided by all orders times 100." If the semantic layer encodes the definition, the question shouldn't have to.

---

## What the climb looks like

| Arm | Mean correct / 25 | ±std |
|-----|------------------:|-----:|
| A — source only | 11.7 | 0.6 |
| B — +intermediate | 15.7 | 0.6 |
| C — +core | 16.3 | 0.6 |
| D — +marts | 16.3 | 0.6 |
| E — +MetricFlow | 17.3 | 1.2 |
| F — +glossary | **19.0** | **0.0** |

---

## Four things worth pulling out

**1. The intermediate layer is where most of the signal lives.**
A→B is the largest jump: +4 correct answers per run. Moving from raw source tables to clean intermediate models — proper joins, consistent grain, business logic encoded in SQL — almost immediately closes the gap on questions that require joining across entities. If you're debating where to invest first, this is the answer.

**2. Marts didn't move the needle.**
C and D are statistically tied. Pre-aggregated mart tables didn't help the agent answer questions more accurately than core fact/dimension models. The agent was already joining correctly. Aggregation without semantic definition is just a shortcut the model didn't need.

**3. The semantic layer adds accuracy but also variance.**
E outperforms D on data questions (17.3 vs 16.3), but its standard deviation is twice as high (±1.2 vs ±0.6). MetricFlow queries timed out on a small number of attempts, and the agent fell back to SQL with mixed results. The semantic layer is the right tool — but only when it's stable.

**4. The glossary turns policy questions from impossible to trivial.**
Arms A–E all answered the three business-context questions (Q22–Q24) with plausible but wrong numbers — they had no way to know the `rating_count >= 100` eligibility rule. Arm F, which received the rule, got all three right in every rep. This wasn't a data access problem. It was a definition access problem. F also achieved zero variance (19/25, ±0) — the most consistent arm in the study.

---

## What grounding can't fix

Two questions failed across all six arms, all three reps. Both required the model to compute percentages or decompositions precisely from query results. It consistently got close but not close enough.

This isn't a grounding problem. Better data access can't make a model more arithmetically precise. The fix is instructing the agent to push calculations back into SQL — not to compute in its head.

---

## The uncomfortable finding

We almost missed the B signal entirely. In an earlier run, the questions included formula hints ("report a single annual total, not a daily series"). That gave arm A enough scaffolding to answer correctly, masking the gap. Removing the hints made the test harder — and more honest. The jump from A to B only appeared clearly once we stopped helping the weakest arm.

The implication: if you're evaluating an AI analytics agent and the questions spell out the computation, you're testing instruction-following, not grounding.

---

## What happens when you swap the model

We ran the same benchmark a second time — same 25 questions, same six arms, same three repetitions — but replaced gpt-4.1 with gpt-6-luna at reasoning_effort=high.

| Arm | gpt-4.1 mean / 25 | gpt-6-luna mean / 25 | Delta |
|-----|------------------:|---------------------:|------:|
| A — source only | 11.7 | 19.3 | +7.7 |
| B — +intermediate | 15.7 | 21.0 | +5.3 |
| C — +core | 16.3 | 21.7 | +5.3 |
| D — +marts | 16.3 | 21.7 | +5.3 |
| E — +MetricFlow | 17.3 | 22.0 | +4.7 |
| F — +glossary | **19.0** | **25.0** | +6.0 |

The overall gain is +34 correct answers per run (+36%). The shape of the curve is the same — grounding still matters, and in the same order — but the floor moved up sharply.

**Three questions that were broken are now fixed.** Q07 (percentage change in order count), Q14 (veg/non-veg unit share with the correct three-group denominator), and Q20 (GMV decomposition to ±INR 0.05 per component) failed across every arm and every rep with gpt-4.1. Luna gets all three right, consistently. These weren't grounding failures. They were precision failures: the model was computing in its head instead of pushing arithmetic into SQL. A stronger reasoner pushes it into SQL.

**Arm F is now perfect.** 25/25 in every repetition, zero variance across all three runs. This closes the loop: once the model can reason precisely enough and the data layer encodes every definition, the questions become answerable.

**Variance nearly disappeared.** gpt-4.1's arm E had ±1.2 (MetricFlow timeouts causing fallbacks). Luna's worst arm is ±0.47, and that variance lives entirely in arm A, where the staging layer has two candidate GMV fields and the model sometimes asks for clarification rather than guessing. That's not a failure — it's the right behavior under ambiguity.

The residual failures in luna (arms A–E, Q22–Q24) are definitional: the business eligibility rule isn't in the data. No model can answer those without it.

---

## Two experiments, one finding

The data layer determines the ceiling. The model determines how close you get to it.

gpt-4.1 at arm F hits 76%. Luna at arm F hits 100%. The ceiling for arm F is 100%; gpt-4.1 leaves 24 percentage points on the table due to arithmetic precision. Luna closes that gap entirely.

But neither model can answer the business-context questions without the glossary. The semantic layer and the model capability are independent axes. You need both.
