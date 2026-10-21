# Audit jawaban A–F: 25 pertanyaan (run v2, 3 repetisi)

Perbandingan ini memakai **jawaban akhir asli** dari 450 attempt `gpt-4.1` pada 21 Oktober 2026 (3 repetisi × 150 kombinasi arm×pertanyaan) dan skor dari [`af_25_v2_grades.json`](../experiments/run.local/af_25_v2_grades.json). Kunci disalin dari [`answers_25.md`](../experiments/answers_25.md).

**Rubrik:** semua bagian jawaban harus benar; count, identitas, dan rank eksak; total uang ±INR 0,01; persentase ±0,01 pp; average/korelasi ±0,01 unit; komponen Q20 ±INR 0,05. Q22–Q24 memerlukan kebijakan bisnis (hanya F). `✓` = semua rep benar; `~` = sebagian benar (mean 0,333–0,667); `✗` = semua rep salah.

| Arm | Mean data benar / 22 | Mean kebijakan / 3 | Mean total / 25 |
| --- | ---: | ---: | ---: |
| A | 11.6666 | 0.0000 | 11.6666 |
| B | 15.6667 | 0.0000 | 15.6667 |
| C | 16.3334 | 0.0000 | 16.3334 |
| D | 16.3333 | 0.0000 | 16.3333 |
| E | 17.3334 | 0.0000 | 17.3334 |
| F | 16.0000 | 3.0000 | 19.0000 |

## Q01

**Kunci dan cakupan:**

**4.359.773 orders.** Count every order with a recorded `order_date` in 2025, regardless of status or currency. Exact integer.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Count 4.359.773 benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count represents all orders in the dataset with ORDER_DATE between 2025-01-01 and 2025-12-31 (exclusive of 2026).

**B ✓:** A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count represents all orders in the population with ORDER_DATE between 2025-01-01 and 2025-12-31 (exclusive of 2026). The unit is orders.

**C ✓:** A total of 4,359,773 orders were placed during 2025, using the recorded order date. This count represents all orders in the population for the year 2025.

**D ✓:** A total of 4,359,773 orders were placed during 2025, using the recorded order date. This count represents all orders in the population for that year.

**E ✓:** A total of 4,359,773 orders were placed during 2025, based on the recorded order date. This count includes all orders regardless of their status.

**F ✓:** A total of 4,359,773 orders were placed during 2025, using the recorded order date. This count includes all orders regardless of status.

</details>

## Q02

**Kunci dan cakupan:**

**INR 1.926.466.048,00 GMV.** Sum recorded `sales_amount` for 2025 **Delivered** orders in INR. Tolerance: ±INR 0,01.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** The total Delivered-order GMV (Gross Merchandise Value) in INR for the full year 2025, using the recorded order date, was 1,926,466,048.0 INR. This value represents the sum of SALES_AMOUNT for all orders with ORDER_STATUS = 'Delivered' and CURRENCY = 'INR' between 2025-01-01 and 2025-12-31 (inclusiv...

**B ✓:** The total Delivered-order GMV (Gross Merchandise Value) in INR for the full year 2025, using the recorded order date, was 1,926,466,048.00 INR. This value represents the sum of delivered sales amounts for all orders in INR currency that were delivered between January 1, 2025 and December 31, 2025 (i...

**C ✓:** The total Delivered-order GMV (Gross Merchandise Value) in INR for the full year 2025, using the recorded order date, was 1,926,466,048.00 INR. This value represents the sum of delivered sales amounts for all orders in INR currency that were delivered between January 1, 2025 and December 31, 2025 (i...

**D ✓:** The total Delivered-order GMV (Gross Merchandise Value) in INR for the full year 2025, using the recorded order date, was 1,926,466,048.00 INR. This value represents the sum of delivered sales amounts for all orders in INR currency during 2025.

**E ✓:** The total Delivered-order GMV in INR for the full year 2025, using the recorded order date, was 1,926,466,048.0 INR. This value represents the sum of sales_amount for all orders with order_status 'Delivered' in 2025, with no currency conversion applied. Population: all delivered orders in 2025. Unit...

**F ✓:** The total Delivered-order GMV (Gross Merchandise Value) in INR for the full year 2025, using the recorded order date, was 1,926,466,048.0 INR. This value represents the sum of sales amounts for all orders with status 'Delivered' in the INR currency during 2025.

</details>

## Q03

**Kunci dan cakupan:**

**INR 482,9352875364 per Delivered order.** Divide INR 1.926.466.048,00 GMV by **3.989.077 Delivered orders**. Tolerance: ±INR 0,01.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** The Average Order Value (AOV) for Delivered orders in INR for the full year 2025, using the recorded order date, was 482.935288 INR. This value is calculated as the total sales amount divided by the number of delivered orders in INR currency for the specified period. Population: all delivered orders...

**B ✓:** The Average Order Value (AOV) in INR for delivered orders in the full year 2025, using the recorded order date, was 482.935288 INR. This value is calculated as the total sales amount in INR divided by the number of delivered orders in 2025. Population: all delivered orders with currency INR and orde...

**C ✓:** The Average Order Value (AOV) for delivered orders in INR for the full year 2025, using the recorded order date, was 482.935288 INR. This value is calculated across all delivered orders with currency INR in the specified period. Unit: INR per delivered order. Population: all delivered orders in INR ...

**D ✓:** The Average Order Value (AOV) for delivered orders in INR for the full year 2025, using the recorded order date, was 482.935288 INR. This value represents the mean delivered sales amount per delivered order in Indian Rupees for all delivered orders placed between January 1, 2025 and December 31, 202...

**E ✓:** The average order value (AOV) for delivered orders in INR for the full year 2025, using the recorded order date, was 482.935288 INR. This means that, on average, each delivered order in 2025 generated sales of approximately 482.94 INR. Population: all delivered orders in 2025, currency: INR, unit: I...

**F ✓:** The average order value (AOV) for Delivered orders in INR for the full year 2025, using the recorded order date, was 482.935288 INR per delivered order. This value is calculated as the gross merchandise value (GMV) divided by the number of delivered orders, considering only orders with currency INR....

</details>

## Q04

**Kunci dan cakupan:**

**5,9970094773%.** Divide **261.456 Cancelled orders** by **4.359.773 total orders** × 100. Tolerance: ±0,01 pp.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** For the full year 2025 (ORDER_DATE >= '2025-01-01' AND ORDER_DATE < '2026-01-01'), there were 4,359,773 total orders, of which 261,456 were cancelled. The cancellation rate was 5.997009% (rounded to six decimals). This means that approximately 6 out of every 100 orders placed in 2025 were cancelled....

**B ✓:** The cancellation rate for Zomato orders in the full year 2025, using the recorded order date, was 5.997009%. This is based on a population of 4,359,773 total orders, of which 261,456 were cancelled. The unit is percentage (%), and the rate is calculated as (cancelled orders / total orders) * 100. In...

**C ✓:** For the full year 2025 (ORDER_DATE >= '2025-01-01' AND ORDER_DATE < '2026-01-01'), there were 4,359,773 total orders, of which 261,456 were cancelled. This results in a cancellation rate of 5.997009% for all recorded orders in 2025. The unit is percentage, and the population is all orders with a rec...

**D ✓:** For the full year 2025 (ORDER_DATE >= '2025-01-01' AND ORDER_DATE < '2026-01-01'), there were 4,359,773 total orders recorded. Of these, 261,456 orders were cancelled. This results in a cancellation rate of 5.997009% for the year. The cancellation rate is calculated as (cancelled orders / total orde...

**E ✓:** The cancellation rate for the full year 2025, using the recorded order date, was 5.997009%. This means that out of all orders placed in 2025, approximately 6% were cancelled. The population is all recorded orders in 2025, and the unit is percentage of orders cancelled.

**F ✓:** The cancellation rate for all recorded orders in 2025, using the recorded order date, was 5.997009%. This means that out of all orders placed in 2025, approximately 6% were cancelled. The population is all orders with an order date in 2025, and the unit is percent of orders cancelled.

</details>

## Q05

**Kunci dan cakupan:**

**2,80539307895 units per order.** Divide **12.230.877 item units** by **4.359.773 total orders**. Tolerance: ±0,01.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 0 | 0.667 ~ | Sebagian benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** For the full year 2025 (using recorded order date), the average ordered quantity per order was 2.805393 items, across a total of 4,359,773 orders. This means that, on average, each order contained about 2.81 items.

**B ✓:** For the full year 2025 (ORDER_DATE >= '2025-01-01' AND ORDER_DATE < '2026-01-01'), the average ordered quantity per order was 2.805393. This means that, on average, each order placed in 2025 contained approximately 2.805393 items. The population is all recorded orders in 2025, and the unit is items ...

**C ✓:** For the full year 2025 (using recorded order date), the average ordered quantity per order was 2.805393 items. This value is calculated across all orders placed in 2025. Unit: items per order. Population: all orders with a recorded order date in 2025. Interpretation: On average, each order in 2025 c...

**D ✓:** The ordered quantity per order for the full year 2025, using the recorded order date, was 2.805393 items per order. This average is calculated across all orders placed in 2025. Unit: items per order. Population: all orders with ORDER_DATE in 2025. Interpretation: On average, each order in 2025 conta...

**E ~:** For the full year 2025 (using recorded order date), the ordered quantity per order was 2.805393 (unit: items per order, population: all recorded orders in 2025). This means that, on average, each order contained approximately 2.81 items.

**F ✓:** For the full year 2025, the ordered quantity per order was 2.805393 (units per order, rounded to six decimals). This means that, on average, each order contained approximately 2.81 items. The population includes all orders recorded with an order date in 2025, regardless of order status. The unit is ...

</details>

## Q06

**Kunci dan cakupan:**

**Desember 2025: INR 185.263.071** (383.530 order). Runner-up November: **INR 180.239.871** (373.651). Gap: **INR 5.023.200**.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** In 2025, the month with the highest Delivered-order GMV in INR was December (2025-12) with a GMV of 185,263,071 INR. The runner-up was November (2025-11) with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation:...

**B ✓:** In 2025, December had the highest Delivered-order GMV in INR, totaling 185,263,071.00 INR. The runner-up month was November, with a GMV of 180,239,871.00 INR. The gap between December and November was 5,023,200.00 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation: Decem...

**C ✓:** In 2025, December had the highest Delivered-order GMV in INR, with a GMV of 185,263,071.00 INR. The runner-up month was November, with a GMV of 180,239,871.00 INR. The gap between them was 5,023,200.00 INR. Population: all delivered orders in INR in 2025. Unit: INR. Interpretation: December outperfo...

**D ✓:** In 2025, the month with the highest Delivered-order GMV in INR was December, with a GMV of 185,263,071 INR. The runner-up was November, with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. Population: all delivered orders in INR currency in 2025. Unit: INR. Interpretation: December...

**E ✓:** In 2025, the month with the highest Delivered-order GMV in INR was December, with a GMV of 185,263,071 INR. The runner-up month was November, with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. 

Population: All delivered orders in 2025 with currency INR, grouped by month. 
Unit: ...

**F ✓:** In 2025, the month with the highest Delivered-order GMV in INR was December, with a GMV of 185,263,071 INR. The runner-up month was November, with a GMV of 180,239,871 INR. The gap between them was 5,023,200 INR. 

Population: All delivered orders in 2025 with sales amounts in INR, grouped by month....

</details>

## Q07

**Kunci dan cakupan:**

Januari: 286.712 order, INR 138.573.283, AOV INR 483,31874145. Desember: 383.530, INR 185.263.071, AOV INR 483,04714364. **Count naik 33,7684%**; **AOV turun 0,0562%**. Count tumbuh lebih cepat. Toleransi ±0,01 pp.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |
| B | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |
| C | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |
| D | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |
| E | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |
| F | 0 | 0 | 0 | 0.000 ✗ | Perubahan % count ~33,73–33,75% (di luar ±0,01 pp dari 33,7684%) |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For January 2025: Delivered order count = 286,712; GMV in INR = 138,573,283.0; AOV in INR = 483.318741. For December 2025: Delivered order count = 383,530; GMV in INR = 185,263,071.0; AOV in INR = 483.047144.

Percentage change in Delivered order count = ((383,530 - 286,712) / 286,712) * 100 = 33.71...

**B ✗:** For delivered orders in INR currency in 2025:

- January: 
  - Delivered order count: 286,712
  - GMV: 138,573,283.00 INR
  - AOV: 483.318741 INR
- December:
  - Delivered order count: 383,530
  - GMV: 185,263,071.00 INR
  - AOV: 483.047144 INR

Percentage change from January to December:
- Delivere...

**C ✗:** No delivered orders in INR were found for either January or December 2025. As a result, the delivered order count, GMV in INR, and AOV in INR are all zero or unavailable for both months. Therefore, the percentage change for both delivered order count and AOV from January to December cannot be calcul...

**D ✗:** For January 2025:
- Delivered order count: 286,712
- GMV in INR: 138,573,283.00
- AOV in INR: 483.318741

For December 2025:
- Delivered order count: 383,530
- GMV in INR: 185,263,071.00
- AOV in INR: 483.047144

Percentage change from January to December:
- Delivered order count: ((383,530 - 286,71...

**E ✗:** For January 2025 (INR):
- Delivered order count: 286,712
- GMV: 138,573,283 INR
- AOV: 483.318741 INR

For December 2025 (INR):
- Delivered order count: 383,530
- GMV: 185,263,071 INR
- AOV: 483.047144 INR

Percentage change from January to December:
- Delivered order count: ((383,530 - 286,712) / 2...

**F ✗:** For January 2025 (INR):
- Delivered order count: 286,712
- GMV: 138,573,283 INR
- AOV: 483.318741 INR

For December 2025 (INR):
- Delivered order count: 383,530
- GMV: 185,263,071 INR
- AOV: 483.047144 INR

Percentage change from January to December:
- Delivered order count: ((383,530 - 286,712) / 2...

</details>

## Q08

**Kunci dan cakupan:**

Bangalore: 440.743 order, INR 233.341.258, AOV INR 529,42703117. Delhi: 339.384, INR 177.702.873, AOV INR 523,60415635. Chennai: 310.963, INR 155.055.243, AOV INR 498,62923563.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Bikaner/granular city (bukan Bangalore, Delhi, Chennai) |
| B | 1 | 1 | 1 | 1.000 ✓ | Bangalore, Delhi, Chennai benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Bangalore, Delhi, Chennai benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Bangalore, Delhi, Chennai benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Bangalore, Delhi, Chennai benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Bangalore, Delhi, Chennai benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bikaner: Delivered-order GMV = 29,030,997 INR, Delivered order count = 49,057, AOV = 591.780928 INR
2. Indiranagar,Bangalore: Delivered-order GMV = 22,092,650 INR, Delivered order count = 36,998, AOV = 597.130926 IN...

**B ✓:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bangalore: Delivered GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
2. Delhi: Delivered GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
3. Chennai: De...

**C ✓:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bangalore: Delivered GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
2. Delhi: Delivered GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
3. Chennai: De...

**D ✓:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bangalore: Delivered GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
2. Delhi: Delivered GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
3. Chennai: De...

**E ✓:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bangalore: GMV = 233,341,258.00 INR, Delivered order count = 440,743, AOV = 529.427031 INR
2. Delhi: GMV = 177,702,873.00 INR, Delivered order count = 339,384, AOV = 523.604156 INR
3. Chennai: GMV = 155,055,243.00 I...

**F ✓:** For 2025, the top three order-recorded cities by Delivered-order GMV in INR are:

1. Bangalore: GMV = 233,341,258 INR, Delivered order count = 440,743, AOV = 529.427031 INR
2. Delhi: GMV = 177,702,873 INR, Delivered order count = 339,384, AOV = 523.604156 INR
3. Chennai: GMV = 155,055,243 INR, Deliv...

</details>

## Q09

**Kunci dan cakupan:**

**Hyderabad**: 319.122 order, 19.236 Cancelled, **6,027789%** cancel. Overall: **5,997009%**. Gap: **+0,030780 pp**.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Bikaner (salah kota) |
| B | 1 | 1 | 1 | 1.000 ✓ | Hyderabad 6,027789% benar |
| C | 0 | 1 | 1 | 0.667 ~ | Rep1 Bangalore salah, rep2–3 Hyderabad benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Hyderabad 6,027789% benar |
| E | 1 | 1 | 0 | 0.667 ~ | Rep3 timeout/unavailable |
| F | 1 | 1 | 1 | 1.000 ✓ | Hyderabad 6,027789% benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** Among cities with at least 50,000 total orders in 2025, Bikaner had the highest cancellation rate. Bikaner had 53,571 orders and a cancellation rate of 0.000000 (0/53,571). The overall 2025 cancellation rate across all cities was also 0.000000 (0/4,359,773). The gap versus the overall 2025 cancellat...

**B ✓:** Among cities with at least 50,000 total orders recorded in 2025, Hyderabad had the highest cancellation rate. Hyderabad had 319,122 orders, with a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate was 0.059970 (5.9970%). The gap between Hyderabad's cancellation rate and the...

**C ~:** Among cities with at least 50,000 total orders in 2025, Bangalore had the highest cancellation rate.

- City: Bangalore
- Order count: 481,626
- Cancellation rate: 0.059857 (5.9857%)

The overall 2025 cancellation rate across all cities was 0.059991 (5.9991%).

- Gap versus overall: -0.0134 percenta...

**D ✓:** Among cities with at least 50,000 total orders recorded in 2025, Hyderabad had the highest cancellation rate. Hyderabad had 319,122 orders and a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate across all cities was 0.059970 (5.9970%). The gap between Hyderabad's cancellat...

**E ~:** Among order-recorded cities with at least 50,000 total orders in 2025, Hyderabad had the highest cancellation rate. Hyderabad recorded 319,122 orders with a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate was 0.059970 (5.9970%). The gap between Hyderabad's cancellation ra...

**F ✓:** Among order-recorded cities with at least 50,000 total orders in 2025, Hyderabad had the highest cancellation rate. It recorded 319,122 orders, with a cancellation rate of 0.060278 (6.0278%). The overall 2025 cancellation rate across all cities was 0.059970 (5.9970%). The gap between Hyderabad's can...

</details>

## Q10

**Kunci dan cakupan:**

Bangalore: 31,0560894 mnt. Delhi: 31,0484820 mnt. **Bangalore lebih lambat 0,0076074 mnt** (~0,46 dtk).

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Tidak menemukan delivery duration data |
| B | 1 | 1 | 1 | 1.000 ✓ | Bangalore 31,056 mnt, Delhi 31,048 mnt benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Bangalore 31,056 mnt, Delhi 31,048 mnt benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Bangalore 31,056 mnt, Delhi 31,048 mnt benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Bangalore 31,056 mnt, Delhi 31,048 mnt benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Bangalore 31,056 mnt, Delhi 31,048 mnt benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** There are no delivered orders in 2025 with a recorded delivery duration for either Bangalore or Delhi in the available data. Therefore, a comparison of average delivery times between these cities for 2025 cannot be made.

**B ✓:** In 2025, for delivered orders with a recorded delivery duration, Bangalore had an average delivery time of 31.056089 minutes, while Delhi had an average of 31.048482 minutes. Bangalore was slower by 0.007607 minutes (about 0.46 seconds). The difference is very small, but Bangalore was marginally slo...

**C ✓:** For delivered orders in 2025 with a recorded delivery duration, the average delivery time in Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small, indicating nearly identica...

**D ✓:** For delivered orders in 2025 with a recorded delivery duration, the average delivery time was 31.056089 minutes in Bangalore and 31.048482 minutes in Delhi. Bangalore was slower by 0.007607 minutes (about 0.46 seconds). The difference is very small, but Bangalore had the slightly higher average deli...

**E ✓:** For delivered orders in 2025 with a recorded delivery duration, the average delivery time in Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small and likely not operationall...

**F ✓:** For Delivered orders in 2025 with a recorded delivery duration, the average delivery time in order-recorded Bangalore was 31.056089 minutes, and in Delhi it was 31.048482 minutes. Bangalore was slower than Delhi by 0.007607 minutes (about 0.46 seconds). The difference is extremely small, indicating ...

</details>

## Q11

**Kunci dan cakupan:**

Delivered: 3.989.077 order, 70,030461% rated, rata-rata 4,14547985. Cancelled: 261.456, 0%, **undefined**. Refunded: 109.240, 0%, **undefined**.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders; 70.0305% had a non-null customer rating; average customer rating among rated orders was 4.145479850327663.
- Cancelled: 261,456 total orders; 0% had a non-null customer rating; no average rating (none rated).
- Refunded: 1...

**B ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders; 70.030461% had a non-null customer rating; average customer rating among rated orders was 4.145480. This average describes only the 2,793,569 delivered orders in 2025 that received a customer rating.
- Cancelled: 261,456 t...

**C ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders; 70.0305% had a non-null customer rating; average customer rating among rated orders was 4.14547985. The average describes the 2,793,569 delivered orders in 2025 that received a customer rating.
- Cancelled: 261,456 total o...

**D ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders; 70.0305% had a non-null customer rating; average customer rating among rated orders was 4.145480.
- Cancelled: 261,456 total orders; 0% had a non-null customer rating; no average rating (none rated).
- Refunded: 109,240 to...

**E ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders; 70.030461% of these had a non-null customer rating; the average customer rating among rated delivered orders was 4.145480. This average describes only delivered orders in 2025 that received a numeric customer rating (about...

**F ✓:** For each recorded order status in 2025:

- Delivered: 3,989,077 total orders. 70.030461% of these had a non-null customer rating. The average customer rating among rated Delivered orders was 4.14547985.
- Cancelled: 261,456 total orders. 0.0% had a non-null customer rating. No average rating is repo...

</details>

## Q12

**Kunci dan cakupan:**

Top 10 restoran: **INR 3.552.103** dari total **INR 1.926.466.048**; share **0,18438441%**.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 0 | 0 | 0.333 ~ | Sebagian benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ~:** For 2025 Delivered orders in INR:
- The top ten restaurants by GMV (ranked by GMV, then R_ID) generated a combined GMV of 3,552,107 INR (sum of: 444,796 + 407,677 + 387,457 + 365,456 + 360,967 + 320,494 + 319,035 + 315,964 + 315,251 + 315,006).
- The total GMV from all restaurants was 1,926,466,048 ...

**B ✓:** For 2025 delivered orders in INR, the top ten restaurants by delivered GMV (ranked by GMV, then restaurant ID) generated a combined GMV of 3,552,107.00 INR. The total delivered GMV in INR for all restaurants in 2025 was 1,926,466,048.00 INR. Thus, the share of delivered GMV from the top ten restaura...

**C ✓:** In 2025, the top ten restaurants by delivered-order GMV in INR generated a combined GMV of 3,552,103 INR. The total delivered-order GMV in INR for all restaurants was 1,926,466,048 INR. The share of delivered-order GMV from the top ten restaurants was 0.001845 (or 0.1845%). This means that the top t...

**D ✓:** In 2025, the top ten restaurants by delivered-order GMV in INR contributed a combined GMV of 3,552,103.00 INR out of a total delivered-order GMV of 1,926,466,048.00 INR. This means the top ten accounted for 0.00184384 (or about 0.184384%) of the total delivered-order GMV in INR. The population is al...

**E ✓:** The top ten restaurants by 2025 delivered-order GMV in INR (ranked by GMV, then restaurant ID) contributed a combined GMV of 3,552,107 INR. The total delivered-order GMV in INR for all restaurants in 2025 was 1,926,466,048 INR. Thus, the top ten restaurants accounted for approximately 0.001844 (or 0...

**F ✓:** The top ten restaurants by 2025 Delivered-order GMV in INR (ranked by GMV, then restaurant ID) are: 437065, 22964, 4484, 16214, 223614, 198307, 84365, 4955, 16344, and 4813. Their combined Delivered-order GMV is 3,552,107 INR. The total Delivered-order GMV in INR for all restaurants in 2025 is 1,926...

</details>

## Q13

**Kunci dan cakupan:**

"North Indian,Chinese": 202.651 total order, 5,880060% cancel, GMV INR 97.195.380. "Indian,Chinese": 126.766, 5,981888%, INR 60.447.386. "Indian": 148.932, 6,000054%, INR 58.362.786.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Total order salah (pakai Delivered saja, bukan total order) |
| B | 0 | 0 | 0 | 0.000 ✗ | Total order salah (pakai Delivered saja, bukan total order) |
| C | 0 | 0 | 0 | 0.000 ✗ | Total order salah (pakai Delivered saja, bukan total order) |
| D | 1 | 1 | 1 | 1.000 ✓ | NIC 202.651, IC/I GMV benar |
| E | 1 | 1 | 1 | 1.000 ✓ | NIC 202.651, IC/I GMV benar |
| F | 1 | 1 | 1 | 1.000 ✓ | NIC 202.651, IC/I GMV benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:

1. "North Indian,Chinese":
   - GMV: 97,195,380.00 INR
   - Total delivered orders: 185,649
   - Cancellation rate: 0.000000 (no cancellations)

2. "Indian,Chinese":
   - GMV: 60,447,386.00 INR
   - Total delivered...

**B ✗:** The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:

1. "North Indian,Chinese":
   - GMV: 97,195,380.00 INR
   - Total delivered orders: 185,649
   - Cancellation rate: 0.000000 (0%)

2. "Indian,Chinese":
   - GMV: 60,447,386.00 INR
   - Total delivered orders: 116,0...

**C ✗:** The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:

1. "North Indian,Chinese":
   - Delivered GMV: 97,195,380.00 INR
   - Total Delivered Orders: 185,649
   - Cancellation Rate: 0.000000 (0%)

2. "Indian,Chinese":
   - Delivered GMV: 60,447,386.00 INR
   - Total Del...

**D ✓:** The three exact cuisine labels with the highest 2025 delivered-order GMV in INR are:

1. North Indian,Chinese
   - Delivered GMV (INR): 97,195,380.00
   - Total order count: 202,651
   - Cancellation rate: 0.058800 (11,916 cancelled / 202,651 total)

2. Indian,Chinese
   - Delivered GMV (INR): 60,44...

**E ✓:** The three exact cuisine labels with the highest 2025 delivered-order GMV in INR are:

1. "North Indian,Chinese":
   - Delivered-order GMV: 97,195,380.00 INR
   - Total order count: 202,651
   - Cancellation rate: 0.058801 (5.8801%)

2. "Indian,Chinese":
   - Delivered-order GMV: 60,447,386.00 INR
  ...

**F ✓:** The three exact cuisine labels with the highest 2025 Delivered-order GMV in INR are:

1. "North Indian,Chinese":
   - Delivered-order GMV: 97,195,380.00 INR
   - Total order count: 202,651
   - Cancellation rate: 0.058801 (5.8801%)

2. "Indian,Chinese":
   - Delivered-order GMV: 60,447,386.00 INR
  ...

</details>

## Q14

**Kunci dan cakupan:**

Veg: 7.277.939 lines, 8.877.759 units, **72,584811%**. Non-Veg: 2.749.222 lines, 3.353.105 units, **27,415082%**. Unknown: 12 lines, 13 units, 0,000106%. Denominator: 12.230.877.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |
| B | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |
| C | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |
| D | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |
| E | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |
| F | 0 | 0 | 0 | 0.000 ✗ | Share Veg/Non-Veg meleset >0,01 pp (perlu denominasi tepat) |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For item lines in 2025 orders, classified by Veg/Non-Veg/Unknown (based on food dimension join):

- Veg: 7,277,939 item lines, 8,877,759 ordered units, share = 72.626964% of total ordered units
- Unknown: 2,749,234 item lines, 3,353,118 ordered units, share = 27.373036% of total ordered units
- Non-...

**B ✗:** For item lines in 2025 orders, classified by Veg/Non-Veg/Unknown (null or unmatched food ID):

- Veg:
  - Item-line count: 7,277,939
  - Total ordered units: 8,877,759
  - Share of total ordered units: 72.626964% 

- Non-Veg:
  - Item-line count: 2,749,222
  - Total ordered units: 3,353,105
  - Shar...

**C ✗:** For item lines belonging to 2025 orders, classified by Veg/Non-Veg/Unknown (null or unmatched food ID):

- Veg: 
  - Item-line count: 7,277,939
  - Total ordered units: 8,877,759
  - Share of total ordered units: 72.626857% 

- Non-Veg:
  - Item-line count: 2,749,222
  - Total ordered units: 3,353,1...

**D ✗:** For item lines belonging to 2025 orders, classified by Veg/Non-Veg/Unknown (null or unmatched food ID):

- Veg:
  - Item-line count: 7,277,939
  - Total ordered units: 8,877,759
  - Share of total ordered units: 72.626964% (8,877,759 / 12,231,877 * 100)

- Non-Veg:
  - Item-line count: 2,749,222
  -...

**E ✗:** For item lines belonging to 2025 orders, the classification and aggregation by food type are as follows:

- Veg:
  - Item-line count: 7,277,939
  - Total ordered units: 8,877,759
  - Share of total ordered units: (8,877,759 / 12,230,877) × 100 = 72.573857%

- Non-Veg:
  - Item-line count: 2,749,222
...

**F ✗:** For item lines belonging to 2025 orders, classified by Veg/Non-Veg/Unknown (null or unmatched food ID):

- Veg:
  - Item-line count: 7,277,939
  - Total ordered units: 8,877,759
  - Share of total ordered units: (8,877,759 / 12,230,877) × 100 = 72.573857%

- Non-Veg:
  - Item-line count: 2,749,222
 ...

</details>

## Q15

**Kunci dan cakupan:**

Multi-line: **3.052.089 orders, 70,005686%**, avg 3,484769 units. One-line: 1.307.684, 29,994314%, avg 1,219753. Zero-line: 0 orders.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 1 | 0 | 0.333 ~ | Rep1: count multi salah (2.941.089); rep2 OK, rep3 share 70,026% (luar toleransi) |
| B | 0 | 1 | 1 | 0.667 ~ | Rep2–3 OK; rep1 70,02% (luar toleransi) |
| C | 1 | 1 | 1 | 1.000 ✓ | 3.052.089, 70,006% benar |
| D | 1 | 1 | 1 | 1.000 ✓ | 3.052.089, 70,006% benar |
| E | 1 | 1 | 1 | 1.000 ✓ | 3.052.089, 70,006% benar |
| F | 0 | 0 | 0 | 0.000 ✗ | Share 70,036%/70,032%/70,026% (semua luar ±0,01 pp) |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ~:** In 2025, among all orders:

- Orders with exactly one item line: 1,307,684 orders (average units per order: 1.219753)
- Orders with more than one item line: 2,941,089 orders (sum of orders with 2–6 item lines; average units per order for these orders: weighted average = (2*1,483,215 + 3*871,006 + 4*...

**B ~:** In 2025, there were no orders with zero item lines (no such rows were returned). Out of all orders:

- 1,307,684 orders (29.98%) had exactly one item line, with an average of 1.219753 units per order.
- 3,052,089 orders (70.02%) had more than one item line, with an average of 3.484769 units per orde...

**C ✓:** In 2025, there were no orders with zero item lines (none reported in the data). Out of all orders:
- 1,307,684 orders (29.99%) had exactly one item line, with an average of 1.219753 units per order.
- 3,052,089 orders (70.01%) had more than one item line, with an average of 3.484769 units per order....

**D ✓:** In 2025, among orders with item line data:

- Orders with more than one item line ("Multi item line") made up 3052089 out of (1307684 + 3052089 = 4359773) orders, or 70.025857% of orders.
- Orders with exactly one item line ("One item line") made up 1307684 orders, or 29.974143% of orders.
- No orde...

**E ✓:** In 2025, there were no orders with zero item lines (no such group appeared in the data). Out of all orders:
- 1,307,684 orders (about 30%) contained exactly one item line.
- 3,052,089 orders (about 70%) contained more than one item line.

Share of orders with more than one item line: 3,052,089 / (1,...

**F ✗:** In 2025, among all recorded orders:

- Orders with one item line: 1,307,684 orders (average ordered units per order: 1.219753)
- Orders with multiple item lines: 3,052,089 orders (average ordered units per order: 3.484769)
- Orders with no item line: 0 orders (none observed in the data)

Share of or...

</details>

## Q16

**Kunci dan cakupan:**

**21.466 item lines** non-zero diff; signed sum **+INR 23.791**; abs sum **INR 23.791**. Tidak ada offset; semua positif.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | 21.466 lines, ±INR 23.791 benar |
| B | 0 | 0 | 0 | 0.000 ✗ | Filter INR menghasilkan 14.321 (bukan 21.466) |
| C | 0 | 0 | 0 | 0.000 ✗ | Filter INR menghasilkan 0 baris (salah) |
| D | 1 | 1 | 1 | 1.000 ✓ | 21.466 lines, ±INR 23.791 benar |
| E | 1 | 1 | 1 | 1.000 ✓ | 21.466 lines, ±INR 23.791 benar |
| F | 1 | 1 | 1 | 1.000 ✓ | 21.466 lines, ±INR 23.791 benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** Among item lines belonging to 2025 orders, there are 21,466 item lines where the recorded line amount differs from price times quantity. The signed sum of these differences is 23,791.0 INR, and the absolute sum is also 23,791.0 INR. Since the signed sum and absolute sum are equal, all differences ar...

**B ✗:** Among item lines belonging to 2025 orders in INR, there are 14,321 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. Since the signed sum and absolute sum ...

**C ✗:** Among item lines belonging to 2025 orders, there are 0 item lines with a non-zero difference between the recorded line amount and price times quantity in INR. Both the signed sum and the absolute sum of those differences are null (effectively zero). Therefore, there is no offset between positive and...

**D ✓:** Among item lines belonging to 2025 orders, 21,466 have a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. Since the signed sum and absolute sum are equal, all differences a...

**E ✓:** Among item lines belonging to 2025 orders, there are 21,466 item lines with a non-zero difference between the recorded line amount and price times quantity. The signed sum of those differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. All 21,466 differences are positive, with non...

**F ✓:** Among item lines belonging to 2025 orders, there are 21,466 item lines where the recorded line amount differs from price times quantity. The signed sum of these differences is 23,791.00 INR, and the absolute sum is also 23,791.00 INR. This means all differences are positive in this snapshot—there is...

</details>

## Q17

**Kunci dan cakupan:**

**Zero** non-zero differences untuk setiap status. Signed sum = INR 0. Rekonsiliasi sempurna.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** For all 2025 orders in INR, the recorded sales amount exactly matches the formula (subtotal - discount + delivery fee + GST) for every order status. There are zero orders with a non-zero difference for any order status, and the signed sum of differences is zero in all cases. This indicates perfect r...

**B ✓:** For all 2025 orders in INR, the recorded sales amount exactly matches subtotal minus discount plus delivery fee plus GST for every order status. There are zero non-zero differences for each status (Cancelled, Delivered, Refunded), and the signed sum of differences is 0.0 INR in all cases. This indic...

**C ✓:** For all 2025 orders in INR, the recorded sales amount reconciles exactly to subtotal minus discount plus delivery fee plus GST for every order status. There are zero orders with a non-zero difference for any order status, and the signed sum of differences is zero INR for all statuses. This indicates...

**D ✓:** For 2025, there are no orders in INR with a non-zero difference between the recorded sales amount and the calculation (subtotal minus discount plus delivery fee plus GST) for any order status. This means the recorded sales amount reconciles exactly to the formula for all orders in INR, across all or...

**E ✓:** For all 2025 orders in INR, there are no orders with a non-zero difference between the recorded sales amount and the calculation (subtotal minus discount plus delivery fee plus GST) for any order status. This means the recorded sales amount fully reconciles to the expected calculation for every orde...

**F ✓:** For 2025, there are no orders in INR currency where the recorded order sales amount differs from the calculation (subtotal minus discount plus delivery fee plus GST) for any order status. This means that for every order status, the count of non-zero differences is zero and the signed sum of those di...

</details>

## Q18

**Kunci dan cakupan:**

Gen Z: 2.222.349 order, INR 1.073.372.395, AOV INR 482,99002317. Millennial: 1.766.728, INR 853.093.653, AOV INR 482,86643615. **Hanya dua segmen.**

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Pakai usia numerik (23, 22, 25) bukan label Gen Z/Millennial |
| B | 0 | 0 | 0 | 0.000 ✗ | Beberapa rep pakai segmen income (No Income), bukan age |
| C | 1 | 1 | 1 | 1.000 ✓ | Gen Z 2.222.349, Millennial 1.766.728 benar |
| D | 1 | 1 | 1 | 1.000 ✓ | Gen Z 2.222.349, Millennial 1.766.728 benar |
| E | 1 | 1 | 1 | 1.000 ✓ | Gen Z 2.222.349, Millennial 1.766.728 benar |
| F | 1 | 1 | 1 | 1.000 ✓ | Gen Z 2.222.349, Millennial 1.766.728 benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For 2025 Delivered orders in INR, the top three customer age segments by Delivered order count are:

1. Age 23: 747,305 Delivered orders, GMV of 361,091,281 INR, and AOV of 483.191309 INR.
2. Age 22: 590,755 Delivered orders, GMV of 285,775,099 INR, and AOV of 483.745544 INR.
3. Age 25: 542,236 Deli...

**B ✗:** For 2025 delivered orders in INR, the top three customer age segments by delivered order count are:

1. Segment: No Income
   - Delivered order count: 1,912,848
   - GMV: 924,154,150 INR
   - AOV: 483.129946 INR

2. Segment: 25001 to 50000
   - Delivered order count: 715,156
   - GMV: 345,622,936 IN...

**C ✓:** For 2025 delivered orders in INR, the top customer age segments by delivered order count are:

1. Gen Z: 2,222,349 delivered orders, GMV of 1,073,372,395.00 INR, and AOV (average order value) of 482.990023 INR.
2. Millennial: 1,766,728 delivered orders, GMV of 853,093,653.00 INR, and AOV of 482.8664...

**D ✓:** For 2025 delivered orders in INR, the top customer age segments by delivered order count are:

1. Gen Z: 2,222,349 delivered orders, GMV of 1,073,372,395.00 INR, and AOV (average order value) of 482.990023 INR.
2. Millennial: 1,766,728 delivered orders, GMV of 853,093,653.00 INR, and AOV of 482.8664...

**E ✓:** For 2025 delivered orders in INR, the top customer age segments by delivered order count are:

1. Gen Z: 2,222,349 delivered orders, GMV 1,073,372,395 INR, AOV 482.990023 INR
2. Millennial: 1,766,728 delivered orders, GMV 853,093,653 INR, AOV 482.866436 INR

Only two age segments had delivered order...

**F ✓:** For 2025 Delivered orders in INR, the top customer age segments by Delivered order count are:

1. Gen Z: 2,222,349 Delivered orders, GMV 1,073,372,395 INR, AOV 482.990023 INR
2. Millennial: 1,766,728 Delivered orders, GMV 853,093,653 INR, AOV 482.866436 INR

Only two age segments occurred in the dat...

</details>

## Q19

**Kunci dan cakupan:**

Sabtu tertinggi: **14.486,211538**. Minggu: 13.119,134615. Jumat: 12.228,980769. Kamis: 9.473,653846. Senin: 9.094,365385. Selasa: 9.082,788462. Rabu: 9.053,773585.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | Sabtu 14.486,211538 tertinggi benar |
| B | 1 | 1 | 1 | 1.000 ✓ | Sabtu 14.486,211538 tertinggi benar |
| C | 1 | 1 | 1 | 1.000 ✓ | Sabtu 14.486,211538 tertinggi benar |
| D | 0 | 0 | 0 | 0.000 ✗ | Merata-ratakan data mart kota-hari (28,95/hari), bukan order total per hari |
| E | 1 | 1 | 1 | 1.000 ✓ | Sabtu 14.486,211538 tertinggi benar |
| F | 0 | 0 | 0 | 0.000 ✗ | Sunday 13.111 (bukan 13.119), Friday 12.230 (bukan 12.229), dll. |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** Across every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders for each weekday was:
- Saturday: 14486.211538 orders
- Sunday: 13119.134615 orders
- Friday: 12228.980769 orders
- Thursday: 9473.653846 orders
- Monday: 9094.365385 orders
- Tues...

**B ✓:** For every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders for each weekday was:
- Saturday: 14,486.211538
- Sunday: 13,119.134615
- Friday: 12,228.980769
- Thursday: 9,473.653846
- Monday: 9,094.365385
- Tuesday: 9,082.788462
- Wednesday: 9,...

**C ✓:** For every calendar date in 2025, including dates with zero Delivered orders, the average number of Delivered orders per weekday was:
- Saturday: 14,486.211538
- Sunday: 13,119.134615
- Friday: 12,228.980769
- Thursday: 9,473.653846
- Monday: 9,094.365385
- Tuesday: 9,082.788462
- Wednesday: 9,053.77...

**D ✗:** For every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders per weekday was:
- Saturday: 28.951266
- Sunday: 26.654489
- Friday: 25.030781
- Thursday: 20.140229
- Monday: 19.475620
- Wednesday: 19.419263
- Tuesday: 19.405275

Saturday had the ...

**E ✓:** Across every calendar date in 2025 (including dates with zero Delivered orders), the average number of Delivered orders for each weekday was:
- Saturday: 14486.211538
- Sunday: 13119.134615
- Friday: 12228.980769
- Thursday: 9473.653846
- Monday: 9094.365385
- Tuesday: 9082.788462
- Wednesday: 9053....

**F ✗:** To find the average number of Delivered orders for each weekday in 2025 (including dates with zero Delivered orders), we divide the total Delivered orders for each weekday by the number of times that weekday occurs in 2025:

- Friday: 635,907 / 52 = 12,229.942308
- Monday: 472,907 / 52 = 9,094.36538...

</details>

## Q20

**Kunci dan cakupan:**

Jan→Feb terbesar negatif: **−INR 9.159.198**. Jan: 286.712 order, INR 138.573.283, AOV INR 483,31874145. Feb: 268.570, INR 129.414.085, AOV INR 481,86351789. Count effect: **−INR 8.768.368,61**; AOV effect: **−INR 390.829,39**. Sum = observed change. Toleransi ±INR 0,05 per komponen.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Count effect −8.771.964 (salah, seharusnya −8.768.368) |
| B | 0 | 0 | 0 | 0.000 ✗ | Count effect −8.771.964 (salah, seharusnya −8.768.368) |
| C | 0 | 0 | 1 | 0.333 ~ | Rep3: count effect −8.768.368,61, AOV effect −390.829,39 benar |
| D | 0 | 0 | 0 | 0.000 ✗ | Count effect −8.771.964 (salah, seharusnya −8.768.368) |
| E | 0 | 0 | 0 | 0.000 ✗ | Count effect −8.771.964 (salah, seharusnya −8.768.368) |
| F | 0 | 0 | 0 | 0.000 ✗ | Count effect −8.771.964 (salah, seharusnya −8.768.368) |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For 2025, the month-over-month delivered-order GMV change in INR for all eleven consecutive month pairs is as follows (GMV in INR):
- Jan→Feb: 129,414,085.0 - 138,573,283.0 = -9,159,198.0
- Feb→Mar: 149,731,681.0 - 129,414,085.0 = +20,317,596.0
- Mar→Apr: 145,794,592.0 - 149,731,681.0 = -3,937,089.0...

**B ✗:** 1. Month-over-month Delivered-order GMV (INR) changes for 2025:
- Jan→Feb: 129,414,085 - 138,573,283 = -9,159,198
- Feb→Mar: 149,731,681 - 129,414,085 = +20,317,596
- Mar→Apr: 145,794,592 - 149,731,681 = -3,937,089
- Apr→May: 158,447,281 - 145,794,592 = +12,652,689
- May→Jun: 156,551,606 - 158,447,2...

**C ~:** 1. Month-over-month delivered-order GMV changes in INR for 2025:
- Jan→Feb: -9,159,198.00
- Feb→Mar: +20,317,596.00
- Mar→Apr: -3,937,089.00
- Apr→May: +12,652,689.00
- May→Jun: -1,895,675.00
- Jun→Jul: +6,543,551.00
- Jul→Aug: +10,819,780.00
- Aug→Sep: -6,605,507.00
- Sep→Oct: +10,821,624.00
- Oct→...

**D ✗:** Step 1: Compute month-over-month GMV change in INR for each consecutive month pair in 2025:

- Jan→Feb: 129,414,085 - 138,573,283 = -9,159,198
- Feb→Mar: 149,731,681 - 129,414,085 = +20,317,596
- Mar→Apr: 145,794,592 - 149,731,681 = -3,937,089
- Apr→May: 158,447,281 - 145,794,592 = +12,652,689
- May...

**E ✗:** To compute the month-over-month (MoM) delivered-order GMV change in INR for all eleven consecutive month pairs in 2025, we first sort the months chronologically and calculate the GMV difference for each pair:

Sorted months and GMV (INR):
- Jan: 138,573,283.0
- Feb: 129,414,085.0
- Mar: 149,731,681....

**F ✗:** To compute the month-over-month Delivered-order GMV change in INR for all eleven consecutive month pairs in 2025, we first align the months and calculate the GMV change for each pair:

Month pairs and GMV (INR):
- Jan→Feb: 138,573,283 → 129,414,085 (Change: -9,159,198)
- Feb→Mar: 129,414,085 → 149,7...

</details>

## Q21

**Kunci dan cakupan:**

r = **−0,0200303**; 12 bulan; tidak mendukung klaim kausalitas.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 1 | 1 | 1 | 1.000 ✓ | r=−0,02003 benar, 12 bulan, tidak kausal |
| B | 1 | 1 | 1 | 1.000 ✓ | r=−0,02003 benar, 12 bulan, tidak kausal |
| C | 1 | 0 | 1 | 0.667 ~ | Rep2 null (tidak dapat dihitung); rep1,3 r=−0,02000 benar |
| D | 0 | 1 | 0 | 0.333 ~ | Rep1,3 null; rep2 r=−0,02003 benar |
| E | 1 | 1 | 1 | 1.000 ✓ | r=−0,02003 benar, 12 bulan, tidak kausal |
| F | 1 | 1 | 1 | 1.000 ✓ | r=−0,02003 benar, 12 bulan, tidak kausal |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✓:** The Pearson correlation coefficient between monthly cancellation rate and average delivered-order delivery time across the twelve calendar months of 2025 is -0.0199979. This calculation used data from all 12 months (January to December 2025). The correlation is very close to zero, indicating almost ...

**B ✓:** The Pearson correlation coefficient between monthly cancellation rate and average delivered-order delivery time across the twelve calendar months of 2025 is -0.02003284030764907. This calculation used all 12 months in 2025. This correlation is very close to zero, indicating almost no linear relation...

**C ~:** The Pearson correlation coefficient between monthly cancellation rate and average delivered-order delivery time across the twelve calendar months of 2025 is -0.01999787909651581. This calculation used all 12 months in 2025. The correlation is very close to zero, indicating almost no linear relations...

**D ~:** The Pearson correlation coefficient between monthly cancellation rate and average delivered-order delivery time across the twelve calendar months of 2025 is null (not computable). All 12 months were included in the analysis. A null correlation indicates that there was insufficient variation or data ...

**E ✓:** The Pearson correlation coefficient between monthly cancellation rate and average Delivered-order delivery time across the twelve calendar months of 2025 is -0.01999788. This calculation used all 12 months of 2025. The correlation is very close to zero, indicating almost no linear relationship betwe...

**F ✓:** The Pearson correlation coefficient between monthly cancellation rate and average Delivered-order delivery time across the twelve calendar months of 2025 is -0.01999788. This calculation used all 12 months of 2025. A correlation coefficient near zero indicates almost no linear relationship between t...

</details>

## Q22

**Kunci dan cakupan:**

(Standard market = restoran dengan `rating_count >= 100`) **1.848.107 order**, **INR 927.955.016 GMV**, **AOV INR 502,11108772**.

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Tidak memiliki aturan standard market (menghasilkan angka full market) |
| B | 0 | 0 | 0 | 0.000 ✗ | Tidak memiliki aturan standard market (menghasilkan angka full market) |
| C | 0 | 0 | 0 | 0.000 ✗ | Tidak memiliki aturan standard market (menghasilkan angka full market) |
| D | 0 | 0 | 0 | 0.000 ✗ | Tidak memiliki aturan standard market (menghasilkan angka full market) |
| E | 0 | 0 | 0 | 0.000 ✗ | Tidak memiliki aturan standard market (menghasilkan angka full market) |
| F | 1 | 1 | 1 | 1.000 ✓ | Menerapkan rating_count≥100: 1.848.107 order, INR 927.955.016 |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For the standard market report covering 2025, applying the standard market eligibility rule (Delivered orders in INR currency) to all metrics: 
- Delivered-order GMV in INR: 1,926,466,048.0 INR
- Delivered order count: 3,989,077 orders
- AOV (Average Order Value): 482.935288 INR per order

Populatio...

**B ✗:** For the standard market report covering 2025, applying the standard market eligibility rule (delivered, not cancelled, not refunded, INR orders):
- Delivered-order GMV in INR: 1,926,466,048.00 INR
- Delivered order count: 3,989,077 orders
- Delivered AOV (Average Order Value): 482.935288 INR per ord...

**C ✗:** For the standard market report covering 2025, applying the standard market eligibility rule (delivered orders in INR) to all metrics:
- Delivered-order GMV in INR: 1,926,466,048.00 INR
- Delivered order count: 3,989,077 orders
- AOV (Average Order Value): 482.935288 INR per order

Population: All de...

**D ✗:** For the standard market report covering 2025, applying the standard market eligibility rule (INR currency) to all metrics: 
- Delivered-order GMV in INR: 1,926,466,048.00 INR
- Delivered order count: 3,989,077 orders
- Delivered AOV (Average Order Value): 482.935288 INR per delivered order

Populati...

**E ✗:** For the standard market report covering 2025, applying the standard market eligibility rule (delivered orders, INR currency) to all metrics:
- Delivered-order GMV in INR: 1,926,466,048.00 INR
- Delivered order count: 3,989,077 orders
- AOV (Average Order Value): 483.012964 INR per delivered order (c...

**F ✓:** For the standard market report in 2025 (applying the eligibility rule: only restaurants with at least 100 recorded ratings), the results for Delivered orders in INR are as follows: 
- Delivered-order GMV: 927,955,016.00 INR
- Delivered order count: 1,848,107
- AOV (Average Order Value): 502.11108772...

</details>

## Q23

**Kunci dan cakupan:**

Standard market, kota restoran: Bangalore INR 129.604.607 (13,96669071%), Chennai INR 92.523.985 (9,97074033%), Hyderabad INR 79.925.454 (8,61307419%).

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Pakai order city (Bikaner, Indiranagar) bukan restaurant city |
| B | 0 | 0 | 0 | 0.000 ✗ | Pakai full market tanpa filter (Bangalore/Delhi/Chennai bukan standard market) |
| C | 0 | 0 | 0 | 0.000 ✗ | Pakai full market tanpa filter (Bangalore/Delhi/Chennai bukan standard market) |
| D | 0 | 0 | 0 | 0.000 ✗ | Pakai full market tanpa filter (Bangalore/Delhi/Chennai bukan standard market) |
| E | 0 | 0 | 0 | 0.000 ✗ | Pakai full market tanpa filter (Bangalore/Delhi/Chennai bukan standard market) |
| F | 1 | 1 | 1 | 1.000 ✓ | Bangalore/Chennai/Hyderabad dengan GMV benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:

1. Bikaner: GMV = 29,030,997 INR, Share = 0.0150702 (1.50702%)
2. Indiranagar,Bangalore: GMV = 22,092,650 INR, Share = 0.0114702 (1.14702%)
3. Koramangala,Bangalore: GMV = 18,686,823 INR, Share = 0.0096...

**B ✗:** In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:

1. Bangalore: GMV = 233,341,258 INR (share: 0.121158)
2. Delhi: GMV = 177,702,873 INR (share: 0.092263)
3. Chennai: GMV = 155,055,243 INR (share: 0.080507)

These shares are calculated out of the total ...

**C ✗:** In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:

1. Bangalore: GMV = 233,341,258 INR, Share = 0.121144 (12.1144%)
2. Delhi: GMV = 177,702,873 INR, Share = 0.092263 (9.2263%)
3. Chennai: GMV = 155,055,243 INR, Share = 0.080497 (8.0497%)

Population: De...

**D ✗:** In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:

1. Bangalore: INR 233,341,258.00 (share: 0.121158)
2. Delhi: INR 177,702,873.00 (share: 0.092263)
3. Chennai: INR 155,055,243.00 (share: 0.080497)

Population: All delivered orders in INR currency in 20...

**E ✗:** In the 2025 standard market report, the three cities leading by Delivered-order GMV in INR were:

1. Bangalore: GMV = 233,341,258 INR (share: 0.121158)
2. Delhi: GMV = 177,702,873 INR (share: 0.092263)
3. Chennai: GMV = 155,055,243 INR (share: 0.080497)

Each city's share is calculated as city GMV d...

**F ✓:** For the 2025 standard market report (restaurants with at least 100 ratings, using restaurant city as reporting geography), the three leading cities by Delivered-order GMV in INR were:

1. Bangalore: GMV = 129,604,607 INR (share: 0.139675)
2. Chennai: GMV = 92,523,985 INR (share: 0.099749)
3. Hyderab...

</details>

## Q24

**Kunci dan cakupan:**

H1 (Jan–Jun): **94.251 repeat customers** dari 98.033. H2 (Jul–Des): **95.899** dari 98.642. **H2 lebih banyak** (selisih 1.648).

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Menggunakan all orders bukan Delivered (95.048/96.514 salah) |
| B | 0 | 0 | 0 | 0.000 ✗ | Menggunakan all orders bukan Delivered (95.048/96.514 salah) |
| C | 0 | 0 | 0 | 0.000 ✗ | Mengecualikan cancelled tapi metodologi berbeda (94.512/96.095 salah) |
| D | 0 | 0 | 0 | 0.000 ✗ | Mengecualikan cancelled tapi metodologi berbeda (94.512/96.095 salah) |
| E | 0 | 0 | 0 | 0.000 ✗ | Menggunakan all orders bukan Delivered (95.048/96.514 salah) |
| F | 1 | 1 | 1 | 1.000 ✓ | H1 94.251, H2 95.899 Delivered repeat customers benar |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** In January–June 2025, there were 95,048 repeat customers (users who placed more than one order in that period). In July–December 2025, there were 96,514 repeat customers (users who placed more than one order in that period). The second half of 2025 (July–December) had more repeat customers than the ...

**B ✗:** In January–June 2025, there were 95,048 repeat customers (customers who placed more than one order in that period). In July–December 2025, there were 96,514 repeat customers (evaluated independently for that half-year). July–December 2025 had more repeat customers than January–June 2025. Population:...

**C ✗:** In January–June 2025, there were 94,512 repeat customers (customers with more than one non-cancelled order in that period). In July–December 2025, there were 96,095 repeat customers (using the same definition for that half). July–December 2025 had more repeat customers than January–June 2025. Popula...

**D ✗:** In January–June 2025, there were 94,512 repeat customers (customers with more than one order in that period). In July–December 2025, there were 96,095 repeat customers (customers with more than one order in that period). July–December 2025 had more repeat customers than January–June 2025. Population...

**E ✗:** In January–June 2025 (H1 2025), there were 95,048 repeat customers (customers who placed more than one order within that half-year). In July–December 2025 (H2 2025), there were 96,514 repeat customers (again, evaluated only within that half-year). H2 2025 had more repeat customers than H1 2025. Popu...

**F ✓:** In January–June 2025, there were 94,251 repeat customers (customers with at least two delivered orders in that period). In July–December 2025, there were 95,899 repeat customers (evaluated independently for that half). July–December 2025 had more repeat customers than January–June 2025. Population: ...

</details>

## Q25

**Kunci dan cakupan:**

Hyderabad: cancel **6,027789%** vs overall **5,997009%** (+0,030780 pp). Delivery: **31,0967157 mnt** vs **31,0743794 mnt** overall (+0,0223363 mnt). **Tidak dapat membuktikan kausalitas.**

| Arm | Rep 1 | Rep 2 | Rep 3 | Mean | Alasan singkat |
| --- | :---: | :---: | :---: | ---: | --- |
| A | 0 | 0 | 0 | 0.000 ✗ | Bikaner (kota salah) |
| B | 1 | 1 | 1 | 1.000 ✓ | Hyderabad 6,027789%, delivery 31,097 vs 31,074 mnt, tidak kausal |
| C | 1 | 1 | 0 | 0.667 ~ | Rep1–2 benar; rep3 hanya sebagian angka |
| D | 0 | 0 | 0 | 0.000 ✗ | Rep1/3: cancel rate 6,031% (OK), tapi delivery Hyderabad tidak tersedia |
| E | 0 | 0 | 0 | 0.000 ✗ | Rep1: delivery Hyderabad dikueri tapi overall cancel tidak; rep2–3 kurang lengkap |
| F | 0 | 0 | 0 | 0.000 ✗ | Rep1/3: delivery Hyderabad tidak dikueri; rep2 OK |

<details><summary>Jawaban arm A–F (rep 1, disingkat)</summary>

**A ✗:** For 2025, the city with the highest cancellation rate among those with at least 50,000 orders is Bikaner. Here are the requested comparisons:

- Bikaner (2025):
  - Cancellation rate: 0.059603 (5.9603%)
  - Average delivery time (delivered orders): 31.045172 minutes
  - Total orders: 53,571
- Overal...

**B ✓:** For 2025, Hyderabad is the city with the highest cancellation rate among cities with at least 50,000 orders (319,122 orders). Its cancellation rate is 0.060278 (6.0278%), and its average delivery time for delivered orders is 31.096716 minutes. The overall 2025 cancellation rate across all cities is ...

**C ~:** For 2025, Hyderabad is the city with the highest cancellation rate among cities with at least 50,000 orders. Its cancellation rate was 0.0602779 (6.03%) out of 319,122 orders, compared to the overall 2025 cancellation rate of 0.0599701 (5.99%). The average delivery time for delivered orders in Hyder...

**D ✗:** For 2025, Hyderabad had the highest cancellation rate among cities with at least 50,000 orders: 19,236 cancellations out of 319,122 orders, for a cancellation rate of 0.060312. The overall 2025 cancellation rate across all cities was 261,456 cancellations out of 4,359,773 orders, or 0.059991. Hydera...

**E ✗:** For 2025, Hyderabad is the order-recorded city with the highest cancellation rate among cities with at least 50,000 orders. Hyderabad had 319,122 orders, a cancellation rate of 0.060278 (6.0278%), and an average delivery time for delivered orders of 31.096716 minutes. The overall 2025 figures for ca...

**F ✗:** For 2025, Hyderabad is the order-recorded city with the highest cancellation rate among cities with at least 50,000 orders. Hyderabad had 319,122 orders, a cancellation rate of 0.060278, and the overall 2025 cancellation rate was 0.059970. The overall average delivery time for delivered orders was 3...

</details>
