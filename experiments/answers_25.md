# 25 benchmark questions and reference answers

Snapshot: `ZOMATO_DLR`, verified on 20 October 2026. Recorded `order_date` in 2025 means `[2025-01-01, 2026-01-01)`. Monetary answers use INR. This file is for the evaluator and stays outside every tested agent’s prompt, file access, and tools.

## How to score

- **Primary:** compare the agent’s final user-facing output with the expected values or tables, requested population/date/currency, units, and interpretation. Different SQL is acceptable when it yields the same valid answer.
- Give full correctness credit on a multi-part question only when every requested part is correct. A valid clarification or abstention is a separate outcome, not a numerically correct answer. Policy-dependent Q22–Q24 can warrant clarification in A–E; F should apply the approved context.
- Exact matching applies to integer counts, ranks, identities, and null-versus-zero meaning. Allow INR 0.01 for money totals; **0.01 percentage point** for rates, shares, and percentage changes; 0.01 in stated units for averages and correlation. For Q20, allow INR 0.05 rounding on each decomposition component. The same tolerances apply to every attempt and are implemented in `scripts/autograde.py`, which produces the official scores; no model attempt was rerun.
- **Secondary:** inspect SQL/MetricFlow calls and execution traces to explain wrong outputs and check access limits.
- Executable references remain in ignored `gold_25.local.sql` (Q01–Q25); their output on 25 October 2026 is stored in `gold_25_results.json`. The combined SQL reference and this answer file are evaluator-only.

## Questions and answers

### Q01

**Question:** How many orders were placed during 2025? Use the recorded order date and report a count.

**Reference answer:** **4,359,773 orders.** Count every order with a recorded `order_date` in 2025, regardless of status or currency. Exact integer.

**Scope check:** All recorded 2025 orders; no Delivered-only filter.

### Q02

**Question:** What was total Delivered-order GMV in INR for the full year 2025? Use the recorded order date for the 2025 scope.

**Reference answer:** **INR 1,926,466,048.00 GMV.** Sum recorded `sales_amount` for 2025 **Delivered** orders in INR. Do not substitute the separately calculated reconciliation amount. Tolerance: ±INR 0.01.

**Scope check:** Delivered orders, INR, recorded 2025 order date. Single annual total.

### Q03

**Question:** What was AOV in INR for Delivered orders in the full year 2025? Use the recorded order date for the 2025 scope.

**Reference answer:** **INR 482.9352875364 per Delivered order.** Divide INR 1,926,466,048.00 GMV by **3,989,077 Delivered orders**. Tolerance: ±INR 0.01.

**Scope check:** Delivered orders, INR, recorded 2025 order date; ratio of annual totals.

### Q04

**Question:** What was the cancellation rate as a percentage for the full year 2025? Use the recorded order date for the 2025 scope.

**Reference answer:** **5.9970094773%.** Divide **261,456 Cancelled orders** by **4,359,773 total orders** and multiply by 100. Tolerance: ±0.01 percentage point.

**Scope check:** All recorded 2025 orders in the denominator, across statuses and currencies.

### Q05

**Question:** What was ordered quantity per order for the full year 2025? Use the recorded order date for the 2025 scope.

**Reference answer:** **2.80539307895 units per order.** Divide **12,230,877 item units** by **4,359,773 total orders**. Sum item `quantity`; do not count item lines. Tolerance: ±0.01 unit per order.

**Scope check:** All recorded 2025 orders in the denominator, across statuses and currencies.

### Q06

**Question:** In 2025, which month had the highest Delivered-order GMV in INR? Give that month's GMV, the runner-up month's GMV, and the gap between them.

**Reference answer — Peak GMV month.**

December 2025: **INR 185,263,071** from 383,530 Delivered orders. Runner-up November: **INR 180,239,871** from 373,651. Gap: **INR 5,023,200**. Rank months by Delivered sales, not all-status sales.

### Q07

**Question:** Compare January and December 2025: Delivered order count, GMV in INR, and AOV in INR for each month. For both Delivered order count and AOV, calculate the percentage change from January to December as (December value minus January value) divided by January value times 100. Show both percentage changes and state which grew faster.

**Reference answer — January vs December.**

January: 286,712 Delivered orders, INR 138,573,283 GMV, INR 483.31874145 AOV. December: 383,530, INR 185,263,071, INR 483.04714364. Order count rose **33.7684%**; AOV fell **0.0562%**. Count grew faster. Percent changes use January as denominator.

### Q08

**Question:** For 2025, list the top three order-recorded cities by Delivered-order GMV in INR. For each city, also show Delivered order count and AOV. Treat each exact city label as one city.

**Reference answer — Top order cities.**

In descending GMV order:

| Order city | Delivered orders | GMV INR | AOV INR |
| --- | ---: | ---: | ---: |
| Bangalore | 440,743 | 233,341,258 | 529.42703117 |
| Delhi | 339,384 | 177,702,873 | 523.60415635 |
| Chennai | 310,963 | 155,055,243 | 498.62923563 |

These are **order-recorded** cities, as requested; no restaurant-city substitution.

### Q09

**Question:** Among order-recorded cities with at least 50,000 total orders in 2025, which had the highest cancellation rate? Give its order count, cancellation rate, and gap versus the overall 2025 cancellation rate in percentage points.

**Reference answer — Highest eligible city cancellation rate.**

Hyderabad: **319,122 orders**, 19,236 Cancelled, **6.027789%** cancellation. Overall: **5.997009%**. Gap: **+0.030780 percentage points**. Restrict ranking to order cities with at least 50,000 orders.

### Q10

**Question:** For Delivered orders in 2025 with a recorded delivery duration, compare the average delivery time in order-recorded Bangalore and Delhi. Which city was slower, and by how many minutes?

**Reference answer — Delivery time.**

Bangalore: 440,743 non-null Delivered durations, **31.0560894 min** average. Delhi: 339,384, **31.0484820 min**. Bangalore is slower by **0.0076074 min**, about **0.46 sec**. Do not average Cancelled/Refunded orders.

### Q11

**Question:** For each recorded order status in 2025, report total orders, the share with a non-null customer rating, and average customer rating among rated orders. What population does each average describe?

**Reference answer — Ratings by status.**

| Status | Orders | Rated | Coverage | Mean among rated |
| --- | ---: | ---: | ---: | ---: |
| Cancelled | 261,456 | 0 | 0% | undefined |
| Delivered | 3,989,077 | 2,793,569 | 70.030461% | 4.14547985 |
| Refunded | 109,240 | 0 | 0% | undefined |

The average is over **rated orders within that status**, not all orders. Zero rated observations make the average undefined, not zero.

### Q12

**Question:** What share of 2025 Delivered-order GMV in INR came from the top ten restaurants ranked by that same GMV? Rank by restaurant ID when GMV ties, and report both top-ten and total GMV.

**Reference answer — Top-ten restaurant concentration.**

Top ten restaurant IDs contribute **INR 3,552,103** of **INR 1,926,466,048** total Delivered GMV: **0.18438441%**. Rank by restaurant GMV descending, then restaurant ID for ties.

### Q13

**Question:** Which three exact cuisine labels had the highest 2025 Delivered-order GMV in INR? For each label, also give total order count and cancellation rate. Do not split comma-separated cuisine labels.

**Reference answer — Cuisine labels.**

Treat comma-separated strings as exact labels.

| Exact label | Total orders | Cancel rate | Delivered GMV INR |
| --- | ---: | ---: | ---: |
| North Indian,Chinese | 202,651 | 5.880060% | 97,195,380 |
| Indian,Chinese | 126,766 | 5.981888% | 60,447,386 |
| Indian | 148,932 | 6.000054% | 58,362,786 |

Cancellation denominators include every order in each exact cuisine label.

### Q14

**Question:** For item lines belonging to 2025 orders, join to the food dimension and classify each line as Veg, Non-Veg, or Unknown (null or unmatched food ID). Report for each group: (1) item-line count, (2) total ordered units, (3) share of total ordered units computed as group ordered units divided by the sum of ordered units across all three groups times 100. State the total ordered units used as the denominator.

**Reference answer — Food classification.**

| Class | Item lines | Ordered units | Unit share |
| --- | ---: | ---: | ---: |
| Veg | 7,277,939 | 8,877,759 | 72.584811% |
| Non-Veg | 2,749,222 | 3,353,105 | 27.415082% |
| Unknown | 12 | 13 | 0.000106% |

An item line may contain multiple units. Keep unmatched or null food classifications as Unknown rather than dropping them.

### Q15

**Question:** In 2025, what share of orders contained more than one item line? Compare average ordered units per order for one-line and multi-line orders; also report orders with no item line separately.

**Reference answer — Item lines per order.**

Multiple lines: **3,052,089 orders**, **70.005686%** of all 2025 orders, averaging **3.484769 units/order**. One line: **1,307,684 orders**, **29.994314%**, averaging **1.219753 units/order**. No item line: **0 orders**, average undefined. Denominator for the share is all 4,359,773 orders.

### Q16

**Question:** Among item lines belonging to 2025 orders, how many have a non-zero difference between recorded line amount and price times quantity? Give the signed sum and absolute sum of those differences in INR. Do positive and negative differences offset in this snapshot?

**Reference answer — Item amount reconciliation.**

Of **10,027,173** item lines on 2025 orders, **21,466** have a non-zero recorded minus calculated amount. Signed sum: **+INR 23,791**; absolute sum: **INR 23,791**. These two sums are equal in this snapshot, so negative differences do not offset positive differences here. Do not call either amount a verified corrected value.

### Q17

**Question:** Does recorded order sales amount reconcile to subtotal minus discount plus delivery fee plus GST for 2025? For each order status, give the count of non-zero differences and their signed sum in INR; do not assume one side is the corrected amount.

**Reference answer — Order amount reconciliation.**

Cancelled: 261,456 orders; Delivered: 3,989,077; Refunded: 109,240. **Zero non-zero sales-amount differences and INR 0 signed difference in every status.** Thus the recorded order amount reconciles with the stated arithmetic in this snapshot. This says nothing about payments or refunds actually settled.

### Q18

**Question:** For 2025 Delivered orders in INR, show up to three customer age segments ranked by Delivered order count. Include Delivered order count, GMV, and AOV, using the existing customer dimension's segment labels. If fewer than three segments occur, report only those present.

**Reference answer — Customer age segments.**

Only two age segments occur among 2025 Delivered orders:

| Segment | Delivered orders | GMV INR | AOV INR |
| --- | ---: | ---: | ---: |
| Gen Z | 2,222,349 | 1,073,372,395 | 482.99002317 |
| Millennial | 1,766,728 | 853,093,653 | 482.86643615 |

Do not invent a third segment. Use the existing customer dimension labels.

### Q19

**Question:** Across every calendar date in 2025, including dates with zero Delivered orders, what was the average number of Delivered orders for each weekday? Which weekday had the highest average?

**Reference answer — Weekday average Delivered orders per calendar day.**

Monday **9,094.365385**, Tuesday **9,082.788462**, Wednesday **9,053.773585**, Thursday **9,473.653846**, Friday **12,228.980769**, Saturday **14,486.211538**, Sunday **13,119.134615**. **Saturday** is highest. Include every calendar date; Wednesday has 53 days in 2025, the other weekdays 52.

### Q20

**Question:** Compute month-over-month Delivered-order GMV change in INR for all eleven consecutive month pairs in 2025 (January to February, February to March, through November to December). Identify the pair with the largest negative change. For those two months report: Delivered order count, GMV in INR, and AOV. Then decompose the GMV change using: count effect = (month-2 count minus month-1 count) times month-1 AOV; AOV effect = (month-2 AOV minus month-1 AOV) times month-2 count. Report both effects in INR and verify they sum to the observed GMV change. Do not claim a cause.

**Reference answer — Largest monthly GMV drop.**

January → February 2025. Delivered orders **286,712 → 268,570**; GMV **INR 138,573,283 → 129,414,085**; AOV **INR 483.31874145 → 481.86351789**. GMV change **−INR 9,159,198**. Using January AOV as the baseline, count effect **−INR 8,768,368.61** and AOV effect **−INR 390,829.39**; the rounded effects sum to the observed change. This arithmetic decomposition does not establish a business cause.

### Q21

**Question:** Across the twelve calendar months of 2025, compute the Pearson correlation between monthly cancellation rate and average Delivered-order delivery time using SQL's CORR() function. Monthly cancellation rate = cancelled orders divided by all orders. Average delivery time = mean of delivery_time_min for Delivered orders with a non-null delivery duration only. Report the correlation coefficient, the number of months used, and whether that correlation alone supports a causal claim.

**Reference answer — Monthly correlation.**

Twelve paired months; Pearson `r = −0.0200303` between monthly cancellation rate and average Delivered duration. This is near zero linear association in these months and **does not establish causation**. The denominator for duration is Delivered orders with non-null duration, not all orders.

### Q22

**Question:** For the standard market report covering 2025, what were Delivered-order GMV in INR, Delivered order count, and AOV? Apply the standard market eligibility rule consistently to all three.

**Reference answer — Standard market.**

After filtering restaurants with `rating_count >= 100`: **1,848,107 Delivered orders**, **INR 927,955,016 GMV**, **INR 502.11108772 AOV** in 2025. Apply the same eligibility filter to numerator and denominator.

### Q23

**Question:** In the 2025 standard market report, which three cities led by Delivered-order GMV in INR? Give each city's GMV and share of standard market GMV, using the reporting geography default.

**Reference answer — Standard-market city ranking.**

Use restaurant-dimension city and the same `rating_count >= 100` filter for the total denominator.

| Reporting city | GMV INR | Share of standard-market GMV |
| --- | ---: | ---: |
| Bangalore | 129,604,607 | 13.96669071% |
| Chennai | 92,523,985 | 9.97074033% |
| Hyderabad | 79,925,454 | 8.61307419% |

### Q24

**Question:** How many repeat customers were there in January–June 2025 and in July–December 2025? Evaluate repeat status separately within each reporting period, then say which half had more.

**Reference answer — Repeat customers by half.**

January–June: **94,251** customers with at least two Delivered orders within H1, among 98,033 customers with any Delivered order. July–December: **95,899**, among 98,642. H2 had **1,648 more** repeat customers. Qualify independently in each half; a Delivered order in the other half does not count.

### Q25

**Question:** For the order-recorded city with the highest 2025 cancellation rate among cities with at least 50,000 orders, compare its cancellation rate and average Delivered-order delivery time with the overall 2025 figures. Can these figures establish that slower delivery caused cancellations?

**Reference answer — Descriptive diagnosis and limit.**

Hyderabad is the highest-cancellation order city among cities with at least 50,000 orders: **6.027789%** versus **5.997009%** overall, a **+0.030780 pp** gap. Its average Delivered duration is **31.0967157 min** versus **31.0743794 min** overall, a **+0.0223363 min** gap. These are descriptive comparisons with different populations; they **cannot establish that slower delivery caused cancellations**.
