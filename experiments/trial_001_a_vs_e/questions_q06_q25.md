# Additional benchmark questions: Q06–Q25

Use each question verbatim. All questions use recorded `order_date` in 2025 unless a narrower period is stated. The question JSON is the canonical machine-readable list. The `stratum` tag is evaluator metadata, not part of the agent prompt.

| ID | Stratum | Question |
| --- | --- | --- |
| Q06 | data | In 2025, which month had the highest Delivered-order GMV in INR? Give that month's GMV, the runner-up month's GMV, and the gap between them. |
| Q07 | data | Compare January and December 2025 in INR: Delivered order count, GMV, and AOV for each month. Which grew faster from January to December, Delivered order count or AOV, in percentage terms? |
| Q08 | data | For 2025, list the top three order-recorded cities by Delivered-order GMV in INR. For each city, also show Delivered order count and AOV. Treat each exact city label as one city. |
| Q09 | data | Among order-recorded cities with at least 50,000 total orders in 2025, which had the highest cancellation rate? Give its order count, cancellation rate, and gap versus the overall 2025 cancellation rate in percentage points. |
| Q10 | data | For Delivered orders in 2025 with a recorded delivery duration, compare the average delivery time in order-recorded Bangalore and Delhi. Which city was slower, and by how many minutes? |
| Q11 | data | For each recorded order status in 2025, report total orders, the share with a non-null customer rating, and average customer rating among rated orders. What population does each average describe? |
| Q12 | data | What share of 2025 Delivered-order GMV in INR came from the top ten restaurants ranked by that same GMV? Rank by restaurant ID when GMV ties, and report both top-ten and total GMV. |
| Q13 | data | Which three exact cuisine labels had the highest 2025 Delivered-order GMV in INR? For each label, also give total order count and cancellation rate. Do not split comma-separated cuisine labels. |
| Q14 | data | For item lines belonging to 2025 orders, compare Veg, Non-Veg, and unknown food classifications: item-line count, ordered units, and each group's share of all ordered units. What is the difference between line count and units here? |
| Q15 | data | In 2025, what share of orders contained more than one item line? Compare average ordered units per order for one-line and multi-line orders; also report orders with no item line separately. |
| Q16 | data | Among item lines belonging to 2025 orders, how many have a non-zero difference between recorded line amount and price times quantity? Give the signed sum and absolute sum of those differences in INR. Do positive and negative differences offset in this snapshot? |
| Q17 | data | Does recorded order sales amount reconcile to subtotal minus discount plus delivery fee plus GST for 2025? For each order status, give the count of non-zero differences and their signed sum in INR; do not assume one side is the corrected amount. |
| Q18 | data | For 2025 Delivered orders in INR, show up to three customer age segments ranked by Delivered order count. Include Delivered order count, GMV, and AOV, using the existing customer dimension's segment labels. If fewer than three segments occur, report only those present. |
| Q19 | data | Across every calendar date in 2025, including dates with zero Delivered orders, what was the average number of Delivered orders for each weekday? Which weekday had the highest average? |
| Q20 | data | Find the largest month-over-month decline in 2025 Delivered-order GMV in INR. Give the two months, their Delivered order counts, GMV, and AOV, then decompose the GMV change into a count effect and an AOV effect using the earlier month's AOV as the count-effect baseline. Do not claim a cause. |
| Q21 | data | Across the twelve months of 2025, did monthly cancellation rate and average Delivered-order delivery time move together? Report their monthly Pearson correlation, the number of months used, and whether that alone supports a causal claim. |
| Q22 | context | For the standard market report covering 2025, what were Delivered-order GMV in INR, Delivered order count, and AOV? Apply the standard market eligibility rule consistently to all three. |
| Q23 | context | In the 2025 standard market report, which three cities led by Delivered-order GMV in INR? Give each city's GMV and share of standard market GMV, using the reporting geography default. |
| Q24 | context | How many repeat customers were there in January–June 2025 and in July–December 2025? Evaluate repeat status separately within each reporting period, then say which half had more. |
| Q25 | data | For the order-recorded city with the highest 2025 cancellation rate among cities with at least 50,000 orders, compare its cancellation rate and average Delivered-order delivery time with the overall 2025 figures. Can these figures establish that slower delivery caused cancellations? |

Q22–Q24 depend on business rules in the context payload. For arms A–E, a justified request for the missing rule can be an appropriate response; score those questions separately from data-only questions. Gold answers and SQL are local files outside agent access.
