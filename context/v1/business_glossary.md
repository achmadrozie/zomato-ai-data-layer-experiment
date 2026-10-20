# Zomato business glossary

Version: 1.0.0 candidate. Scope: the Project 1 snapshot in `ZOMATO_DLR`.

## Business entities and grain

An order is a single transaction identified by `order_id`. An order item is a line identified by `order_item_id`; a line can contain more than one unit. Item-line count, quantity, and distinct food count describe different things.

The order fact has one row per order. The item fact has one row per item line. Joining an order to its item lines repeats order-level amounts on every matching line. An order-level total belongs to the order grain; item quantities and line amounts belong to the item grain. Ratios combining these grains aggregate their numerator and denominator over the same business population and time period.

A customer, food, and restaurant dimension each has one row per corresponding ID. The calendar dimension has one row per date. Food-level attributes are associated with item lines. A food-specific order count means distinct orders containing that food; dividing item count by all orders describes a different population.

## Order status and financial meaning

Delivered, Cancelled, and Refunded are source order-status labels. The snapshot records a status value, rather than a history of status transitions. A refunded row does not establish when the refund happened or the amount refunded.

GMV in this project means the sum of source order sales amounts for Delivered orders. A non-delivered order contributes zero to delivered sales. This is a project metric definition; the available data does not establish accounting revenue, profit, net settlement, or actual cash collected.

The calculated order amount is subtotal minus discount plus delivery fee plus GST. The source order sales amount is retained separately. The order financial delta is source sales amount minus the calculated order amount.

Source item amount is the recorded item `line_amount`. Calculated item amount is price multiplied by quantity. The item amount delta is source item amount minus calculated item amount. Nonzero deltas remain visible; neither amount has been silently substituted for the other. Item amount excludes the order-level adjustments used in the order financial calculation.

## Metric definitions and units

| Metric | Definition | Unit and population |
| --- | --- | --- |
| `count_order_total` | Count of order rows | Orders, all statuses |
| `count_order_delivered` | Count of Delivered orders | Orders |
| `count_order_cancelled` | Count of Cancelled orders | Orders |
| `count_order_refunded` | Count of Refunded orders | Orders |
| `count_order_rated` | Count of orders with a nonnull numeric customer rating | Orders, all statuses |
| `gmv` | Sum of delivered source order sales amounts | Source currency |
| `aov` | GMV divided by delivered order count | Source currency per delivered order |
| `cancellation_rate` | 100 × cancelled order count / all order count | Percentage, 0–100 scale |
| `delivered_rate` | 100 × delivered order count / all order count | Percentage, 0–100 scale |
| `refund_rate` | 100 × refunded order count / all order count | Percentage, 0–100 scale |
| `rating_coverage_rate` | 100 × rated order count / all order count | Percentage, 0–100 scale |
| `avg_delivery_time_min` | Average nonnull numeric delivery duration among Delivered orders | Minutes per order with a duration |
| `avg_customer_rating` | Average nonnull numeric customer rating | Rating points, all statuses with a rating |
| `count_order_item` | Count of item-line rows | Item lines, all order statuses |
| `total_ordered_quantity` | Sum of item quantities | Units, all order statuses |
| `total_ordered_amount` | Sum of source item line amounts | Source monetary amount, all order statuses |
| `avg_item_unit_price` | Source item line amount divided by item quantity | Source monetary amount per unit; quantity weighted |
| `item_lines_per_order` | Item-line count divided by all order count | Item lines per order |
| `ordered_quantity_per_order` | Item quantity divided by all order count | Units per order |

The last two ratios use the order and item facts. Their shared dimensions and filters must define the same population. Food attributes are not shared dimensions of the all-order denominator. A zero denominator has no defined business ratio. Missing numeric values are absent observations; SQL aggregates exclude null inputs, so a count of orders is not necessarily the count of observed ratings or durations.

Currencies are not converted. A monetary total has a currency-specific meaning. Item rows inherit their currency context from the parent order; the item fact does not contain a currency column. Summing amounts across currencies does not establish a converted monetary total.

## Time and geography

Order timestamps have no verified source timezone and are parsed without a timezone offset. The `_source` suffix denotes source wall-clock time. UTC or another timezone cannot be inferred from that suffix. An hourly mart bucket includes both the calendar date and the hour, rather than pooling the same hour of day across dates.

`order_date` is parsed from the separately supplied source order-date field. Timestamp-derived hour comes from the source order timestamp. Equality between the supplied date and the timestamp's date is a data-quality question, rather than an assumed transformation rule. A business-day boundary in a different timezone is unestablished.

Order city is derived from the source order's restaurant-city text. Restaurant-dimension city is the restaurant attribute in the snapshot. Customer residence, delivery destination, and geographic changes over time are not established by those fields. Order cuisine and restaurant-dimension cuisine are also separate source attributes.

Calendar weekends mean Saturday and Sunday. Customer `age_segment` labels are age bands in this project: under 25 is Gen Z; 25–39 is Millennial; 40–54 is Gen X; 55 and above is Boomer; missing age is Unknown. They are not birth-year cohort classifications.

## Aggregation and coverage

Counts, quantities, and monetary sums can be combined over disjoint groups at their declared grain and currency. A larger-group average needs the sum of its nonnull observations divided by their count; an unweighted average of group averages generally changes the meaning. A larger-group rate or AOV likewise comes from aggregated numerator and denominator. Percentiles are not additive.

The order daily mart groups by source date, order city, and currency. The delivery hourly mart contains Delivered orders and groups by source timestamp hour and order city. The restaurant lifetime mart groups by restaurant and currency over the available snapshot; lifetime means the observed snapshot period. The item daily mart groups by source order date and order city. Current delivery and restaurant marts include averages without all the observation counts required for arbitrary weighted reaggregation.

The snapshot contains no reliable change marker for incremental loading. Current order status and dimension attributes do not establish historical state at an arbitrary past date. Customer ratings on orders, restaurant aggregate ratings, and review star ratings are different measures with different populations. Review AI enrichment belongs to Project 0 and is outside this experiment's current data coverage.
