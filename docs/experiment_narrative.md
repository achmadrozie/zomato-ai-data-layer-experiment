# Does Better Data Grounding Make AI Analytics More Reliable?

## The short version

- We ran a controlled test: two models, one frozen dataset, 25 business questions, six progressively richer data environments ("arms"), three repetitions each — 900 attempts in total (450 per model).
- With `gpt-4.1`, raw source tables got 45% of answers right (11.3 of 25). The full stack with semantic metrics and a business glossary got 73% (18.3 of 25).
- Most of the climb comes from reaching the intermediate and core layers (A→C, +5.3 correct answers). After C the data-question score is flat: C, D, and E differ by less than the repetition-to-repetition spread.
- The glossary is what makes the three policy questions answerable. No arm without it answered any of them correctly.
- With `gpt-6-luna` (reasoning effort high) the same benchmark scores 130.7 of 150 versus 93.3 for `gpt-4.1`, and the biggest remaining gap is access to definitions, not arithmetic.

---

## How it was scored

Every final answer is graded by one deterministic script, [`scripts/autograde.py`](../scripts/autograde.py), against reference values obtained by re-running the author's gold SQL on 25 October 2026. The same rules apply to every attempt; the script never looks at the arm or the model. An earlier manual grading agreed on 887 of 900 attempts; the 13 differences (all `gpt-4.1`) were reviewed one by one and replaced by the script's score. Luna's manual and scripted scores were identical.

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

25 questions drawn from analyst workflows — order counts, GMV, cancellation rates, delivery comparisons, customer segmentation, correlation analysis. Three questions (Q22–Q24) require business rules that only arm F receives; the other 22 are data questions any arm could in principle answer. Each arm × question × model was run three times to measure consistency, not just accuracy.

---

## What the climb looks like (`gpt-4.1`, temperature 0)

| Arm | Data correct / 22 | Total correct / 25 | ±std (total) |
|-----|------------------:|-------------------:|-----:|
| A — source only | 11.3 | 11.3 | 0.6 |
| B — +intermediate | 14.0 | 14.0 | 1.0 |
| C — +core | 16.7 | 16.7 | 1.2 |
| D — +marts | 16.3 | 16.3 | 0.6 |
| E — +MetricFlow | 16.7 | 16.7 | 0.6 |
| F — +glossary | 15.3 | **18.3** | 0.6 |

---

## Four things worth pulling out

**1. Reaching the intermediate and core layers matters most.**
A→B adds 2.7 correct answers per run and B→C adds another 2.7. Part of this is plain access: the customer age-segment labels live in the core dimension, so Q18 fails in A and B and is answerable from C onward. Part is cleaner joins: Q13 (cuisine order counts) fails in A, B, and C in every repetition for `gpt-4.1`.

**2. Marts and MetricFlow did not move the data score.**
C, D, and E sit at 16.7, 16.3, and 16.7. The 0.3-point differences are smaller than the standard deviation across repetitions (0.6–1.2), so the data cannot rank them. Optional semantic access is not a measurable gain here.

**3. The glossary turns policy questions from impossible to trivial.**
Arms A–E answered the three business-context questions (Q22–Q24) without the rules, and none of those answers matched the reference. Arm F, which received the `rating_count >= 100` eligibility, restaurant-city geography, and repeat-customer rules, got all three right in every repetition. That is a definition-access problem, not a data-access problem. F's data score (15.3 of 22) is slightly below C–E because Q12, Q15, and Q19 fail in F in every repetition, so the glossary neither helped nor reliably hurt on data questions.

**4. Some failures are arithmetic, not grounding.**
Q07, Q14, and Q20 fail in 18, 18, and 17 of 18 `gpt-4.1` attempts respectively. The model does the percentage or decomposition by hand in its final answer — for example, 33.732% instead of 33.7684% for Q07 — instead of pushing it into SQL. Q12 shows the same weakness: the model listed ten GMV values that sum to 3,552,103 and then wrote 3,552,107.

---

## What happens when you swap the model

Same 25 questions, same six arms, same three repetitions, with `gpt-6-luna` at reasoning effort high instead of `gpt-4.1`.

| Arm | gpt-4.1 mean / 25 | gpt-6-luna mean / 25 | Delta |
|-----|------------------:|---------------------:|------:|
| A — source only | 11.3 | 19.3 | +8.0 |
| B — +intermediate | 14.0 | 21.0 | +7.0 |
| C — +core | 16.7 | 21.7 | +5.0 |
| D — +marts | 16.3 | 21.7 | +5.3 |
| E — +MetricFlow | 16.7 | 22.0 | +5.3 |
| F — +glossary | 18.3 | **25.0** | +6.7 |

Overall, Luna scores 130.7 of 150 against 93.3 (+37.3 correct answers, +40%). The shape of the curve is similar, but the floor moved up sharply.

**Precision failures mostly disappear.** Q07, Q14, and Q20 fail almost everywhere for `gpt-4.1` but are answered correctly by Luna in nearly every arm (Q07 is the exception in a few arm-A and arm-C repetitions).

**Luna's remaining misses are about definitions.** In arm A it sometimes asks which amount defines GMV (SUBTOTAL or SALES_AMOUNT), once answered with SUBTOTAL, and fails Q18 in A and B because the age-segment labels are not visible there. Q22–Q24 fail in A–E because the rules are absent. The question text does not define GMV, so part of this variance reflects an ambiguity in the benchmark itself.

**Arm F is perfect.** 25 of 25 in all three repetitions. Read this as "once the model can compute precisely and the glossary supplies the rules, this benchmark is solved", not as proof that the benchmark is hard: the reference answers, the questions, and the glossary rules come from the same author and snapshot.

**Variance nearly disappears.** Luna's total standard deviation across repetitions is 0.6, with no variation at all in arms B, E, and F.

---

## Two experiments, one finding

The data layer and the glossary set what is answerable; the model decides how close you get. `gpt-4.1` leaves about a quarter of the benchmark unanswered even with every layer, largely through arithmetic. Luna closes that gap. Neither model can answer the policy questions without the glossary. They are independent axes, and you need both.

## Limits

One dataset, two models, three repetitions per cell. Differences below about one point are within the repetition noise. The benchmark was authored together with its reference answers, and the scoring script checks that required values are present and correct, not that every sentence of an answer is sound.
