# Zomato business context

Version: 1.0.0 candidate, for review. Scope: the Project 1 snapshot in `ZOMATO_DLR`.

## Entities and order status

- An order is one transaction. An item line can contain multiple units; line count and quantity are different.
- Order amounts belong to the whole order. Joining item lines repeats those amounts.
- Delivered, Cancelled, and Refunded describe the recorded order state. The snapshot does not provide status-transition or refund-payment history.

## Proposed reporting policies

These are candidate experiment policies for review, not claims about Zomato's real business rules. They are not yet approved for benchmark use.

- **CTX-01 — Standard market report:** eligible restaurants have at least 100 recorded ratings (`dim_restaurant.rating_count >= 100`). Missing rating counts are ineligible. The eligibility filter applies to every metric in that report; metric formulas stay as defined in the semantic layer.
- **CTX-02 — Reporting geography:** an unqualified market/city report uses restaurant-dimension city. Order-recorded city is used only when the request explicitly asks for it.
- **CTX-03 — Repeat customers:** a repeat customer has at least two Delivered orders within the requested reporting period. Orders before that period do not qualify the customer for that report.

## Time and report interpretation

- Daily reports use the supplied order-date field; hourly reports use the order timestamp. Mart `_utc` labels are naming conventions: values have not been timezone-converted or verified as UTC.
- Monetary reports are scoped by source currency; no exchange-rate conversion is available.
- Reports retain recorded amounts and show reconciliation discrepancies separately. A discrepancy alone does not establish a corrected business amount.
- Order customer ratings, restaurant ratings, and review star ratings describe different populations. The report topic determines which is relevant.
