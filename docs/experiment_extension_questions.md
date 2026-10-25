# Three follow-up analysis tasks

These tasks extend the frozen Q01–Q25 benchmark. They are **not** part of its 900 scored attempts. Each asks for a descriptive diagnosis and a decision; the snapshot cannot establish causal effects on its own. Use the recorded order date for 2025, keep INR amounts separate from other currencies, and state denominators and missing-data limits.

## E01 — Why did monthly Delivered GMV fall from January to February?

> The existing analysis identifies January → February 2025 as the largest month-over-month drop in Delivered-order GMV. Diagnose whether this indicates weaker daily demand. Compare both months' total and per-calendar-day Delivered order count and INR GMV, plus AOV. Decompose the total GMV change into a calendar-day exposure component and changes in Delivered orders per day and AOV; show a formula whose components reconcile to the observed change. Check whether the change is broad across order-recorded cities or concentrated in a few, using each city's contribution to the net change. Give one operational recommendation and the evidence that would be needed before treating any proposed driver as causal.

**Why this adds value:** Q20 decomposes totals into count and AOV but does not account for February's 28 days versus January's 31. The reference totals imply GMV per day increased from about INR 4.47m to INR 4.62m, so a claim that daily demand fell would be unsupported. City attribution adds a second diagnostic layer.

**Review criteria:** Correct month lengths and per-day denominators; an exact, stated decomposition order; city contributions calculated from Delivered INR GMV with the same date scope; recommendation proportional to the evidence; no causal claim from aggregate data.

## E02 — Should Hyderabad cancellation be the next intervention priority?

> Among order-recorded cities with at least 50,000 orders in 2025, quantify Hyderabad's cancellation rate, the overall rate, their percentage-point gap, and the approximate number of cancellations represented by that gap at Hyderabad's order volume. Compare monthly Hyderabad and overall rates and check whether the gap is persistent or driven by a few months. Compare Delivered-order delivery durations only among orders with a recorded duration, stating why they cannot be used as the cancellation population. Decide whether Hyderabad warrants immediate intervention, targeted investigation, or no special action; propose one measurable test or additional dataset that would distinguish possible causes.

**Why this adds value:** Q09 and Q25 identify the highest eligible city but the observed annual gap is only about 0.0308 percentage points. Ranking alone can make a very small difference look operationally important. A monthly check, effect size, and decision threshold make the recommendation more defensible.

**Review criteria:** All-order cancellation denominators; absolute impact and monthly comparisons; Delivered-only duration denominator; explicit uncertainty and practical significance; no claim that observed delivery duration caused cancellations.

## E03 — Did repeat-customer performance improve in H2, and what should be tested next?

> For January–June and July–December 2025 separately, count customers with at least one Delivered order, customers with at least two Delivered orders within that half, and the resulting repeat-customer rate. Compare the rates as well as the raw counts. Break the change down by customers present in both halves versus those present in only one half, and by the distribution of Delivered orders per customer within each half; avoid counting a customer's H1 orders toward H2 qualification. Explain which parts reflect observed composition or frequency and which cannot be assigned a cause. Recommend one retention experiment with a target population, treatment, primary outcome, and guardrail.

**Why this adds value:** Q24 reports 94,251 versus 95,899 repeat customers, but the active-customer bases also differ (98,033 versus 98,642). The implied rates are about 96.14% and 97.22%, a 1.08 percentage-point rise. Cohort overlap and frequency distinguish a larger base from higher repeat incidence without pretending to identify a causal retention mechanism.

**Review criteria:** Independent half-year repeat qualification, unique-customer denominators, explicit overlap accounting, a coherent explanation of count versus rate change, and a testable recommendation rather than a causal conclusion from this snapshot.

## Review performed

- Read the frozen 25 prompts and reference answers, especially Q09, Q20, Q24, and Q25.
- Checked the order fact and mart documentation for city, status, date, currency, delivery duration, and customer ID availability.
- Calculated the daily January/February comparisons and H1/H2 repeat rates from the published reference totals. These are design checks, not new warehouse query results.
- Kept this extension separate from `questions_25.json` and the existing grade files so the 900-attempt comparison remains reproducible.
