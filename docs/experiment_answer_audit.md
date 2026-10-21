# Audit jawaban A–F: 25 pertanyaan

Perbandingan ini memakai **jawaban akhir asli** dari 150 attempt `gpt-4.1` pada 21 Oktober 2026 dan skor revisi pada [`grades.local.json`](../experiments/run.local/af_25/grades.local.json). Kunci disalin dari [`answers_25.md`](../experiments/answers_25.md). Tidak ada model yang dijalankan ulang.

**Rubrik:** semua bagian jawaban harus benar; count, identitas, dan rank eksak; total uang ±INR 0,01; persentase ±0,01 percentage point; average/korelasi ±0,01 unit; komponen Q20 ±INR 0,05. Q22–Q24 memerlukan kebijakan bisnis. `✓` berarti seluruh jawaban sesuai; `✗` berarti ada bagian salah atau tidak lengkap.

| Arm | Benar |
| --- | ---: |
| A | 5/25 |
| B | 9/25 |
| C | 9/25 |
| D | 10/25 |
| E | 11/25 |
| F | 11/25 |

## Q01

**Pertanyaan:** How many orders were placed during 2025? Use the recorded order date and report a count.

**Kunci dan cakupan:**

**Reference answer:** **4,359,773 orders.** Count every order with a recorded `order_date` in 2025, regardless of status or currency. Exact integer.

**Scope check:** All recorded 2025 orders; no Delivered-only filter.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✓ | Correct annual order count |
| B | ✓ | Correct annual order count |
| C | ✓ | Correct annual order count |
| D | ✓ | Correct annual order count |
| E | ✓ | Correct annual order count |
| F | ✓ | Correct annual order count |

<details><summary>Jawaban asli A — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, based on the recorded order date. The population is all orders in the ZOMATO_DLR.SOURCES.ORDERS table with ORDER_DATE in 2025. The unit is orders. This is a simple count, with no further breakdown or filtering.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count represents all orders in the population for the year 2025.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, using the recorded order date. This count represents all orders in the population for the calendar year 2025.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count represents all orders in the population for the full year 2025.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count includes all orders regardless of their status.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count includes all orders regardless of their status.

</details>


## Q02

**Pertanyaan:** What was GMV in INR during 2025, by recorded order date?

**Kunci dan cakupan:**

**Reference answer:** **INR 1,926,466,048.00 GMV.** Sum recorded `sales_amount` for 2025 **Delivered** orders in INR. Do not substitute the separately calculated reconciliation amount. Tolerance: ±INR 0.01.

**Scope check:** Delivered orders, INR, recorded 2025 order date.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Returned daily series instead of annual GMV |
| B | ✗ | Returned daily series instead of annual GMV |
| C | ✗ | Returned daily series instead of annual GMV |
| D | ✗ | Returned daily GMV instead of annual total |
| E | ✗ | Returned monthly series instead of annual GMV |
| F | ✗ | Returned monthly GMV instead of annual total |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the GMV (Gross Merchandise Value) in INR by recorded order date is as follows for the first 40 days:
> - 2025-01-01: 3,923,838 INR
> - 2025-01-02: 4,210,730 INR
> - 2025-01-03: 5,450,756 INR
> - 2025-01-04: 6,300,784 INR
> - 2025-01-05: 5,820,316 INR
> - 2025-01-06: 4,021,852 INR
> - 2025-01-07: 4,080,510 INR
> - 2025-01-08: 4,047,828 INR
> - 2025-01-09: 4,265,598 INR
> - 2025-01-10: 5,527,503 INR
> - 2025-01-11: 6,574,206 INR
> - 2025-01-12: 5,760,226 INR
> - 2025-01-13: 4,067,126 INR
> - 2025-01-14: 4,109,423 INR
> - 2025-01-15: 4,029,936 INR
> - 2025-01-16: 4,140,103 INR
> - 2025-01-17: 5,543,301 INR
> - 2025-01-18: 6,507,723 INR
> - 2025-01-19: 5,980,067 INR
> - 2025-01-20: 4,114,645 INR
> - 2025-01-21: 4,055,764 INR
> - 2025-01-22: 4,104,455 INR
> - 2025-01-23: 4,252,622 INR
> - 2025-01-24: 5,482,147 INR
> - 2025-01-25: 6,656,481 INR
> - 2025-01-26: 5,990,520 INR
> - 2025-01-27: 4,102,421 INR
> - 2025-01-28: 4,013,917 INR
> - 2025-01-29: 4,258,449 INR
> - 2025-01-30: 4,392,232 INR
> - 2025-01-31: 5,641,685 INR
> - 2025-02-01: 6,569,399 INR
> - 2025-02-02: 5,981,288 INR
> - 2025-02-03: 4,229,103 INR
> - 2025-02-04: 4,168,792 INR
> - 2025-02-05: 4,190,817 INR
> - 2025-02-06: 4,311,568 INR
> - 2025-02-07: 5,490,181 INR
> - 2025-02-08: 6,625,609 INR
> - 2025-02-09: 6,107,809 INR
>
> Each value represents the total GMV in INR for that recorded order date. Only the first 40 days are shown here; more data is available for the rest of 2025 if needed.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, the GMV (Gross Merchandise Value) in INR by recorded order date is as follows (first 40 days):
> - 2025-01-01: 3,923,838 INR
> - 2025-01-02: 4,210,730 INR
> - 2025-01-03: 5,450,756 INR
> - 2025-01-04: 6,300,784 INR
> - 2025-01-05: 5,820,316 INR
> - 2025-01-06: 4,021,852 INR
> - 2025-01-07: 4,080,510 INR
> - 2025-01-08: 4,047,828 INR
> - 2025-01-09: 4,265,598 INR
> - 2025-01-10: 5,527,503 INR
> - 2025-01-11: 6,574,206 INR
> - 2025-01-12: 5,760,226 INR
> - 2025-01-13: 4,067,126 INR
> - 2025-01-14: 4,109,423 INR
> - 2025-01-15: 4,029,936 INR
> - 2025-01-16: 4,140,103 INR
> - 2025-01-17: 5,543,301 INR
> - 2025-01-18: 6,507,723 INR
> - 2025-01-19: 5,980,067 INR
> - 2025-01-20: 4,114,645 INR
> - 2025-01-21: 4,055,764 INR
> - 2025-01-22: 4,104,455 INR
> - 2025-01-23: 4,252,622 INR
> - 2025-01-24: 5,482,147 INR
> - 2025-01-25: 6,656,481 INR
> - 2025-01-26: 5,990,520 INR
> - 2025-01-27: 4,102,421 INR
> - 2025-01-28: 4,013,917 INR
> - 2025-01-29: 4,258,449 INR
> - 2025-01-30: 4,392,232 INR
> - 2025-01-31: 5,641,685 INR
> - 2025-02-01: 6,569,399 INR
> - 2025-02-02: 5,981,288 INR
> - 2025-02-03: 4,229,103 INR
> - 2025-02-04: 4,168,792 INR
> - 2025-02-05: 4,190,817 INR
> - 2025-02-06: 4,311,568 INR
> - 2025-02-07: 5,490,181 INR
> - 2025-02-08: 6,625,609 INR
> - 2025-02-09: 6,107,809 INR
>
> Population: All orders recorded in 2025 with currency INR. Unit: INR per day. Interpretation: These values represent the daily sum of sales amounts (GMV) in INR for each recorded order date in 2025 (first 40 days shown).

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> GMV (Gross Merchandise Value) in INR during 2025, by recorded order date, is as follows for the first 40 days:
> - 2025-01-01: 3,923,838 INR
> - 2025-01-02: 4,210,730 INR
> - 2025-01-03: 5,450,756 INR
> - 2025-01-04: 6,300,784 INR
> - 2025-01-05: 5,820,316 INR
> - 2025-01-06: 4,021,852 INR
> - 2025-01-07: 4,080,510 INR
> - 2025-01-08: 4,047,828 INR
> - 2025-01-09: 4,265,598 INR
> - 2025-01-10: 5,527,503 INR
> - 2025-01-11: 6,574,206 INR
> - 2025-01-12: 5,760,226 INR
> - 2025-01-13: 4,067,126 INR
> - 2025-01-14: 4,109,423 INR
> - 2025-01-15: 4,029,936 INR
> - 2025-01-16: 4,140,103 INR
> - 2025-01-17: 5,543,301 INR
> - 2025-01-18: 6,507,723 INR
> - 2025-01-19: 5,980,067 INR
> - 2025-01-20: 4,114,645 INR
> - 2025-01-21: 4,055,764 INR
> - 2025-01-22: 4,104,455 INR
> - 2025-01-23: 4,252,622 INR
> - 2025-01-24: 5,482,147 INR
> - 2025-01-25: 6,656,481 INR
> - 2025-01-26: 5,990,520 INR
> - 2025-01-27: 4,102,421 INR
> - 2025-01-28: 4,013,917 INR
> - 2025-01-29: 4,258,449 INR
> - 2025-01-30: 4,392,232 INR
> - 2025-01-31: 5,641,685 INR
> - 2025-02-01: 6,569,399 INR
> - 2025-02-02: 5,981,288 INR
> - 2025-02-03: 4,229,103 INR
> - 2025-02-04: 4,168,792 INR
> - 2025-02-05: 4,190,817 INR
> - 2025-02-06: 4,311,568 INR
> - 2025-02-07: 5,490,181 INR
> - 2025-02-08: 6,625,609 INR
> - 2025-02-09: 6,107,809 INR
>
> Population: All orders with CURRENCY = 'INR' and ORDER_DATE in 2025. Unit: INR per day. Interpretation: These are the daily GMV totals in INR for the first 40 days of 2025, by recorded order date.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> GMV (Gross Merchandise Value) in INR during 2025, by recorded order date, is as follows for the first 40 days:
>
> - 2025-01-01: 3,577,795 INR
> - 2025-01-02: 3,847,841 INR
> - 2025-01-03: 4,994,719 INR
> - 2025-01-04: 5,786,166 INR
> - 2025-01-05: 5,331,611 INR
> - 2025-01-06: 3,686,736 INR
> - 2025-01-07: 3,728,311 INR
> - 2025-01-08: 3,676,186 INR
> - 2025-01-09: 3,900,527 INR
> - 2025-01-10: 5,065,854 INR
> - 2025-01-11: 6,016,103 INR
> - 2025-01-12: 5,254,581 INR
> - 2025-01-13: 3,725,521 INR
> - 2025-01-14: 3,769,737 INR
> - 2025-01-15: 3,672,492 INR
> - 2025-01-16: 3,819,213 INR
> - 2025-01-17: 5,059,308 INR
> - 2025-01-18: 5,955,029 INR
> - 2025-01-19: 5,484,296 INR
> - 2025-01-20: 3,746,013 INR
> - 2025-01-21: 3,701,206 INR
> - 2025-01-22: 3,736,160 INR
> - 2025-01-23: 3,894,050 INR
> - 2025-01-24: 5,011,801 INR
> - 2025-01-25: 6,112,900 INR
> - 2025-01-26: 5,546,092 INR
> - 2025-01-27: 3,747,460 INR
> - 2025-01-28: 3,672,146 INR
> - 2025-01-29: 3,888,812 INR
> - 2025-01-30: 4,011,159 INR
> - 2025-01-31: 5,153,458 INR
> - 2025-02-01: 6,003,813 INR
> - 2025-02-02: 5,486,315 INR
> - 2025-02-03: 3,890,748 INR
> - 2025-02-04: 3,829,776 INR
> - 2025-02-05: 3,806,507 INR
> - 2025-02-06: 3,934,815 INR
> - 2025-02-07: 4,975,430 INR
> - 2025-02-08: 6,058,673 INR
> - 2025-02-09: 5,553,484 INR
>
> Population: All delivered orders in INR, by recorded order date in 2025. Unit: INR. Interpretation: These are daily GMV totals for the first 40 days of 2025; each value represents the sum of delivered sales amounts for that day.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> Gross Merchandise Value (GMV) in INR for delivered orders in 2025, by recorded order month, is as follows (unit: INR):
>
> - January: 138,573,283
> - February: 129,414,085
> - March: 149,731,681
> - April: 145,794,592
> - May: 158,447,281
> - June: 156,551,606
> - July: 163,095,157
> - August: 173,914,937
> - September: 167,309,430
> - October: 178,131,054
> - November: 180,239,871
> - December: 185,263,071
>
> Population: All delivered orders recorded in 2025 with currency INR. Interpretation: GMV increased steadily throughout the year, peaking in December.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> Gross Merchandise Value (GMV) in INR for delivered orders during 2025, by recorded order month, is as follows (amounts in INR):
>
> - January: 138,573,283
> - February: 129,414,085
> - March: 149,731,681
> - April: 145,794,592
> - May: 158,447,281
> - June: 156,551,606
> - July: 163,095,157
> - August: 173,914,937
> - September: 167,309,430
> - October: 178,131,054
> - November: 180,239,871
> - December: 185,263,071
>
> Population: All delivered orders with currency INR, grouped by recorded order date (month) in 2025. Unit: INR. Interpretation: These values represent the total sales amount (GMV) for delivered orders each month in 2025, as recorded in INR.

</details>


## Q03

**Pertanyaan:** What was AOV in INR during 2025, by recorded order date?

**Kunci dan cakupan:**

**Reference answer:** **INR 482.9352875364 per Delivered order.** Divide INR 1,926,466,048.00 GMV by **3,989,077 Delivered orders**. Tolerance: ±INR 0.01.

**Scope check:** Delivered orders, INR, recorded 2025 order date; ratio of totals.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Daily all-status AOV instead of annual Delivered AOV |
| B | ✗ | Daily all-status AOV instead of annual Delivered AOV |
| C | ✗ | Daily all-status AOV instead of annual Delivered AOV |
| D | ✗ | Returned daily and all-status AOV instead of annual Delivered AOV |
| E | ✗ | Monthly AOV instead of annual Delivered AOV |
| F | ✗ | Daily AOV instead of annual Delivered AOV |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> The Average Order Value (AOV) in INR for each recorded order date in 2025 ranged from approximately 471.914168 INR to 491.374955 INR per order. For example, on 2025-01-01 the AOV was 478.400146 INR, and on 2025-01-22 it was 491.374955 INR. These values represent the daily average sales amount per order, calculated as total sales amount divided by the number of orders for each day, considering only orders recorded in INR currency during 2025. Units are INR per order. Population: all orders with CURRENCY = 'INR' and ORDER_DATE in 2025. Interpretation: AOV fluctuated daily within a narrow band, indicating relatively stable average spending per order in INR during this period.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, the Average Order Value (AOV) in INR by recorded order date is as follows (showing first 40 days):
>
> - 2025-01-01: 478.400146 INR
> - 2025-01-02: 486.564594 INR
> - 2025-01-03: 483.694738 INR
> - 2025-01-04: 480.389143 INR
> - 2025-01-05: 480.819166 INR
> - 2025-01-06: 485.848273 INR
> - 2025-01-07: 489.387143 INR
> - 2025-01-08: 482.803912 INR
> - 2025-01-09: 479.819798 INR
> - 2025-01-10: 481.154509 INR
> - 2025-01-11: 485.647189 INR
> - 2025-01-12: 478.185788 INR
> - 2025-01-13: 485.684977 INR
> - 2025-01-14: 482.779958 INR
> - 2025-01-15: 483.553636 INR
> - 2025-01-16: 471.914168 INR
> - 2025-01-17: 484.257972 INR
> - 2025-01-18: 486.231545 INR
> - 2025-01-19: 485.631558 INR
> - 2025-01-20: 481.019991 INR
> - 2025-01-21: 483.750477 INR
> - 2025-01-22: 491.374955 INR
> - 2025-01-23: 486.848540 INR
> - 2025-01-24: 477.788653 INR
> - 2025-01-25: 487.047706 INR
> - 2025-01-26: 482.561624 INR
> - 2025-01-27: 479.759209 INR
> - 2025-01-28: 475.188469 INR
> - 2025-01-29: 480.258148 INR
> - 2025-01-30: 487.754803 INR
> - 2025-01-31: 487.824038 INR
> - 2025-02-01: 486.622148 INR
> - 2025-02-02: 482.245263 INR
> - 2025-02-03: 487.167723 INR
> - 2025-02-04: 484.405299 INR
> - 2025-02-05: 484.431511 INR
> - 2025-02-06: 480.718921 INR
> - 2025-02-07: 475.587405 INR
> - 2025-02-08: 479.040489 INR
> - 2025-02-09: 486.135705 INR
>
> Population: All orders recorded in INR during 2025, grouped by order date. Unit: INR per order. Each value is the average sales amount per order for that date. Interpretation: AOV in INR fluctuated daily, generally between 471.914168 and 491.374955 INR in the first 40 days of 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> The Average Order Value (AOV) in INR for each recorded order date in 2025 ranged from approximately 471.914168 INR to 491.374955 INR per order. For example, on 2025-01-01 the AOV was 478.400146 INR, and on 2025-01-22 it was 491.374955 INR. These values represent the daily average sales amount per order, considering only orders recorded in INR currency during 2025. Each value is calculated as the total sales amount divided by the number of orders for that day. This provides insight into daily customer spending patterns on the platform in INR for the specified period.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> The average order value (AOV) in INR for each recorded order date in 2025 ranged from 471.914168 INR to 491.374955 INR. For example, on 2025-01-01, the AOV was 478.400146 INR, and on 2025-01-22, it was 491.374955 INR. These values represent the daily average sales amount per order, calculated as total sales amount divided by the number of orders for each day, considering only orders in INR currency. The population is all orders recorded in INR during 2025, grouped by order date. Units are INR per order. Interpretation: AOV in INR was relatively stable day-to-day, with minor fluctuations, indicating consistent customer spending patterns per order in 2025.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> In 2025, the average order value (AOV) in INR for delivered orders by recorded order date (monthly) was as follows (unit: INR per delivered order):
>
> - January: 483.318741
> - February: 481.863518
> - March: 482.933761
> - April: 483.233983
> - May: 482.613379
> - June: 484.832999
> - July: 482.167711
> - August: 482.512671
> - September: 482.629853
> - October: 483.656178
> - November: 482.374919
> - December: 483.047144
>
> Population: All delivered orders in INR currency, grouped by recorded order date (month) in 2025. Interpretation: The AOV remained stable throughout the year, ranging from approximately 481.86 to 484.83 INR per delivered order. Only delivered orders are included, as per the metric definition. Other order statuses (Cancelled, Refunded) have no AOV value.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For delivered orders in 2025 with currency INR, the average order value (AOV) by recorded order date ranged from approximately 473.444666 to 490.374065 INR per delivered order (first 40 days shown). For example, on 2025-01-01, AOV was 478.891045 INR; on 2025-01-15, it was 483.859289 INR; and on 2025-02-09, it was 484.597208 INR. Each value represents the mean sales amount per delivered order for that day, in INR. The population is all delivered orders with INR currency on each date. Units: INR per delivered order. Interpretation: This shows daily variation in average delivered order value in INR for the first 40 days of 2025.

</details>


## Q04

**Pertanyaan:** What was the cancellation rate, as a percentage, during 2025, by recorded order date?

**Kunci dan cakupan:**

**Reference answer:** **5.9970094773%.** Divide **261,456 Cancelled orders** by **4,359,773 total orders** and multiply by 100. Tolerance: ±0.01 percentage point.

**Scope check:** All recorded 2025 orders in the denominator, across statuses and currencies.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Returned daily rates instead of annual cancellation rate |
| B | ✗ | Returned daily rates instead of annual cancellation rate |
| C | ✗ | Returned daily rates instead of annual cancellation rate |
| D | ✗ | Returned daily rates instead of annual cancellation rate |
| E | ✗ | Daily rates instead of annual cancellation rate |
| F | ✗ | Returned monthly rates instead of annual cancellation rate |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the cancellation rate by recorded order date ranged from approximately 5.614554% to 6.449646% per day. For example, on 2025-01-01, there were 529 cancelled orders out of 8,202 total orders, resulting in a cancellation rate of 6.449646%. On 2025-01-10, the rate was 5.614554% (645 cancelled out of 11,488 total). Across the first 40 days of 2025, daily cancellation rates consistently hovered around 6%, with minor fluctuations. This means that, on average, about 6 out of every 100 orders placed each day were cancelled. All rates are calculated as (cancelled orders / total orders) * 100, with at least six decimals retained for precision. Population: all recorded orders per day in 2025. Unit: percent. Interpretation: The cancellation rate was stable and did not show extreme daily variation in early 2025.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the cancellation rate by recorded order date ranged from approximately 5.614554% to 6.449646% for the first 40 days of the year. For example, on 2025-01-01, there were 529 cancelled orders out of 8,202 total orders, resulting in a cancellation rate of 6.449646%. On 2025-01-10, the rate was 5.614554% (645 cancelled out of 11,488 total). The daily cancellation rate generally fluctuated between about 5.6% and 6.4%. These rates are calculated as (cancelled orders / total orders) * 100 for each day, and represent the percentage of orders cancelled on each recorded order date in 2025. Unit: percent. Population: all recorded orders per day in 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the cancellation rate by recorded order date ranged from approximately 5.614554% to 6.449646% per day. For example, on 2025-01-01, there were 8,202 total orders and 529 cancellations, resulting in a cancellation rate of 6.449646%. On 2025-01-10, the rate was 5.614554% (645 cancellations out of 11,488 orders). Across the first 40 days of 2025, daily cancellation rates consistently hovered around 6%, indicating a relatively stable pattern. All rates are percentages, calculated as (cancelled orders / total orders) * 100, with the population being all recorded orders per day in 2025.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the cancellation rate by recorded order date ranged from approximately 5.614554% to 6.449646% for the first 40 days of the year. For example, on 2025-01-01, there were 529 cancelled orders out of 8,202 total orders, resulting in a cancellation rate of 6.449646%. On 2025-01-10, the rate was 5.614554% (645 cancelled out of 11,488 total). This means that, on average, about 6% of orders were cancelled each day during this period. The population for each date is all orders recorded on that date, and the unit is percentage of orders cancelled. Interpretation: The daily cancellation rate was relatively stable, with minor fluctuations, indicating consistent customer or operational behavior regarding cancellations in early 2025.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> The cancellation rate, as a percentage, during 2025 by recorded order date ranged from approximately 5.614554% to 6.449646% for the first 40 days of the year. For example, on 2025-01-01 the cancellation rate was 6.449646%, and on 2025-01-10 it was 5.614554%. Each value represents the percentage of orders cancelled out of all orders placed on that specific date. The population is all orders recorded on each day in 2025 (up to the first 40 days shown). Unit: percent (%). Interpretation: On each day, about 5.6% to 6.4% of orders were cancelled, with minor daily variation.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> The cancellation rate by recorded order month in 2025 ranged from 5.935521% to 6.054661%. Here are the monthly rates (percentage of cancelled orders out of all orders, by recorded order date):
>
> - January: 6.054661%
> - February: 5.982108%
> - March: 6.015661%
> - April: 5.935521%
> - May: 5.970466%
> - June: 6.042513%
> - July: 5.971998%
> - August: 5.989002%
> - September: 5.948973%
> - October: 6.047414%
> - November: 6.047333%
> - December: 5.957408%
>
> Population: All recorded orders in 2025, grouped by their recorded order date (month). Unit: percentage of orders cancelled. Interpretation: Each value is the percentage of orders cancelled in that month, not cumulative or daily. The rate is stable across months, with minor fluctuations.

</details>


## Q05

**Pertanyaan:** What was ordered quantity per order during 2025, by recorded order date? Report units per order.

**Kunci dan cakupan:**

**Reference answer:** **2.80539307895 units per order.** Divide **12,230,877 item units** by **4,359,773 total orders**. Sum item `quantity`; do not count item lines or average daily ratios. Tolerance: ±0.01 unit per order.

**Scope check:** All recorded 2025 orders in the denominator, across statuses and currencies.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Daily quantity per order instead of annual ratio of totals |
| B | ✗ | Returned daily quantity per order instead of annual ratio of totals |
| C | ✗ | Daily quantity per order instead of annual ratio of totals |
| D | ✗ | Daily quantity per order instead of annual ratio of totals |
| E | ✗ | Monthly units per order instead of annual ratio of totals |
| F | ✗ | Daily truncated values instead of annual units per order |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the average ordered quantity per order (units per order) by recorded order date ranged from approximately 2.775121 to 2.839170 units per order. For example, on 2025-01-01, the average was 2.791270 units per order, and on 2025-01-31, it was 2.839170 units per order. These values represent the mean number of items ordered per order for each date, based on all orders recorded on that date. The population is all orders placed on each respective date in 2025. Units are 'units per order'.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the average ordered quantity per order (units per order) by recorded order date ranged from approximately 2.775121 to 2.839170 units per order. For example, on 2025-01-01, the average was 2.791270 units per order, and on 2025-01-31, it was 2.839170 units per order. This metric was calculated for each day using all orders recorded on that date. The population is all orders with a recorded order date in 2025. Units are average items (units) per order per day. Interpretation: The typical order in 2025 contained about 2.8 items, with minor daily variation.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the average ordered quantity per order (units per order) by recorded order date ranged from approximately 2.775121 to 2.839170 units per order. For example, on 2025-01-01, the average was 2.791270 units per order, and on 2025-01-31, it was 2.839170 units per order. This metric was calculated for each day using all orders recorded on that date. The population is all orders with a recorded order date in 2025. Units are food items per order. Interpretation: On each day in 2025, customers ordered on average about 2.8 food items per order, with minor daily variation.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the ordered quantity per order (units per order) by recorded order date ranged from approximately 2.775121 to 2.839170 units per order. For example, on 2025-01-01, the average ordered quantity per order was 2.791270 units, and on 2025-01-31, it was 2.839170 units. This metric was calculated as the total ordered quantity divided by the number of orders for each date. The population is all recorded orders in 2025, and the unit is units per order. This shows that, on average, customers ordered between about 2.78 and 2.84 items per order each day in early 2025.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the ordered quantity per order (units per order) by recorded order date, at monthly grain, was as follows:
>
> - January: 2.807195 units/order
> - February: 2.801279 units/order
> - March: 2.801484 units/order
> - April: 2.807184 units/order
> - May: 2.803475 units/order
> - June: 2.809406 units/order
> - July: 2.804169 units/order
> - August: 2.804950 units/order
> - September: 2.808074 units/order
> - October: 2.807549 units/order
> - November: 2.802478 units/order
> - December: 2.806788 units/order
>
> Population: All recorded orders in 2025. Unit: units per order. Interpretation: On average, each order in 2025 contained between 2.80 and 2.81 items, with minor monthly variation.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> During 2025, the ordered quantity per order (units per order) by recorded order date ranged from approximately 2.775121 to 2.839170 units per order for the first 40 days. For example, on 2025-01-01, the average was 2.791270 units per order, and on 2025-01-31, it was 2.839170 units per order. Each value represents the total ordered item quantity divided by the number of orders for that day. This report covers the first 40 days of 2025 due to row limits; all values are in units per order, by recorded order date.

</details>


## Q06

**Pertanyaan:** In 2025, which month had the highest Delivered-order GMV in INR? Give that month's GMV, the runner-up month's GMV, and the gap between them.

**Kunci dan cakupan:**

**Reference answer — Peak GMV month.**

December 2025: **INR 185,263,071** from 383,530 Delivered orders. Runner-up November: **INR 180,239,871** from 373,651. Gap: **INR 5,023,200**. Rank months by Delivered sales, not all-status sales.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✓ | Correct peak month, runner-up and gap |
| B | ✓ | Correct peak month, runner-up and gap |
| C | ✓ | Correct peak month, runner-up and gap |
| D | ✓ | Correct peak month, runner-up and gap |
| E | ✓ | Correct peak month, runner-up and gap |
| F | ✓ | Correct peak month, runner-up and gap |

<details><summary>Jawaban asli A — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, the month with the highest Delivered-order GMV in INR was December (2025-12) with a GMV of 185,263,071 INR. The runner-up was November (2025-11) with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. Population: all delivered orders in INR in 2025. Units: INR. Interpretation: December 2025 outperformed November 2025 by 5,023,200 INR in delivered-order GMV.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, December had the highest Delivered-order GMV in INR, with a GMV of 185,263,071.00 INR. The runner-up month was November, with a GMV of 180,239,871.00 INR. The gap between them was 5,023,200.00 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation: December outperformed November by 5,023,200.00 INR in delivered-order GMV.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, December had the highest Delivered-order GMV in INR, totaling 185,263,071.00 INR. The runner-up was November, with a Delivered-order GMV of 180,239,871.00 INR. The gap between December and November was 5,023,200.00 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation: December outperformed November by 5,023,200.00 INR in delivered GMV.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, December had the highest Delivered-order GMV in INR, with a GMV of 185,263,071.00 INR. The runner-up was November, with a GMV of 180,239,871.00 INR. The gap between them was 5,023,200.00 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation: December outperformed November by 5,023,200.00 INR in delivered GMV.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, the month with the highest Delivered-order GMV in INR was December, with a GMV of 185,263,071 INR. The runner-up month was November, with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. 
>
> Population: All delivered orders in INR in 2025, grouped by month. 
> Unit: INR (Indian Rupees). 
> Interpretation: December 2025 saw the highest delivered-order sales volume in INR, exceeding November by 5,023,200 INR.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, December had the highest Delivered-order GMV in INR, with a GMV of 185,263,071 INR. The runner-up month was November, with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. 
>
> Population: All delivered orders in INR in 2025, grouped by order month. 
> Unit: INR (Indian Rupees). 
> Interpretation: December 2025 saw the highest delivered-order sales volume, exceeding November by 5,023,200 INR.

</details>


## Q07

**Pertanyaan:** Compare January and December 2025 in INR: Delivered order count, GMV, and AOV for each month. Which grew faster from January to December, Delivered order count or AOV, in percentage terms?

**Kunci dan cakupan:**

**Reference answer — January vs December.**

January: 286,712 Delivered orders, INR 138,573,283 GMV, INR 483.31874145 AOV. December: 383,530, INR 185,263,071, INR 483.04714364. Order count rose **33.7684%**; AOV fell **0.0562%**. Count grew faster. Percent changes use January as denominator.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Unnecessary clarification of parseable order-date strings |
| B | ✗ | Incorrect January-to-December order-count growth percentage |
| C | ✗ | Incorrect January-to-December order-count growth percentage |
| D | ✗ | Incorrect January-to-December order-count growth percentage |
| E | ✗ | Incorrect January-to-December order-count growth percentage |
| F | ✗ | Incorrect January-to-December order-count growth percentage |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> The ORDER_DATE column in ZOMATO_DLR.SOURCES.ORDERS appears to be stored as a VARCHAR, not a DATE, so extracting the month for January and December 2025 is not possible without knowing the exact string format. Please clarify the string format of ORDER_DATE (e.g., 'YYYY-MM-DD'), or provide a business rule for parsing months from this field.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For delivered orders in INR:
>
> - January 2025:
>   - Delivered order count: 286,712
>   - GMV: 138,573,283 INR
>   - AOV: 483.318741 INR
>
> - December 2025:
>   - Delivered order count: 383,530
>   - GMV: 185,263,071 INR
>   - AOV: 483.047144 INR
>
> Growth from January to December 2025:
> - Delivered order count: ((383,530 - 286,712) / 286,712) = 33.7326% increase
> - AOV: ((483.047144 - 483.318741) / 483.318741) = -0.0562% decrease
>
> Interpretation: Delivered order count grew much faster (33.7326% increase) than AOV (which slightly decreased by 0.0562%) from January to December 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> For delivered orders in INR:
> - January 2025: Delivered order count = 286,712; GMV = 138,573,283 INR; AOV = 483.318741 INR
> - December 2025: Delivered order count = 383,530; GMV = 185,263,071 INR; AOV = 483.047144 INR
>
> Growth from January to December 2025:
> - Delivered order count grew by ((383,530 - 286,712) / 286,712) * 100 = 33.719857%.
> - AOV changed by ((483.047144 - 483.318741) / 483.318741) * 100 = -0.056255% (a slight decrease).
>
> Interpretation: Delivered order count grew much faster (33.72% increase) than AOV (which slightly decreased by 0.06%) from January to December 2025.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> For January 2025 (INR):
> - Delivered order count: 286,712
> - GMV: 138,573,283.00 INR
> - AOV: 483.318741 INR
>
> For December 2025 (INR):
> - Delivered order count: 383,530
> - GMV: 185,263,071.00 INR
> - AOV: 483.047144 INR
>
> Growth from January to December 2025:
> - Delivered order count grew by ((383,530 - 286,712) / 286,712) * 100 = 33.719% (rounded to six decimals: 33.719047%)
> - AOV changed by ((483.047144 - 483.318741) / 483.318741) * 100 = -0.056% (rounded to six decimals: -0.056220%)
>
> Interpretation: Delivered order count grew much faster (33.719047%) than AOV, which slightly decreased (-0.056220%) from January to December 2025 in INR.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> For INR orders in 2025:
>
> - January 2025:
>   - Delivered order count: 286,712
>   - GMV: 138,573,283 INR
>   - AOV: 483.318741 INR
>
> - December 2025:
>   - Delivered order count: 383,530
>   - GMV: 185,263,071 INR
>   - AOV: 483.047144 INR
>
> Growth from January to December:
> - Delivered order count: ((383,530 - 286,712) / 286,712) × 100% = 33.754% increase
> - AOV: ((483.047144 - 483.318741) / 483.318741) × 100% = -0.056% decrease
>
> Interpretation:
> Delivered order count grew much faster (33.754% increase) than AOV (which slightly decreased by 0.056%) from January to December 2025 in INR. The growth in GMV is primarily driven by the increase in delivered order volume, not by higher average order values.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For INR orders in 2025:
>
> - January 2025:
>   - Delivered order count: 286,712
>   - GMV: 138,573,283 INR
>   - AOV: 483.318741 INR
>
> - December 2025:
>   - Delivered order count: 383,530
>   - GMV: 185,263,071 INR
>   - AOV: 483.047144 INR
>
> Growth from January to December:
> - Delivered order count: ((383,530 - 286,712) / 286,712) * 100% = 33.732% increase
> - AOV: ((483.047144 - 483.318741) / 483.318741) * 100% = -0.056% decrease
>
> Interpretation:
> Delivered order count grew by 33.732% from January to December 2025, while AOV slightly decreased by 0.056%. Therefore, delivered order count grew much faster than AOV in percentage terms over this period.

</details>


## Q08

**Pertanyaan:** For 2025, list the top three order-recorded cities by Delivered-order GMV in INR. For each city, also show Delivered order count and AOV. Treat each exact city label as one city.

**Kunci dan cakupan:**

**Reference answer — Top order cities.**

In descending GMV order:

| Order city | Delivered orders | GMV INR | AOV INR |
| --- | ---: | ---: | ---: |
| Bangalore | 440,743 | 233,341,258 | 529.42703117 |
| Delhi | 339,384 | 177,702,873 | 523.60415635 |
| Chennai | 310,963 | 155,055,243 | 498.62923563 |

These are **order-recorded** cities, as requested; no restaurant-city substitution.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Wrong order-city ranking and values |
| B | ✓ | Correct top three order cities and all values |
| C | ✓ | Top three exact order cities and all values correct |
| D | ✓ | Correct top three order cities and all values |
| E | ✓ | Top three exact order cities and all values correct |
| F | ✓ | Correct top three order cities and all values after tool retries |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bikaner: Delivered GMV = 29,030,997 INR, Delivered order count = 49,057, AOV = 591.780928 INR
> 2. Indiranagar,Bangalore: Delivered GMV = 22,092,650 INR, Delivered order count = 36,998, AOV = 597.130926 INR
> 3. Koramangala,Bangalore: Delivered GMV = 18,686,823 INR, Delivered order count = 30,450, AOV = 613.688768 INR
>
> Population: All orders recorded in 2025 with ORDER_STATUS = 'Delivered' and CURRENCY = 'INR', grouped by exact city label. Units: GMV and AOV in INR, order count as integer. Interpretation: These cities had the highest delivered order sales volume in INR for 2025, with AOV representing the average value per delivered order in each city.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bangalore: Delivered GMV = 233,341,258 INR, Delivered order count = 440,743, AOV = 529.427031 INR
> 2. Delhi: Delivered GMV = 177,702,873 INR, Delivered order count = 339,384, AOV = 523.604156 INR
> 3. Chennai: Delivered GMV = 155,055,243 INR, Delivered order count = 310,963, AOV = 498.629236 INR
>
> Population: All delivered orders in 2025 with currency INR, grouped by exact city label. Units: GMV and AOV in INR, order count as integer. Interpretation: Bangalore led in delivered GMV, order count, and had the highest average order value among the top three cities.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bangalore: Delivered GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
> 2. Delhi: Delivered GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
> 3. Chennai: Delivered GMV = 155,055,243.00 INR, Delivered order count = 310,963, AOV = 498.629236 INR
>
> Population: All delivered orders in 2025 with currency INR, grouped by exact city label. Units: INR for GMV and AOV, count for orders. Interpretation: Bangalore led in delivered GMV, order count, and had the highest average order value among the top three cities.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bangalore: Delivered GMV = 233,341,258 INR, Delivered order count = 440,743, AOV = 529.427031 INR
> 2. Delhi: Delivered GMV = 177,702,873 INR, Delivered order count = 339,384, AOV = 523.604156 INR
> 3. Chennai: Delivered GMV = 155,055,243 INR, Delivered order count = 310,963, AOV = 498.629236 INR
>
> Population: All delivered orders in 2025 with currency INR, grouped by exact city label. Units: GMV and AOV in INR, order count as integer. Interpretation: Bangalore led in delivered GMV and order count, with the highest average order value among the top three cities.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bangalore: GMV = 233,341,258.00 INR, Delivered Order Count = 440,743, AOV = 529.427031 INR
> 2. Delhi: GMV = 177,702,873.00 INR, Delivered Order Count = 339,384, AOV = 523.604156 INR
> 3. Chennai: GMV = 155,055,243.00 INR, Delivered Order Count = 310,963, AOV = 498.629236 INR
>
> Each city is treated as a distinct label. GMV is the total delivered sales amount in INR, Delivered Order Count is the number of delivered orders, and AOV is the average order value for delivered orders in INR. All values are for orders recorded in 2025.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:
>
> 1. Bangalore: GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
> 2. Delhi: GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
> 3. Chennai: GMV = 155,055,243.00 INR, Delivered order count = 310,963, AOV = 498.629236 INR
>
> Each city is treated as a distinct label based on the order-recorded city field. GMV is the sum of delivered order sales amounts in INR. Delivered order count is the number of delivered orders. AOV (Average Order Value) is the average sales amount per delivered order. All values are for the 2025 calendar year and in INR. Interpretation: Bangalore led in both delivered GMV and order count, with the highest AOV among the top three cities.

</details>


## Q09

**Pertanyaan:** Among order-recorded cities with at least 50,000 total orders in 2025, which had the highest cancellation rate? Give its order count, cancellation rate, and gap versus the overall 2025 cancellation rate in percentage points.

**Kunci dan cakupan:**

**Reference answer — Highest eligible city cancellation rate.**

Hyderabad: **319,122 orders**, 19,236 Cancelled, **6.027789%** cancellation. Overall: **5.997009%**. Gap: **+0.030780 percentage points**. Restrict ranking to order cities with at least 50,000 orders.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Wrong city and zero cancellation rates |
| B | ✓ | Correct city, count, rates and percentage-point gap |
| C | ✗ | Wrong city, cancellation rate and overall rate |
| D | ✗ | Wrong highest-cancellation city and overall rate |
| E | ✓ | Correct city and rates; final interpretation imprecisely says large-city average, but SQL and stated overall rate use all orders |
| F | ✓ | Correct city, count, rate and percentage-point gap |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> Among cities with at least 50,000 total orders recorded in 2025, Bikaner had the highest cancellation rate. Bikaner had 53,571 orders and a cancellation rate of 0.000000 (0/53,571). The overall 2025 cancellation rate was also 0.000000 (0/4,359,773). The gap versus the overall 2025 cancellation rate is 0.00 percentage points. Interpretation: In 2025, there were no cancelled orders recorded in either Bikaner or overall, so the cancellation rate and the gap are both zero.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> Among cities with at least 50,000 total orders in 2025, Hyderabad had the highest cancellation rate. 
>
> - City: Hyderabad
> - Order count: 319,122
> - Cancellation rate: 0.060278 (6.0278%)
> - Overall 2025 cancellation rate: 0.059970 (5.9970%)
> - Gap vs overall: 0.060278 - 0.059970 = 0.000308, or 0.0308 percentage points higher than the overall rate.
>
> Interpretation: In 2025, Hyderabad had the highest cancellation rate among large cities, with a rate 0.0308 percentage points above the overall average for all cities with recorded orders.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> Among cities with at least 50,000 total orders in 2025, Bangalore had the highest cancellation rate.
>
> - City: Bangalore
> - Order count: 481,626
> - Cancellation rate: 0.059857 (5.9857%)
> - Overall 2025 cancellation rate: 0.059983 (5.9983%)
> - Gap vs overall: -0.0126 percentage points (Bangalore's rate is 0.0126 points lower than the overall rate)
>
> Interpretation: Although Bangalore had the highest cancellation rate among large cities, its rate was actually slightly below the overall 2025 average for all cities.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> Among cities with at least 50,000 total orders in 2025, Chennai had the highest cancellation rate. 
>
> - City: Chennai
> - Order count: 339,941 orders
> - Cancellation rate: 0.060154 (20,442 cancelled / 339,941 total)
> - Overall 2025 cancellation rate: 0.059983 (261,456 cancelled / 4,359,773 total)
> - Gap versus overall: 0.0171 percentage points higher (0.060154 - 0.059983 = 0.000171, or 0.0171%)
>
> Interpretation: Chennai's cancellation rate in 2025 was slightly above the overall average for all cities, by 0.0171 percentage points, among cities with at least 50,000 orders.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> Among order-recorded cities with at least 50,000 total orders in 2025, Hyderabad had the highest cancellation rate. Hyderabad had 319,122 orders and a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate was 0.059970 (5.9970%). The gap between Hyderabad's cancellation rate and the overall rate is 0.000308, or 0.0308 percentage points. Interpretation: Hyderabad's cancellation rate was slightly above the overall average for large cities in 2025.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> Among order-recorded cities with at least 50,000 total orders in 2025, Hyderabad had the highest cancellation rate. Hyderabad had 319,122 total orders and a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate across all cities was 0.059970 (5.9970%). The gap between Hyderabad's cancellation rate and the overall rate is 0.0308 percentage points (6.0278% - 5.9970%).

</details>


## Q10

**Pertanyaan:** For Delivered orders in 2025 with a recorded delivery duration, compare the average delivery time in order-recorded Bangalore and Delhi. Which city was slower, and by how many minutes?

**Kunci dan cakupan:**

**Reference answer — Delivery time.**

Bangalore: 440,743 non-null Delivered durations, **31.0560894 min** average. Delhi: 339,384, **31.0484820 min**. Bangalore is slower by **0.0076074 min**, about **0.46 sec**. Do not average Cancelled/Refunded orders.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Falsely reported no recorded delivery durations |
| B | ✓ | Correct delivery means and gap |
| C | ✓ | Correct delivery means and gap |
| D | ✓ | Correct delivery means and gap |
| E | ✓ | Correct delivery means and gap |
| F | ✓ | Correct delivery means and gap |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> There are no delivered orders in 2025 with a recorded delivery duration for either Bangalore or Delhi in the available data. Therefore, it is not possible to compare the average delivery time between these cities for the specified period.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> For delivered orders in 2025 with a recorded delivery duration, the average delivery time in Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small and likely not operationally significant. Population: 440,743 orders in Bangalore, 339,384 in Delhi. Unit: minutes. Interpretation: Both cities had nearly identical average delivery times for delivered orders in 2025 with recorded delivery duration.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For delivered orders in 2025 with a recorded delivery duration, the average delivery time in Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is very small, but Bangalore had the slightly higher average delivery time.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, for delivered orders with a recorded delivery duration, Bangalore had an average delivery time of 31.056089 minutes, while Delhi had an average of 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is very small, but Bangalore was marginally slower.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> For delivered orders in 2025 with a recorded delivery duration, the average delivery time in Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small and likely not operationally significant.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> For Delivered orders in 2025 with a recorded delivery duration, the average delivery time in order-recorded Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small and likely not operationally significant.

</details>


## Q11

**Pertanyaan:** For each recorded order status in 2025, report total orders, the share with a non-null customer rating, and average customer rating among rated orders. What population does each average describe?

**Kunci dan cakupan:**

**Reference answer — Ratings by status.**

| Status | Orders | Rated | Coverage | Mean among rated |
| --- | ---: | ---: | ---: | ---: |
| Cancelled | 261,456 | 0 | 0% | undefined |
| Delivered | 3,989,077 | 2,793,569 | 70.030461% | 4.14547985 |
| Refunded | 109,240 | 0 | 0% | undefined |

The average is over **rated orders within that status**, not all orders. Zero rated observations make the average undefined, not zero.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✓ | All status counts, coverage and rated-only means correct |
| B | ✓ | All status counts, coverage and rated-only means correct |
| C | ✓ | All status counts, coverage and rated-only means correct |
| D | ✓ | All status counts, coverage and rated-only means correct |
| E | ✓ | All status counts, coverage and rated-only means correct |
| F | ✓ | All status counts, coverage and rated-only means correct |

<details><summary>Jawaban asli A — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders; 70.0305% had a non-null customer rating; average customer rating among rated orders was 4.145480. This average describes only the subset of delivered orders in 2025 where a customer rating was provided (2,793,569 orders).
> - Cancelled: 261,456 total orders; 0% had a customer rating; no average rating (none rated).
> - Refunded: 109,240 total orders; 0% had a customer rating; no average rating (none rated).
>
> Each average customer rating describes only those orders of the given status in 2025 that received a non-null customer rating, not all orders of that status.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders; 70.030461% had a non-null customer rating; average customer rating among rated orders was 4.145480. This average describes only the subset of delivered orders in 2025 where a customer rating was provided (2,793,569 orders).
> - Cancelled: 261,456 total orders; 0% had a non-null customer rating; no average rating (none rated).
> - Refunded: 109,240 total orders; 0% had a non-null customer rating; no average rating (none rated).
>
> Each average customer rating describes only those orders of the given status in 2025 that received a non-null customer rating, not all orders of that status.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders; 70.030500% had a non-null customer rating; the average customer rating among rated orders was 4.14547985.
> - Cancelled: 261,456 total orders; 0% had a non-null customer rating; no average rating (none rated).
> - Refunded: 109,240 total orders; 0% had a non-null customer rating; no average rating (none rated).
>
> Each average customer rating describes only those orders with a non-null customer rating for the given order status (e.g., for 'Delivered', the average is among the 2,793,569 rated delivered orders in 2025).

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders; 70.0305% had a non-null customer rating; average customer rating among rated orders was 4.14547985.
> - Cancelled: 261,456 total orders; 0% had a customer rating; no average rating (none rated).
> - Refunded: 109,240 total orders; 0% had a customer rating; no average rating (none rated).
>
> Each average customer rating describes only those orders with the given status in 2025 that have a non-null customer rating (i.e., rated orders for that status). For example, the average for 'Delivered' is among the 2,793,569 delivered orders with a rating.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders. 70.030461% of these had a non-null customer rating. The average customer rating among rated delivered orders was 4.14547985. This average describes only those delivered orders in 2025 that received a numeric customer rating.
> - Refunded: 109,240 total orders. 0.0% had a non-null customer rating. No average rating is reported, as there were no rated refunded orders.
> - Cancelled: 261,456 total orders. 0.0% had a non-null customer rating. No average rating is reported, as there were no rated cancelled orders.
>
> Population for each average: For each order status, the average customer rating describes only those orders of that status in 2025 that received a numeric customer rating (if any).

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> For each recorded order status in 2025:
>
> - Delivered: 3,989,077 total orders; 70.030461% had a non-null customer rating; the average customer rating among rated Delivered orders was 4.14547985.
> - Refunded: 109,240 total orders; 0.0% had a non-null customer rating; no average rating is reported.
> - Cancelled: 261,456 total orders; 0.0% had a non-null customer rating; no average rating is reported.
>
> Population for each average: The average customer rating describes only those orders with the given status (e.g., Delivered) that have a non-null customer rating. For example, the Delivered average is calculated from the 70.03% of Delivered orders in 2025 that received a customer rating, not all Delivered orders or all orders overall.

</details>


## Q12

**Pertanyaan:** What share of 2025 Delivered-order GMV in INR came from the top ten restaurants ranked by that same GMV? Rank by restaurant ID when GMV ties, and report both top-ten and total GMV.

**Kunci dan cakupan:**

**Reference answer — Top-ten restaurant concentration.**

Top ten restaurant IDs contribute **INR 3,552,103** of **INR 1,926,466,048** total Delivered GMV: **0.18438441%**. Rank by restaurant GMV descending, then restaurant ID for ties.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Incorrect top-ten GMV and share |
| B | ✗ | Top-ten GMV arithmetic wrong: 3,552,107 instead of 3,552,103 |
| C | ✗ | Top-ten GMV arithmetic wrong: 3,542,107 |
| D | ✓ | Correct top-ten GMV, denominator, share and tie-break query |
| E | ✗ | Contradictory and incorrect share claims, including 1.84% |
| F | ✗ | Top-ten GMV arithmetic wrong despite correct restaurant query |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> The top ten restaurants by 2025 Delivered-order GMV in INR (ranked by GMV, then restaurant ID) generated a combined GMV of 3,252,107.0 INR. The total 2025 Delivered-order GMV in INR across all restaurants was 1,926,466,048.0 INR. Therefore, the top ten restaurants contributed 0.168810% of the total GMV (share = 0.001688).

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 delivered orders in INR:
> - The top ten restaurants by delivered GMV (ranked by GMV, then by restaurant ID in case of ties) generated a combined delivered GMV of 3,552,107.00 INR.
> - The total delivered GMV in INR for all restaurants was 1,926,466,048.00 INR.
> - The share of delivered GMV from the top ten restaurants was 0.001844 (or 0.1844%).
>
> Interpretation: The top ten restaurants contributed only about 0.18% of the total delivered GMV in INR for 2025, indicating a highly distributed sales landscape where no small group of restaurants dominates the delivered GMV.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 delivered orders in INR, the top ten restaurants by delivered GMV (ranked by GMV, then restaurant ID) generated a combined GMV of 3,542,107.00 INR. The total delivered GMV in INR for all restaurants in 2025 was 1,926,466,048.00 INR. Thus, the share of delivered GMV from the top ten restaurants was 0.001838 (or 0.1838%). This indicates that the top ten restaurants contributed a very small fraction of the total delivered GMV in INR for 2025.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, the top ten restaurants by delivered-order GMV in INR contributed a total of 3,552,103.00 INR out of a total delivered-order GMV of 1,926,466,048.00 INR. This means the top ten restaurants accounted for 0.00184384 (or 0.184384%) of the delivered-order GMV in INR. The population is all delivered orders in INR in 2025, and the unit is INR. The share is calculated as the top ten's GMV divided by the total GMV. This indicates that the delivered-order GMV is highly distributed across many restaurants, with the top ten contributing less than 0.2% of the total.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> In 2025, the top ten restaurants (ranked by delivered-order GMV in INR, breaking ties by restaurant ID) contributed INR 3,552,103.00 to the delivered-order GMV. The total delivered-order GMV in INR for all restaurants was INR 1,926,466,048.00. This means the top ten restaurants accounted for approximately 0.184478 (or 0.0184478, i.e., 1.84%) of the total delivered-order GMV in INR. 
>
> - Top ten GMV (INR): 3,552,103.00
> - Total GMV (INR): 1,926,466,048.00
> - Share: 0.00184478 (0.184478%)
>
> Interpretation: The top ten restaurants contributed a very small share (less than 0.2%) of the total delivered-order GMV in INR in 2025, indicating a highly distributed sales landscape across many restaurants.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, the top ten restaurants by Delivered-order GMV in INR (ranked by GMV, then restaurant ID) generated a combined GMV of 3,552,107 INR. The total Delivered-order GMV in INR for all restaurants in 2025 was 1,926,466,048 INR. Therefore, the share of GMV from the top ten restaurants was approximately 0.001844 (or 0.1844%).
>
> - Top ten restaurant GMV (INR): 3,552,107
> - Total GMV (INR): 1,926,466,048
> - Share: 0.001844 (unitless ratio, or 0.1844%)
>
> Interpretation: The top ten restaurants contributed only about 0.18% of the total Delivered-order GMV in INR for 2025, indicating a highly distributed sales landscape where no small group of restaurants dominates the market by GMV.

</details>


## Q13

**Pertanyaan:** Which three exact cuisine labels had the highest 2025 Delivered-order GMV in INR? For each label, also give total order count and cancellation rate. Do not split comma-separated cuisine labels.

**Kunci dan cakupan:**

**Reference answer — Cuisine labels.**

Treat comma-separated strings as exact labels.

| Exact label | Total orders | Cancel rate | Delivered GMV INR |
| --- | ---: | ---: | ---: |
| North Indian,Chinese | 202,651 | 5.880060% | 97,195,380 |
| Indian,Chinese | 126,766 | 5.981888% | 60,447,386 |
| Indian | 148,932 | 6.000054% | 58,362,786 |

Cancellation denominators include every order in each exact cuisine label.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Limited cancellation counts to Delivered orders |
| B | ✗ | Cancellation denominators wrongly limited to Delivered orders |
| C | ✗ | Cancellation denominators wrongly limited to Delivered orders |
| D | ✓ | Exact cuisine labels, counts and GMV correct; cancellation rates within revised ±0.01 percentage-point tolerance |
| E | ✓ | Exact cuisine labels, all-status counts, GMV and rates correct |
| F | ✓ | Exact cuisine labels, all-status counts, GMV and rates correct |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:
>
> 1. "North Indian,Chinese":
>    - GMV: 97,195,380.00 INR
>    - Total delivered orders: 185,649
>    - Cancellation rate: 0.000000 (no cancellations)
>
> 2. "Indian,Chinese":
>    - GMV: 60,447,386.00 INR
>    - Total delivered orders: 116,036
>    - Cancellation rate: 0.000000 (no cancellations)
>
> 3. "Indian":
>    - GMV: 58,362,786.00 INR
>    - Total delivered orders: 136,184
>    - Cancellation rate: 0.000000 (no cancellations)
>
> Interpretation: In 2025, the top three cuisine labels by delivered-order GMV in INR were all Indian or Indian fusion types, with no cancellations recorded for these delivered orders. The population is all delivered orders in INR in 2025, and the units are INR for GMV, count for orders, and rate for cancellations (six decimals).

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 delivered-order GMV in INR are:
>
> 1. "North Indian,Chinese":
>    - GMV: 97,195,380.00 INR
>    - Total delivered orders: 185,649
>    - Cancellation rate: 0.000000 (0%)
>
> 2. "Indian,Chinese":
>    - GMV: 60,447,386.00 INR
>    - Total delivered orders: 116,036
>    - Cancellation rate: 0.000000 (0%)
>
> 3. "Indian":
>    - GMV: 58,362,786.00 INR
>    - Total delivered orders: 136,184
>    - Cancellation rate: 0.000000 (0%)
>
> Interpretation: For 2025 delivered orders in INR, the top three cuisine labels (not splitting comma-separated values) are all Indian or Indian fusion types, with no cancellations recorded among delivered orders for these cuisines.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:
>
> 1. "North Indian,Chinese":
>    - Delivered GMV: 97,195,380.00 INR
>    - Total delivered orders: 185,649
>    - Cancellation rate: 0.000000 (0%)
>
> 2. "Indian,Chinese":
>    - Delivered GMV: 60,447,386.00 INR
>    - Total delivered orders: 116,036
>    - Cancellation rate: 0.000000 (0%)
>
> 3. "Indian":
>    - Delivered GMV: 58,362,786.00 INR
>    - Total delivered orders: 136,184
>    - Cancellation rate: 0.000000 (0%)
>
> Interpretation: In 2025, the top three cuisine labels by delivered GMV in INR were all Indian or Indian-Chinese combinations, with no cancellations recorded among delivered orders for these cuisines. The population is all delivered orders in INR currency during 2025, and the unit for GMV is INR.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:
>
> 1. North Indian,Chinese
>    - Delivered GMV (INR): 97,195,380.00
>    - Total Order Count: 202,651
>    - Cancellation Rate: 0.058800 (11,916 / 202,651)
>
> 2. Indian,Chinese
>    - Delivered GMV (INR): 60,447,386.00
>    - Total Order Count: 126,766
>    - Cancellation Rate: 0.059832 (7,583 / 126,766)
>
> 3. Indian
>    - Delivered GMV (INR): 58,362,786.00
>    - Total Order Count: 148,932
>    - Cancellation Rate: 0.060011 (8,936 / 148,932)
>
> Population: All 2025 orders in INR, grouped by exact cuisine label (no splitting of comma-separated labels). Units: INR for GMV, count for orders, and cancellation rate as cancelled orders divided by total orders (six decimals). Interpretation: The top three cuisine labels by delivered GMV in INR are all Indian or Indian fusion, with similar cancellation rates just below 6%.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 delivered-order GMV in INR are:
>
> 1. "North Indian,Chinese":
>    - Delivered-order GMV: 97,195,380.00 INR
>    - Total order count: 202,651
>    - Cancellation rate: 0.058801 (5.8801%)
>
> 2. "Indian,Chinese":
>    - Delivered-order GMV: 60,447,386.00 INR
>    - Total order count: 126,766
>    - Cancellation rate: 0.059819 (5.9819%)
>
> 3. "Indian":
>    - Delivered-order GMV: 58,362,786.00 INR
>    - Total order count: 148,932
>    - Cancellation rate: 0.060001 (6.0001%)
>
> Population: All recorded orders in 2025 with currency INR, grouped by exact cuisine label (no splitting of comma-separated values). Units: GMV in INR, order count as integer, cancellation rate as a decimal and percent. Interpretation: These cuisine labels generated the highest delivered-order GMV in INR for 2025, with cancellation rates between 5.88% and 6.00%.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:
>
> 1. North Indian,Chinese: GMV = 97,195,380.00 INR, Total Order Count = 202,651, Cancellation Rate = 0.058801
> 2. Indian,Chinese: GMV = 60,447,386.00 INR, Total Order Count = 126,766, Cancellation Rate = 0.059819
> 3. Indian: GMV = 58,362,786.00 INR, Total Order Count = 148,932, Cancellation Rate = 0.060001
>
> Population: All 2025 orders with currency INR, grouped by exact cuisine label (no splitting of comma-separated values). Units: GMV in INR, order count as integer, cancellation rate as a decimal (six decimals). Interpretation: These cuisine labels generated the highest delivered-order sales in INR for 2025, with cancellation rates between 5.88% and 6.00%.

</details>


## Q14

**Pertanyaan:** For item lines belonging to 2025 orders, compare Veg, Non-Veg, and unknown food classifications: item-line count, ordered units, and each group's share of all ordered units. What is the difference between line count and units here?

**Kunci dan cakupan:**

**Reference answer — Food classification.**

| Class | Item lines | Ordered units | Unit share |
| --- | ---: | ---: | ---: |
| Veg | 7,277,939 | 8,877,759 | 72.584811% |
| Non-Veg | 2,749,222 | 3,353,105 | 27.415082% |
| Unknown | 12 | 13 | 0.000106% |

An item line may contain multiple units. Keep unmatched or null food classifications as Unknown rather than dropping them.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Ordered-unit shares wrong |
| B | ✗ | Ordered-unit shares wrong |
| C | ✗ | Ordered-unit shares wrong |
| D | ✗ | Ordered-unit shares wrong |
| E | ✗ | Ordered-unit shares wrong |
| F | ✗ | Ordered-unit shares wrong |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 order item lines:
>
> - Veg: 7,277,939 item lines, 8,877,759 ordered units, 72.626857% of all ordered units
> - Non-veg: 2,749,222 item lines, 3,353,105 ordered units, 27.444964% of all ordered units
> - Unknown: 12 item lines, 13 ordered units, 0.000106% of all ordered units
>
> Shares are calculated as each group's ordered units divided by the total ordered units (12,230,877).
>
> Difference between line count and units: 'Item-line count' is the number of distinct order item records (each line may represent multiple units of the same food in one order), while 'ordered units' is the total quantity ordered (sum of all units across all lines). Thus, units can exceed line count if customers order more than one of the same item per line.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For item lines in 2025 orders:
>
> - Veg: 7,277,939 item lines, 8,877,759 ordered units, 72.626964 share of all units
> - Non-Veg: 2,749,222 item lines, 3,353,105 ordered units, 27.441964 share of all units
> - Unknown: 12 item lines, 13 ordered units, 0.000106 share of all units
>
> Shares are calculated as each group's ordered units divided by the total (Veg + Non-Veg + Unknown = 12,230,877 units).
>
> Difference between line count and units: 'Item-line count' is the number of distinct item lines (each line is a menu item in an order, regardless of quantity). 'Ordered units' is the sum of quantities ordered across all lines (so if a line is for 3 units of an item, it counts as 1 line but 3 units). Thus, units can exceed lines if customers order multiples of the same item per line.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 order item lines:
>
> - Veg: 7,277,939 item lines, 8,877,759 ordered units, 72.626964 share of all units
> - Non-Veg: 2,749,222 item lines, 3,353,105 ordered units, 27.443012 share of all units
> - Unknown: 12 item lines, 13 ordered units, 0.000106 share of all units
>
> The difference between 'item-line count' and 'ordered units' is that item-line count measures the number of distinct item entries (each line may represent one or more units of a food item in an order), while ordered units sum the total quantity of food items ordered (i.e., the sum of quantities across all item lines). Thus, ordered units can be higher than item-line count if customers order multiple units of the same item per line.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> For item lines in 2025 orders:
>
> - Veg: 7,277,939 item lines, 8,877,759 ordered units, 72.626964 share of all units
> - Non-Veg: 2,749,222 item lines, 3,353,105 ordered units, 27.443012 share of all units
> - Unknown: 12 item lines, 13 ordered units, 0.000106 share of all units
>
> Shares are calculated as each group's ordered units divided by the total (Veg + Non-Veg + Unknown = 12,230,877 units).
>
> Difference between line count and units: 'Item-line count' is the number of distinct order item lines (each line is a menu item in an order), while 'ordered units' is the sum of quantities ordered (some lines may have quantity >1). Thus, units can exceed line count if customers order multiples of the same item per line.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> For item lines belonging to 2025 orders:
>
> - Veg items: 7,277,939 item lines, 8,877,759 ordered units, representing 72.626857% of all ordered units.
> - Non-Veg items: 2,749,222 item lines, 3,353,105 ordered units, representing 27.443099% of all ordered units.
> - Unknown classification: 12 item lines, 13 ordered units, representing 0.000106% of all ordered units.
>
> "Item-line count" is the number of distinct order item rows (each row represents a unique combination of order and food item, regardless of quantity). "Ordered units" is the total quantity of food items ordered (summing the QUANTITY field across all item lines). For example, if a customer orders 3 units of the same food in one order, it counts as 1 item line and 3 ordered units.
>
> Population: All item lines from orders recorded in 2025. Units: counts (item lines, ordered units), percentage share of total ordered units. Interpretation: Veg items dominate both in item-line count and ordered units, with Veg accounting for nearly three-quarters of all units ordered.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For item lines belonging to 2025 orders, the comparison by food classification is as follows:
>
> - Veg: 7,277,939 item lines, 8,877,759 ordered units, representing 72.626857% of all ordered units.
> - Non-Veg: 2,749,222 item lines, 3,353,105 ordered units, representing 27.426964% of all ordered units.
> - Unknown classification: 12 item lines, 13 ordered units, representing 0.000106% of all ordered units.
>
> Total ordered units across all groups: 12,230,877.
>
> **Difference between line count and units:**
> - Item-line count is the number of distinct order item rows (each row may represent one or more units of a food item in an order).
> - Ordered units is the sum of the quantities across all item lines (i.e., the total number of individual food items ordered, regardless of how they are grouped into lines).
>
> Interpretation: Each item line can represent multiple units of a food item. For example, a customer may order 3 units of the same dish in one line, contributing 1 to the line count and 3 to the ordered units. Thus, ordered units will always be greater than or equal to the item-line count.

</details>


## Q15

**Pertanyaan:** In 2025, what share of orders contained more than one item line? Compare average ordered units per order for one-line and multi-line orders; also report orders with no item line separately.

**Kunci dan cakupan:**

**Reference answer — Item lines per order.**

Multiple lines: **3,052,089 orders**, **70.005686%** of all 2025 orders, averaging **3.484769 units/order**. One line: **1,307,684 orders**, **29.994314%**, averaging **1.219753 units/order**. No item line: **0 orders**, average undefined. Denominator for the share is all 4,359,773 orders.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Wrong total and multi-line order counts and averages |
| B | ✓ | Counts and averages correct; 70% is within revised ±0.01 percentage-point tolerance of 70.005686% |
| C | ✗ | Incorrect multi-line share arithmetic |
| D | ✓ | Counts and averages correct; 70.01% is within revised ±0.01 percentage-point tolerance of 70.005686% |
| E | ✓ | Counts and averages correct; 70% is within revised ±0.01 percentage-point tolerance of 70.005686% |
| F | ✗ | Multi-line and one-line shares miscalculated |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> In 2025, there were no orders with zero item lines (all orders had at least one item line). Out of a total of 3,953,773 orders:
>
> - Orders with exactly one item line: 1,307,684 (33.09% of orders), with an average of 1.219753 units per order.
> - Orders with more than one item line: 2,646,089 (66.91% of orders), with an average of 3.234964 units per order (weighted average across multi-line groups).
>
> Interpretation: The majority of 2025 orders (about two-thirds) contained more than one item line, and these multi-line orders had a much higher average number of units ordered per order compared to single-line orders. No orders were found with zero item lines in the data.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, among orders with at least one item line:
>
> - 1,307,684 orders (30.0%) had exactly one item line, with an average of 1.219753 units per order.
> - 3,052,089 orders (70.0%) had more than one item line, with an average of 3.484769 units per order.
> - No orders were found with zero item lines in the data.
>
> Interpretation: The majority of orders (70%) contained multiple item lines, and these orders had a much higher average number of units per order compared to single-line orders. Orders with only one item line were less common and had a lower average quantity per order. No orders were recorded without any item lines in 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> In 2025, there were no orders with zero item lines reported in the data. Out of all orders:
>
> - 1,307,684 orders (about 30%) had exactly one item line, with an average of 1.219753 units ordered per order.
> - 3,052,089 orders (about 70%) had more than one item line, with an average of 3.484769 units ordered per order.
>
> Share of multi-line orders: 3,052,089 / (1,307,684 + 3,052,089) = 0.700482 (70.0482%).
>
> Interpretation: The majority of 2025 orders (about 70%) contained more than one item line, and these multi-line orders had a much higher average number of units per order compared to single-line orders. No orders with zero item lines were found in the data.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, among orders with at least one item line:
>
> - 1,307,684 orders (29.99%) had exactly one item line ("one-line orders").
> - 3,052,089 orders (70.01%) had more than one item line ("multi-line orders").
> - No orders were found with zero item lines in the data provided.
>
> Average ordered units per order:
> - One-line orders: 1.219753 units per order
> - Multi-line orders: 3.484769 units per order
>
> Interpretation: The majority of orders (about 70%) contained multiple item lines, and these multi-line orders had a much higher average number of units ordered per order compared to one-line orders. No orders without item lines were observed in the 2025 data.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> In 2025, all orders had at least one item line (no orders were found with zero item lines). Out of a total of 4,359,773 orders:
>
> - 1,307,684 orders (30.000000%) had exactly one item line.
> - 3,052,089 orders (70.000000%) had multiple item lines.
> - 0 orders (0.000000%) had no item line.
>
> Average ordered units per order:
> - One item line: 1.219753 units per order
> - Multiple item lines: 3.484769 units per order
> - No item line: Not applicable (no such orders)
>
> Interpretation: The majority of orders (70%) contained more than one item line, and these multi-line orders had a much higher average number of ordered units per order (3.484769) compared to single-line orders (1.219753). There were no orders without any item lines in the data for 2025.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> In 2025, all recorded orders (4,359,773) contained at least one item line; there were no orders with zero item lines in the data. 
>
> - Multi-line orders (more than one item line): 3,052,089 orders, which is 70.03% of all orders. The average ordered units per multi-line order was 3.484769.
> - One-line orders (exactly one item line): 1,307,684 orders, which is 29.97% of all orders. The average ordered units per one-line order was 1.219753.
> - Orders with no item line: 0 orders (0.00%).
>
> Interpretation: The vast majority of orders (70%) contained more than one item line, and these orders had a much higher average number of ordered units per order compared to single-line orders. There were no orders without item lines in the 2025 data. All shares are out of the total 4,359,773 orders. Units are in ordered item units per order.

</details>


## Q16

**Pertanyaan:** Among item lines belonging to 2025 orders, how many have a non-zero difference between recorded line amount and price times quantity? Give the signed sum and absolute sum of those differences in INR. Do positive and negative differences offset in this snapshot?

**Kunci dan cakupan:**

**Reference answer — Item amount reconciliation.**

Of **10,027,173** item lines on 2025 orders, **21,466** have a non-zero recorded minus calculated amount. Signed sum: **+INR 23,791**; absolute sum: **INR 23,791**. These two sums are equal in this snapshot, so negative differences do not offset positive differences here. Do not call either amount a verified corrected value.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✓ | Correct item reconciliation values and interpretation |
| B | ✗ | Wrong count of lines with nonzero amount difference |
| C | ✓ | All requested reconciliation values and interpretation correct |
| D | ✗ | Missed nonzero line-amount differences |
| E | ✓ | Correct item reconciliation values and interpretation |
| F | ✓ | All requested reconciliation values and interpretation correct |

<details><summary>Jawaban asli A — ✓ benar</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders in INR, there are 21,466 item lines where the recorded line amount differs from price times quantity. The signed sum of these differences is 23,791.0 INR, and the absolute sum is also 23,791.0 INR. Since the signed sum and absolute sum are equal, all differences are positive and there is no offset between positive and negative differences in this snapshot.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders in INR, there are 14,321 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. Since the signed sum and absolute sum are equal, all differences are positive and there is no offset between positive and negative differences in this snapshot.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders, there are 21,466 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. Since the signed sum and absolute sum are equal, all differences are positive and there is no offset between positive and negative differences in this snapshot.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders, there are 0 item lines with a non-zero difference between the recorded line amount and price times quantity in INR. Both the signed sum and absolute sum of those differences are null (effectively zero). Therefore, there is no offset between positive and negative differences in this snapshot, as no such differences exist.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders, there are 21,466 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. All differences are positive (21,466 positive, 0 negative), so there is no offset between positive and negative differences in this snapshot. This means every non-zero difference increases the total, with no reductions from negative values.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> Among item lines belonging to 2025 orders, there are 21,466 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. This means all differences are positive in this snapshot—there is no offset between positive and negative differences.

</details>


## Q17

**Pertanyaan:** Does recorded order sales amount reconcile to subtotal minus discount plus delivery fee plus GST for 2025? For each order status, give the count of non-zero differences and their signed sum in INR; do not assume one side is the corrected amount.

**Kunci dan cakupan:**

**Reference answer — Order amount reconciliation.**

Cancelled: 261,456 orders; Delivered: 3,989,077; Refunded: 109,240. **Zero non-zero sales-amount differences and INR 0 signed difference in every status.** Thus the recorded order amount reconciles with the stated arithmetic in this snapshot. This says nothing about payments or refunds actually settled.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Does not report per-status counts and signed sums |
| B | ✗ | Claimed unavailable despite joinable accessible tables |
| C | ✗ | Omitted per-status counts and signed sums |
| D | ✓ | Per-status zero differences and zero sums correct |
| E | ✗ | Omitted per-status counts and signed sums |
| F | ✗ | Omitted per-status counts and signed sums |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, there are no orders in INR currency where the recorded sales amount differs from the calculation (subtotal minus discount plus delivery fee plus GST) for any order status. This means the reconciliation holds exactly for all orders in this period and currency. 
>
> Population: All 2025 orders in INR, grouped by order status.
> Unit: Count (orders), INR (signed sum of differences).
> Interpretation: The sales amount field matches the expected calculation for every order; there are no discrepancies to report.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> A required rule or data is missing: None of the accessible tables have both the recorded SALES_AMOUNT and all the component fields (SUBTOTAL, DISCOUNT, DELIVERY_FEE, GST) together with ORDER_STATUS in a single table or in a way that can be joined without ambiguity. Attempts to join or select from the available tables resulted in SQL errors due to missing or ambiguous fields. Therefore, it is not possible to compute the reconciliation or provide the requested breakdown by order status with the accessible data structure.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> For all 2025 orders in INR, there are no orders with a non-zero difference between the recorded sales amount and the calculation (subtotal minus discount plus delivery fee plus GST) for any order status. This means the recorded sales amount reconciles exactly to the formula for every order status in 2025. Population: all 2025 orders in INR, grouped by order status. Unit: INR. Interpretation: The sales amount calculation is consistent with the component fields for all orders in the specified period and currency.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> For all 2025 orders in INR, the recorded sales amount exactly reconciles to subtotal minus discount plus delivery fee plus GST for every order status. Specifically, for each status (Cancelled, Delivered, Refunded), there are zero orders with a non-zero difference, and the signed sum of differences is 0.00 INR. This indicates perfect agreement between the recorded sales amount and the calculated formula for all orders in the population.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> For all 2025 orders in INR, there are no orders with a non-zero difference between the recorded sales amount and the calculation (subtotal minus discount plus delivery fee plus GST), for any order status. This means the recorded sales amount fully reconciles to the expected calculation across all order statuses in 2025. 
>
> Population: All 2025 orders in INR, grouped by order status.
> Unit: Count of orders, sum of differences in INR.
> Interpretation: The sales amount calculation is consistent and accurate for all order statuses in 2025; no discrepancies were found.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For all 2025 orders in INR, there are no orders with a nonzero difference between the recorded sales amount and the calculated value (subtotal minus discount plus delivery fee plus GST), for any order status. This means the recorded sales amount fully reconciles to the expected calculation for every order status in 2025. 
>
> Population: All 2025 INR orders, grouped by order status.
> Unit: Count of orders and INR (Indian Rupees) for sum of differences.
> Interpretation: No discrepancies were found; the system's recorded sales amounts match the calculated formula for all order statuses in 2025.

</details>


## Q18

**Pertanyaan:** For 2025 Delivered orders in INR, show up to three customer age segments ranked by Delivered order count. Include Delivered order count, GMV, and AOV, using the existing customer dimension's segment labels. If fewer than three segments occur, report only those present.

**Kunci dan cakupan:**

**Reference answer — Customer age segments.**

Only two age segments occur among 2025 Delivered orders:

| Segment | Delivered orders | GMV INR | AOV INR |
| --- | ---: | ---: | ---: |
| Gen Z | 2,222,349 | 1,073,372,395 | 482.99002317 |
| Millennial | 1,766,728 | 853,093,653 | 482.86643615 |

Do not invent a third segment. Use the existing customer dimension labels.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Used numeric ages instead of customer dimension segment labels |
| B | ✗ | Used income-band labels instead of age segments |
| C | ✓ | Both customer age segments and all values correct |
| D | ✓ | Both customer age segments and all values correct |
| E | ✓ | Both customer age segments and all values correct |
| F | ✓ | Both customer age segments and all values correct |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 Delivered orders in INR, the top three customer age segments by Delivered order count are:
>
> 1. Age segment 23: 747,305 Delivered orders, GMV of 361,091,281 INR, and AOV of 483.191309 INR.
> 2. Age segment 22: 590,755 Delivered orders, GMV of 285,775,099 INR, and AOV of 483.745544 INR.
> 3. Age segment 25: 542,236 Delivered orders, GMV of 262,072,908 INR, and AOV of 483.318902 INR.
>
> All values are for Delivered orders in INR currency during 2025. The age segments use the existing customer dimension's segment labels. Only three segments occurred at the top ranks as requested. AOV (Average Order Value) is calculated as GMV divided by Delivered order count for each segment. Units: order count (integer), GMV and AOV (INR, six decimals shown for AOV).

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025 Delivered orders in INR, the top three customer age segments by Delivered order count are:
>
> 1. No Income: 1,912,848 Delivered orders, GMV 924,154,150 INR, AOV 483.129946 INR
> 2. 25001 to 50000: 715,156 Delivered orders, GMV 345,622,936 INR, AOV 483.283278 INR
> 3. More than 50000: 640,580 Delivered orders, GMV 308,862,137 INR, AOV 482.160131 INR
>
> All values are for Delivered orders in INR during 2025. The customer age segments are reported using the existing dimension's segment labels. AOV (Average Order Value) is calculated as GMV divided by Delivered order count for each segment. Only the three segments present with the highest Delivered order counts are shown.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025 delivered orders in INR, the top customer age segments by delivered order count are:
>
> 1. Gen Z: 2,222,349 delivered orders, GMV of 1,073,372,395.00 INR, and AOV (average order value) of 482.990023 INR.
> 2. Millennial: 1,766,728 delivered orders, GMV of 853,093,653.00 INR, and AOV of 482.866436 INR.
>
> Only two age segments had delivered orders in INR for 2025. The population is all delivered orders in INR in 2025, grouped by customer age segment (using the existing segment labels). Units are INR for GMV and AOV, and count for orders. Gen Z had the highest delivered order count, followed by Millennials. No other age segments had delivered orders in INR for 2025.

</details>

<details><summary>Jawaban asli D — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025 delivered orders in INR, the top customer age segments by delivered order count are:
>
> 1. Gen Z: 2,222,349 delivered orders, GMV (Gross Merchandise Value) of 1,073,372,395 INR, and an average order value (AOV) of 482.990023 INR.
> 2. Millennial: 1,766,728 delivered orders, GMV of 853,093,653 INR, and an AOV of 482.866436 INR.
>
> Only two age segments had delivered orders in INR for 2025. All values are for delivered orders only. GMV and AOV are reported in INR. The age segment labels are from the customer dimension.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025 delivered orders in INR, the top customer age segments by delivered order count are:
>
> 1. Gen Z: 2,222,349 delivered orders, GMV 1,073,372,395 INR, AOV 482.990023 INR
> 2. Millennial: 1,766,728 delivered orders, GMV 853,093,653 INR, AOV 482.866436 INR
>
> Only two age segments had delivered orders in INR in 2025. The delivered order count is the number of delivered orders per segment, GMV is the gross merchandise value (sum of sales amount for delivered orders), and AOV is the average order value (GMV divided by delivered order count). All values are for the 2025 calendar year and use the customer dimension's segment labels. No other age segments had delivered orders in INR in 2025.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025 Delivered orders in INR, the top customer age segments by Delivered order count are:
>
> 1. Gen Z: 2,222,349 Delivered orders, GMV 1,073,372,395.00 INR, AOV 482.99002317 INR
> 2. Millennial: 1,766,728 Delivered orders, GMV 853,093,653.00 INR, AOV 482.86643615 INR
>
> No other age segments had Delivered orders in INR for 2025. All values are as recorded in the snapshot. The population is all Delivered orders in INR in 2025, grouped by customer age segment. Units: order count (integer), GMV and AOV (INR). Interpretation: Gen Z and Millennials were the only age segments with Delivered orders in INR, with Gen Z leading in both order count and GMV. AOV is similar for both segments.

</details>


## Q19

**Pertanyaan:** Across every calendar date in 2025, including dates with zero Delivered orders, what was the average number of Delivered orders for each weekday? Which weekday had the highest average?

**Kunci dan cakupan:**

**Reference answer — Weekday average Delivered orders per calendar day.**

Monday **9,094.365385**, Tuesday **9,082.788462**, Wednesday **9,053.773585**, Thursday **9,473.653846**, Friday **12,228.980769**, Saturday **14,486.211538**, Sunday **13,119.134615**. **Saturday** is highest. Include every calendar date; Wednesday has 53 days in 2025, the other weekdays 52.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✓ | Seven weekday averages include all calendar dates |
| B | ✓ | Seven weekday averages include all calendar dates |
| C | ✓ | Seven weekday averages include all calendar dates |
| D | ✗ | Averaged mart city-date rows rather than daily total Delivered orders |
| E | ✓ | Seven weekday averages include all calendar dates |
| F | ✗ | Several weekday totals and averages incorrect |

<details><summary>Jawaban asli A — ✓ benar</summary>

**Final answer (verbatim):**

> Across every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders for each weekday was:
> - Saturday: 14,486.211538
> - Sunday: 13,119.134615
> - Friday: 12,228.980769
> - Thursday: 9,473.653846
> - Monday: 9,094.365385
> - Tuesday: 9,082.788462
> - Wednesday: 9,053.773585
>
> The weekday with the highest average number of Delivered orders was Saturday (14,486.211538 orders per Saturday). Population: all 365 calendar dates in 2025. Unit: Delivered orders per day. Interpretation: Saturdays saw the highest average Delivered order volume, while Wednesdays saw the lowest.

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> For every calendar date in 2025, including dates with zero Delivered orders, the average number of Delivered orders for each weekday was:
> - Saturday: 14,486.211538
> - Sunday: 13,119.134615
> - Friday: 12,228.980769
> - Thursday: 9,473.653846
> - Monday: 9,094.365385
> - Tuesday: 9,082.788462
> - Wednesday: 9,053.773585
>
> The weekday with the highest average number of Delivered orders was Saturday (14,486.211538 orders per Saturday in 2025).
>
> Population: All calendar dates in 2025 (including those with zero Delivered orders). Unit: Delivered orders per weekday. Interpretation: Saturdays had the highest average Delivered order volume, while Wednesdays had the lowest.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For every calendar date in 2025, including dates with zero Delivered orders, the average number of Delivered orders per weekday was:
> - Saturday: 14,486.211538
> - Sunday: 13,119.134615
> - Friday: 12,228.980769
> - Thursday: 9,473.653846
> - Monday: 9,094.365385
> - Tuesday: 9,082.788462
> - Wednesday: 9,053.773585
>
> The weekday with the highest average number of Delivered orders was Saturday (14,486.211538 orders per date).
>
> Population: All calendar dates in 2025 (including those with zero delivered orders). Unit: Delivered orders per date per weekday. Interpretation: Saturdays had the highest average delivered order volume, followed by Sundays and Fridays.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> Across every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders for each weekday was:
> - Saturday: 28.951266
> - Sunday: 26.654489
> - Friday: 25.030781
> - Thursday: 20.140229
> - Monday: 19.475620
> - Wednesday: 19.419263
> - Tuesday: 19.405275
>
> Saturday had the highest average number of Delivered orders. Units are average Delivered orders per calendar date, per weekday, across all cities and currencies. Population: all calendar dates in 2025.

</details>

<details><summary>Jawaban asli E — ✓ benar</summary>

**Final answer (verbatim):**

> Across every calendar date in 2025, including dates with zero Delivered orders, the average number of Delivered orders for each weekday was:
> - Saturday: 14486.211538
> - Sunday: 13119.134615
> - Friday: 12228.980769
> - Thursday: 9473.653846
> - Monday: 9094.365385
> - Tuesday: 9082.788462
> - Wednesday: 9053.773585
>
> Saturday had the highest average number of Delivered orders. Units are orders per day, population is all calendar dates in 2025, and each weekday's average includes all such dates regardless of order activity. Interpretation: Delivery activity peaks on Saturdays, with the lowest averages on Wednesdays.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> To find the average number of Delivered orders for each weekday in 2025 (including dates with zero Delivered orders), we divide the total Delivered orders for each weekday by the number of times that weekday occurs in 2025:
>
> - Friday: 635,907 / 52 = 12,229.942308
> - Monday: 472,907 / 52 = 9,094.365385
> - Saturday: 753,283 / 52 = 14,486.211538
> - Sunday: 682,195 / 52 = 13,111.442308
> - Thursday: 492,630 / 52 = 9,473.653846
> - Tuesday: 472,305 / 52 = 9,083.750000
> - Wednesday: 479,850 / 53 = 9,057.547170
>
> The weekday with the highest average number of Delivered orders is Saturday, with an average of 14,486.211538 Delivered orders per Saturday in 2025.
>
> Population: All calendar dates in 2025 (including those with zero Delivered orders), grouped by weekday. Unit: Delivered orders per weekday. Interpretation: Saturday had the highest average Delivered order volume in 2025.

</details>


## Q20

**Pertanyaan:** Find the largest month-over-month decline in 2025 Delivered-order GMV in INR. Give the two months, their Delivered order counts, GMV, and AOV, then decompose the GMV change into a count effect and an AOV effect using the earlier month's AOV as the count-effect baseline. Do not claim a cause.

**Kunci dan cakupan:**

**Reference answer — Largest monthly GMV drop.**

January → February 2025. Delivered orders **286,712 → 268,570**; GMV **INR 138,573,283 → 129,414,085**; AOV **INR 483.31874145 → 481.86351789**. GMV change **−INR 9,159,198**. Using January AOV as the baseline, count effect **−INR 8,768,368.61** and AOV effect **−INR 390,829.39**; the rounded effects sum to the observed change. This arithmetic decomposition does not establish a business cause.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Wrong months for largest GMV decline and incorrect decomposition |
| B | ✗ | Incorrect count and AOV decomposition amounts |
| C | ✗ | Incorrect count and AOV decomposition amounts |
| D | ✗ | AOVs and decomposition amounts incorrect |
| E | ✗ | Wrong months for largest GMV decline and inconsistent decomposition |
| F | ✗ | Wrong months for largest GMV decline and inconsistent decomposition |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from August to September:
>
> - August 2025: 360,436 delivered orders, GMV = 173,914,937 INR, AOV = 482.512671 INR
> - September 2025: 346,662 delivered orders, GMV = 167,309,430 INR, AOV = 482.629853 INR
>
> GMV change = 167,309,430 - 173,914,937 = -6,605,507 INR
>
> Decomposition:
> - Count effect (using August AOV): (346,662 - 360,436) * 482.512671 = -6,654,964.964 INR
> - AOV effect: (September AOV - August AOV) * September count = (482.629853 - 482.512671) * 346,662 = 40,457.964 INR
>
> Interpretation: The GMV decline of -6,605,507 INR from August to September 2025 is almost entirely due to a decrease in delivered order count, with a negligible positive effect from a slight increase in AOV. No causation is claimed.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from January to February.
>
> - January 2025: 286,712 delivered orders, GMV = 138,573,283 INR, AOV = 483.318741 INR
> - February 2025: 268,570 delivered orders, GMV = 129,414,085 INR, AOV = 481.863518 INR
> - GMV change: 129,414,085 - 138,573,283 = -9,159,198 INR
>
> Decomposition of GMV change:
> - Count effect (using January's AOV): (February order count - January order count) × January AOV = (268,570 - 286,712) × 483.318741 = (-18,142) × 483.318741 = -8,771,964.837622 INR
> - AOV effect (using February's order count): (February AOV - January AOV) × February order count = (481.863518 - 483.318741) × 268,570 = (-1.455223) × 268,570 = -390,233.162110 INR
>
> Interpretation: The total GMV decline of -9,159,198 INR from January to February 2025 is primarily due to a decrease in delivered order count (-8,771,964.84 INR), with a smaller contribution from a decrease in average order value (-390,233.16 INR). No causation is claimed.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from January to February.
>
> - Earlier month: January 2025
>   - Delivered order count: 286,712
>   - Delivered GMV (INR): 138,573,283.00
>   - Delivered AOV (INR): 483.31874145
> - Later month: February 2025
>   - Delivered order count: 268,570
>   - Delivered GMV (INR): 129,414,085.00
>   - Delivered AOV (INR): 481.86351789
>
> GMV change: 129,414,085.00 - 138,573,283.00 = -9,159,198.00 INR
>
> Decomposition:
> - Count effect (using Jan AOV): (Feb count - Jan count) × Jan AOV = (268,570 - 286,712) × 483.31874145 = (-18,142) × 483.31874145 = -8,771,964.099
> - AOV effect (using Feb count): (Feb AOV - Jan AOV) × Feb count = (481.86351789 - 483.31874145) × 268,570 = (-1.45522356) × 268,570 = -390,233.901
>
> Interpretation: The GMV decline of -9,159,198.00 INR from January to February 2025 is primarily due to a decrease in delivered order count (count effect: -8,771,964.099 INR), with a smaller contribution from a decrease in average order value (AOV effect: -390,233.901 INR). No causation is claimed.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from January to February.
>
> - January 2025: Delivered order count = 286,712; Delivered GMV = 138,573,283.00 INR; AOV = 483.367964 INR
> - February 2025: Delivered order count = 268,570; Delivered GMV = 129,414,085.00 INR; AOV = 482.012964 INR
>
> GMV change = 129,414,085.00 - 138,573,283.00 = -9,159,198.00 INR
>
> Decomposition:
> - Count effect (using January's AOV): (February count - January count) × January AOV = (268,570 - 286,712) × 483.367964 = -8,803,073.13 INR
> - AOV effect (using February count): (February AOV - January AOV) × February count = (482.012964 - 483.367964) × 268,570 = -364,124.87 INR
>
> Interpretation: The GMV decline of -9,159,198.00 INR from January to February 2025 is mostly due to a drop in delivered order count (-8,803,073.13 INR), with a smaller contribution from a decrease in average order value (-364,124.87 INR). No causation is claimed.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from August to September.
>
> - August 2025: Delivered order count = 360,436; GMV = 173,914,937 INR; AOV = 482.512671 INR
> - September 2025: Delivered order count = 346,662; GMV = 167,309,430 INR; AOV = 482.629853 INR
>
> GMV change = 167,309,430 - 173,914,937 = -6,605,507 INR (decline)
>
> Decomposition:
> - Count effect (using August's AOV): (346,662 - 360,436) × 482.512671 = -6,673,073.44 INR
> - AOV effect (using September's count): (482.629853 - 482.512671) × 346,662 = +40,566.44 INR
> - Total explained change: -6,673,073.44 + 40,566.44 = -6,632,507.00 INR (matches observed decline within rounding)
>
> Interpretation: The GMV decline from August to September 2025 in INR was primarily due to a decrease in delivered order count, with a negligible positive effect from a slight increase in AOV. No cause is claimed.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> The largest month-over-month decline in 2025 Delivered-order GMV in INR occurred from August to September.
>
> - August 2025: Delivered order count = 360,436; GMV = 173,914,937 INR; AOV = 482.512671 INR
> - September 2025: Delivered order count = 346,662; GMV = 167,309,430 INR; AOV = 482.629853 INR
> - GMV change = 167,309,430 - 173,914,937 = -6,605,507 INR
>
> Decomposition of GMV change:
> - Count effect (using August's AOV): (346,662 - 360,436) × 482.512671 = -6,666,899.44 INR
> - AOV effect (using September's count): (482.629853 - 482.512671) × 346,662 = +40,392.44 INR
> - Total = Count effect + AOV effect = -6,626,507.00 INR (matches observed GMV change within rounding)
>
> Interpretation: The GMV decline from August to September is almost entirely due to a decrease in delivered order count, with AOV nearly unchanged. No cause is claimed.

</details>


## Q21

**Pertanyaan:** Across the twelve months of 2025, did monthly cancellation rate and average Delivered-order delivery time move together? Report their monthly Pearson correlation, the number of months used, and whether that alone supports a causal claim.

**Kunci dan cakupan:**

**Reference answer — Monthly correlation.**

Twelve paired months; Pearson `r = −0.0200303` between monthly cancellation rate and average Delivered duration. This is near zero linear association in these months and **does not establish causation**. The denominator for duration is Delivered orders with non-null duration, not all orders.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Incorrect Pearson correlation |
| B | ✗ | Incorrect Pearson correlation |
| C | ✗ | Incorrect Pearson correlation |
| D | ✗ | Incorrect Pearson correlation |
| E | ✗ | Incorrect Pearson correlation |
| F | ✗ | Incorrect Pearson correlation sign and value |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> Across the twelve months of 2025, the Pearson correlation between monthly cancellation rate and average delivery time for delivered orders is approximately 0.073964. This is based on 12 months of data (January to December 2025). This very weak positive correlation indicates that the two metrics moved almost independently over the year. Correlation alone does not support a causal claim; it only measures linear association, not causation. Other factors or confounders could explain any observed relationship.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> To answer, we first calculate the monthly cancellation rate as CANCELLED_ORDERS / TOTAL_ORDERS for each month, and use the provided average delivery time for delivered orders. Calculating the Pearson correlation coefficient between these two series across the 12 months of 2025 yields a value of approximately 0.073857. The number of months used is 12. This very low positive correlation indicates that monthly cancellation rate and average delivered-order delivery time did not move together in a meaningful way in 2025. Correlation alone does not support a causal claim; it only measures linear association, not causation. Other factors or confounders may be involved, and further analysis would be required to establish causality.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> The Pearson correlation between monthly cancellation rate and average delivered-order delivery time across the twelve months of 2025 is approximately 0.099964. This was calculated using the monthly values for cancellation rate and average delivery time for each month (12 months in total). The correlation is very close to zero, indicating almost no linear relationship between the two metrics over these months. 
>
> Population: All Zomato orders in 2025, grouped by month (n=12 months).
> Units: Cancellation rate (unitless, proportion), average delivery time (minutes).
>
> Interpretation: The low correlation suggests that changes in monthly cancellation rate and average delivered-order delivery time did not move together in 2025. This correlation alone does not support a causal claim between these two metrics; correlation does not imply causation, and further analysis would be required to establish any causal relationship.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> For each month in 2025, the cancellation rate was calculated as CANCELLED_ORDER_COUNT / TOTAL_ORDER_COUNT, and the average delivered-order delivery time as DELIVERED_DELIVERY_TIME_SUM_MIN / DELIVERED_ORDER_COUNT. Using the 12 monthly pairs, the Pearson correlation between cancellation rate and average delivered-order delivery time is approximately 0.997964. All 12 months were used. This very high positive correlation means that, in 2025, months with higher cancellation rates also tended to have higher average delivery times for delivered orders. However, correlation alone does not support a causal claim; other factors could drive both metrics, and further analysis would be needed to establish causality.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> To assess whether monthly cancellation rate and average delivery time for delivered orders moved together in 2025, we calculate the Pearson correlation coefficient using the 12 monthly pairs provided. The computed Pearson correlation is approximately 0.0197 (rounded to six decimals), based on all 12 months of 2025. This value is very close to zero, indicating almost no linear relationship between the two metrics across months. 
>
> Population: All Zomato orders in 2025, aggregated by month (n=12 months).
> Units: Cancellation rate (percentage of orders cancelled), average delivery time (minutes, delivered orders only).
>
> Interpretation: The near-zero correlation means that, in 2025, months with higher cancellation rates did not systematically coincide with higher or lower average delivery times for delivered orders. This correlation alone does not support a causal claim between cancellation rate and delivery time; correlation does not imply causation, and further analysis would be required to establish any causal relationship.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> To assess whether monthly cancellation rate and average delivery time for delivered orders moved together in 2025, we calculate the Pearson correlation coefficient between the two metrics across the 12 months. Using the provided monthly values, the Pearson correlation is approximately 0.0736 (rounded to four decimals: 0.0736), based on all 12 months of 2025. This is a very weak positive correlation, indicating little to no linear relationship between the two metrics over the year. 
>
> Population: 12 months in 2025. Units: cancellation rate (percent), average delivery time (minutes).
>
> Interpretation: This weak correlation does not support a causal claim between cancellation rate and average delivery time. Correlation alone, especially of this magnitude, does not establish causation.

</details>


## Q22

**Pertanyaan:** For the standard market report covering 2025, what were Delivered-order GMV in INR, Delivered order count, and AOV? Apply the standard market eligibility rule consistently to all three.

**Kunci dan cakupan:**

**Reference answer — Standard market.**

After filtering restaurants with `rating_count >= 100`: **1,848,107 Delivered orders**, **INR 927,955,016 GMV**, **INR 502.11108772 AOV** in 2025. Apply the same eligibility filter to numerator and denominator.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Invented standard-market eligibility and omitted rating-count threshold |
| B | ✗ | Invented standard-market eligibility and omitted rating-count threshold |
| C | ✗ | Invented standard-market eligibility and omitted rating-count threshold |
| D | ✗ | Invented eligibility rule; omitted restaurant rating-count threshold |
| E | ✗ | Invented eligibility rule; omitted restaurant rating-count threshold |
| F | ✗ | Quoted standard-market eligibility but used unfiltered full-market MetricFlow result |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report covering 2025, applying the standard market eligibility rule (delivered orders in INR):
> - Delivered-order GMV in INR: 1,926,466,048.0 INR
> - Delivered order count: 3,989,077 orders
> - AOV (Average Order Value): 482.935288 INR per order
>
> All three metrics are calculated for delivered orders in INR during 2025. The AOV is the GMV divided by the delivered order count, with at least six decimals retained for precision.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report covering 2025, applying the standard market eligibility rule (delivered, not cancelled, not refunded, INR orders):
> - Delivered-order GMV in INR: 1,926,466,048.00 INR
> - Delivered order count: 3,989,077 orders
> - Delivered AOV (Average Order Value): 482.93528754 INR per order
>
> All three metrics are calculated for the same eligible population and period. The AOV is the mean sales amount per delivered order, to six decimals as requested.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report covering 2025, applying the standard market eligibility rule (delivered orders in INR) to all three metrics:
> - Delivered-order GMV in INR: 1,926,466,048.00 INR
> - Delivered order count: 3,989,077 orders
> - Delivered AOV (Average Order Value) in INR: 482.935288 INR per order
>
> Population: All delivered orders in INR currency during 2025. Units: GMV and AOV in INR, order count as integer. Interpretation: The average delivered order in 2025 was worth approximately 482.94 INR, with nearly 4 million delivered orders and a total delivered GMV of about 1.93 billion INR.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report covering 2025 (orders in INR):
> - Delivered-order GMV was 1,926,466,048.00 INR.
> - Delivered order count was 3,989,077.
> - Delivered AOV (Average Order Value) was 482.935288 INR.
>
> All three metrics consistently apply the standard market eligibility rule (INR currency, delivered orders, 2025 order date).

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report covering 2025, applying the standard market eligibility rule (delivered orders, INR currency) consistently to all metrics: 
> - Delivered-order GMV in INR: 1,926,466,048.0 INR
> - Delivered order count: 3,989,077 orders
> - AOV (Average Order Value): 482.935288 INR per delivered order (rounded to six decimals)
>
> Population: All delivered orders in 2025 with currency INR. Units: GMV and AOV in INR, order count as integer. Interpretation: The average delivered order in INR during 2025 was worth approximately 482.94 INR, with nearly 4 million delivered orders and a total delivered GMV of about 1.93 billion INR.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For the standard market report in 2025 (applying the eligibility rule: only restaurants with at least 100 recorded ratings), the results for Delivered orders in INR are as follows:
>
> - Delivered-order GMV: 1,926,466,048 INR
> - Delivered order count: 3,989,077 orders
> - AOV (Average Order Value): 482.935288 INR per delivered order
>
> Population: All Delivered orders from eligible restaurants (rating_count >= 100) in 2025, reported in INR. Units are as specified. All three metrics were filtered consistently per the standard market eligibility rule.

</details>


## Q23

**Pertanyaan:** In the 2025 standard market report, which three cities led by Delivered-order GMV in INR? Give each city's GMV and share of standard market GMV, using the reporting geography default.

**Kunci dan cakupan:**

**Reference answer — Standard-market city ranking.**

Use restaurant-dimension city and the same `rating_count >= 100` filter for the total denominator.

| Reporting city | GMV INR | Share of standard-market GMV |
| --- | ---: | ---: |
| Bangalore | 129,604,607 | 13.96669071% |
| Chennai | 92,523,985 | 9.97074033% |
| Hyderabad | 79,925,454 | 8.61307419% |

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Invented full-market geography and ignored missing standard-market policy |
| B | ✗ | Applied full-market order-city ranking instead of unspecified standard-market policy |
| C | ✗ | Invented standard-market policy; used full-market order cities |
| D | ✗ | Invented standard-market geography and omitted eligibility rule |
| E | ✗ | Invented standard-market policy and used full-market order-city ranking |
| F | ✓ | Correct eligibility, geography, ranking, GMV and shares within revised ±0.01 percentage-point tolerance |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:
>
> 1. Bikaner: GMV = 29,030,997 INR, Share = 0.015070 (1.5070%)
> 2. Indiranagar,Bangalore: GMV = 22,092,650 INR, Share = 0.011470 (1.1470%)
> 3. Koramangala,Bangalore: GMV = 18,686,823 INR, Share = 0.009698 (0.9698%)
>
> Population: Delivered orders in INR currency, 2025, by city (reporting geography default).
> Unit: INR (GMV), proportion of total delivered-order GMV (share).
> Interpretation: These three cities together contributed about 3.62% of the delivered-order GMV in INR for the standard market in 2025.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:
>
> 1. Bangalore: GMV = 233,341,258.00 INR, Share = 0.121144 (12.1144%)
> 2. Delhi: GMV = 177,702,873.00 INR, Share = 0.092263 (9.2263%)
> 3. Chennai: GMV = 155,055,243.00 INR, Share = 0.080497 (8.0497%)
>
> Population: All delivered orders in INR currency in 2025, grouped by city (reporting geography default).
> Unit: INR (Indian Rupees) for GMV, share is a decimal fraction of total standard market GMV.
> Interpretation: These three cities contributed the highest delivered GMV in INR, together accounting for about 29.39% of the standard market's delivered GMV in 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:
>
> 1. Bangalore: GMV = 233,341,258 INR, Share = 0.121158 (12.1158%)
> 2. Delhi: GMV = 177,702,873 INR, Share = 0.092263 (9.2263%)
> 3. Chennai: GMV = 155,055,243 INR, Share = 0.080507 (8.0507%)
>
> Population: All delivered orders in INR currency in 2025, grouped by city (reporting geography default).
> Unit: INR (Indian Rupees) for GMV, share is a proportion of total delivered GMV in INR.
> Interpretation: These three cities together accounted for about 29.39% of the delivered GMV in the standard market for 2025.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:
>
> 1. Bangalore: GMV = 233,341,258.00 INR, Share = 0.121144 (12.1144%)
> 2. Delhi: GMV = 177,702,873.00 INR, Share = 0.092263 (9.2263%)
> 3. Chennai: GMV = 155,055,243.00 INR, Share = 0.080497 (8.0497%)
>
> Population: All delivered orders in INR currency in 2025, grouped by city (reporting geography default).
> Unit: INR (Indian Rupees) for GMV, share is a proportion of total delivered GMV in INR.
> Interpretation: Bangalore, Delhi, and Chennai together accounted for approximately 29.39% of the delivered-order GMV in INR in the standard market for 2025.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:
>
> 1. Bangalore: GMV = 233,341,258 INR (share: 12.116857%)
> 2. Delhi: GMV = 177,702,873 INR (share: 9.227964%)
> 3. Chennai: GMV = 155,055,243 INR (share: 8.050964%)
>
> These shares are calculated out of the total standard market delivered GMV in INR for 2025, which was 1,926,466,048 INR. The reporting geography default is city. Each city's share is its GMV divided by the total GMV, expressed as a percentage with at least six decimals for precision.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> In the 2025 standard market report (restaurants with at least 100 ratings, using restaurant city as the reporting geography), the three leading cities by Delivered-order GMV in INR were:
>
> 1. Bangalore: GMV = 129,604,607 INR (share: 0.139675)
> 2. Chennai: GMV = 92,523,985 INR (share: 0.099749)
> 3. Hyderabad: GMV = 79,925,454 INR (share: 0.086154)
>
> Population: Delivered orders at eligible restaurants in 2025, currency INR, grouped by restaurant city.
> Unit: INR (Indian Rupees) for GMV; share is the city's GMV divided by the total standard market GMV (927,955,016 INR), shown as a decimal fraction.
> Interpretation: These three cities together accounted for approximately 32.6% of the standard market's delivered-order GMV in INR for 2025.

</details>


## Q24

**Pertanyaan:** How many repeat customers were there in January–June 2025 and in July–December 2025? Evaluate repeat status separately within each reporting period, then say which half had more.

**Kunci dan cakupan:**

**Reference answer — Repeat customers by half.**

January–June: **94,251** customers with at least two Delivered orders within H1, among 98,033 customers with any Delivered order. July–December: **95,899**, among 98,642. H2 had **1,648 more** repeat customers. Qualify independently in each half; a Delivered order in the other half does not count.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Counted all-status repeat orders instead of Delivered-only policy |
| B | ✗ | Counted all-status repeat orders instead of Delivered-only policy |
| C | ✗ | Counted all-status repeat orders instead of Delivered-only policy |
| D | ✗ | Counted all-status repeat orders instead of Delivered-only policy |
| E | ✗ | Used non-cancelled rather than Delivered-only repeat rule |
| F | ✓ | Applied delivered-only repeat rule separately in each half and correct counts |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 95,048 repeat customers (users who placed more than one order in that period). In July–December 2025, there were 96,514 repeat customers (users who placed more than one order in that period). Repeat status was evaluated separately within each half-year. July–December 2025 had more repeat customers than January–June 2025.

</details>

<details><summary>Jawaban asli B — ✗ salah</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 95,048 repeat customers (customers who placed more than one order in that period). In July–December 2025, there were 96,514 repeat customers (evaluated independently for that period). July–December 2025 had more repeat customers than January–June 2025. Population: all customers with at least one order in each respective period. Unit: unique customers per period. Interpretation: Repeat customer counts are slightly higher in the second half of 2025.

</details>

<details><summary>Jawaban asli C — ✗ salah</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 94,512 repeat customers (customers with more than one order in that period). In July–December 2025, there were 96,095 repeat customers (customers with more than one order in that period). Repeat status was evaluated separately within each half-year. July–December 2025 had more repeat customers than January–June 2025.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 94,512 repeat customers (customers with more than one order in that period). In July–December 2025, there were 96,095 repeat customers. Repeat status was evaluated separately within each half-year. July–December 2025 had more repeat customers than January–June 2025 (by 1,583 customers).

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 94,512 repeat customers (customers with more than one non-cancelled order in that period). In July–December 2025, there were 96,095 repeat customers (customers with more than one non-cancelled order in that period). The second half of 2025 (July–December) had more repeat customers than the first half.

</details>

<details><summary>Jawaban asli F — ✓ benar</summary>

**Final answer (verbatim):**

> In January–June 2025, there were 94,251 repeat customers (customers with at least two delivered orders in that period). In July–December 2025, there were 95,899 repeat customers (evaluated separately for that half). July–December 2025 had more repeat customers than January–June 2025. Population: all customers with at least two delivered orders in each respective half-year period. Unit: unique customers per half-year. Interpretation: The number of repeat customers increased in the second half of 2025.

</details>


## Q25

**Pertanyaan:** For the order-recorded city with the highest 2025 cancellation rate among cities with at least 50,000 orders, compare its cancellation rate and average Delivered-order delivery time with the overall 2025 figures. Can these figures establish that slower delivery caused cancellations?

**Kunci dan cakupan:**

**Reference answer — Descriptive diagnosis and limit.**

Hyderabad is the highest-cancellation order city among cities with at least 50,000 orders: **6.027789%** versus **5.997009%** overall, a **+0.030780 pp** gap. Its average Delivered duration is **31.0967157 min** versus **31.0743794 min** overall, a **+0.0223363 min** gap. These are descriptive comparisons with different populations; they **cannot establish that slower delivery caused cancellations**.

| Arm | Skor | Alasan penilaian |
| --- | :---: | --- |
| A | ✗ | Wrong highest-cancellation city |
| B | ✓ | Correct city, cancellation and delivery comparisons, causal limit |
| C | ✓ | Correct city, comparisons and causal limit |
| D | ✗ | Incorrect Hyderabad delivery mean |
| E | ✗ | Missing Hyderabad delivery-time comparison |
| F | ✗ | Missing Hyderabad delivery-time comparison |

<details><summary>Jawaban asli A — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, Bikaner is the city with the highest cancellation rate among cities with at least 50,000 orders. The figures are:
>
> - Bikaner (2025):
>   - Cancellation rate: 0.059603 (5.9603%)
>   - Average delivery time (delivered orders): 31.045172 minutes
>   - Orders analyzed: 53,571
>
> - Overall (2025):
>   - Cancellation rate: 0.059970 (5.9970%)
>   - Average delivery time (delivered orders): 31.074379 minutes
>
> Interpretation:
> - Bikaner's cancellation rate is slightly below the overall average, and its average delivery time for delivered orders is also marginally lower than the overall average.
> - These figures do not establish that slower delivery caused cancellations in Bikaner or overall. The cancellation rate is not higher where delivery is slower, and correlation alone would not prove causation without further analysis (e.g., comparing cancelled vs. delivered order delivery times, controlling for confounders).

</details>

<details><summary>Jawaban asli B — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, Hyderabad is the city with the highest cancellation rate among cities with at least 50,000 orders (319,122 orders). Its cancellation rate is 0.060278 (6.0278%), and its average delivery time for delivered orders is 31.0967157 minutes. The overall 2025 cancellation rate across all cities is 0.059970 (5.9970%), and the overall average delivered order delivery time is 31.0743794 minutes.
>
> Interpretation: Hyderabad's cancellation rate and average delivery time are both slightly higher than the overall figures. However, these small differences do not establish that slower delivery caused cancellations. Correlation alone does not prove causation; other factors could be involved, and further analysis (such as examining delivery times specifically for cancelled orders or controlling for confounding variables) would be needed to establish causality.

</details>

<details><summary>Jawaban asli C — ✓ benar</summary>

**Final answer (verbatim):**

> For 2025, Hyderabad is the city with the highest cancellation rate among cities with at least 50,000 orders (319,122 orders). Its cancellation rate is 0.060278 (6.0278%), and its average delivery time for delivered orders is 31.096716 minutes. The overall 2025 cancellation rate across all cities is 0.059970 (5.9970%), and the overall average delivery time for delivered orders is 31.074379 minutes.
>
> Interpretation: Hyderabad's cancellation rate and average delivery time are both slightly higher than the overall figures. However, these small differences do not establish that slower delivery caused cancellations. Correlation alone does not prove causation; other factors could be involved, and further analysis (such as order-level timing vs. cancellation, or causal modeling) would be required to establish causality.

</details>

<details><summary>Jawaban asli D — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, Hyderabad is the city with the highest cancellation rate among cities with at least 50,000 orders. Its cancellation rate was 0.060278 (6.0278%) out of 319,122 orders, compared to the overall 2025 cancellation rate of 0.059970 (5.9970%). The average delivery time for delivered orders in Hyderabad was 31.080007 minutes, while the overall average was 31.074379 minutes. 
>
> Interpretation: Hyderabad's cancellation rate and average delivery time are both slightly above the overall figures, but the differences are very small (cancellation rate higher by 0.000308, delivery time higher by 0.005628 minutes). These figures alone do not establish that slower delivery caused cancellations, as correlation does not prove causation and the delivery time difference is negligible. Other factors may be involved, and further causal analysis would be required.

</details>

<details><summary>Jawaban asli E — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, Hyderabad is the order-recorded city with the highest cancellation rate among cities with at least 50,000 orders. Its cancellation rate is 0.060278 (6.0278%), based on 319,122 orders. The overall 2025 cancellation rate is 5.997009% and the overall average delivery time for delivered orders is 31.074379 minutes. (Hyderabad's average delivery time for delivered orders was not directly retrieved, so only the overall figure is available.)
>
> Interpretation: Hyderabad's cancellation rate is slightly higher than the overall average. However, without Hyderabad's specific average delivery time, we cannot directly compare its delivery speed to the overall average. Even if Hyderabad had a slower delivery time, this correlation alone would not establish that slower delivery caused more cancellations. Establishing causation would require further analysis, such as controlling for confounding factors and examining whether slower delivery times precede cancellations within the same city or order cohort.

</details>

<details><summary>Jawaban asli F — ✗ salah</summary>

**Final answer (verbatim):**

> For 2025, Hyderabad is the order-recorded city with the highest cancellation rate among cities with at least 50,000 orders. Its cancellation rate was 0.060278 (6.0278%) out of 319,122 orders. The overall 2025 cancellation rate across all cities was 0.059970 (5.9970%). The average delivery time for delivered orders overall was 31.074379 minutes. (The Hyderabad-specific average delivery time was not directly calculated, but the comparison is between Hyderabad's cancellation rate and the overall average delivery time.)
>
> Interpretation: Hyderabad's cancellation rate is slightly higher than the overall average, but the difference is marginal (0.0308 percentage points). The overall average delivery time does not establish a direct causal link between slower delivery and higher cancellations in Hyderabad. Correlation or comparison alone does not prove causation; additional analysis (such as comparing Hyderabad's delivery times specifically, or controlling for other factors) would be required to establish whether slower delivery caused more cancellations.

</details>
