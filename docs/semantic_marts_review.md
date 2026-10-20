# Semantic and marts checkpoint

## Scope

All six core tables now have a semantic model in their own model YAML: `dim_customer`, `dim_date`, `dim_food`, `dim_restaurant`, `fact_order`, and `fact_order_item`. The two fact semantic models provide measures; the four dimensions provide joinable customer, date, food, and restaurant attributes. Identifiers such as names and emails are not exposed from the customer semantic model.

MetricFlow parses 19 metrics: the nine existing metrics plus ten added here. New simple metrics are `count_order_refunded`, `count_order_rated`, `avg_delivery_time_min`, and `avg_customer_rating`. New percentage metrics are `delivered_rate`, `refund_rate`, and `rating_coverage_rate` (0–100 scale, like the existing `cancellation_rate`). `avg_item_unit_price` is source item amount divided by quantity. `item_lines_per_order` and `ordered_quantity_per_order` combine item fact numerators with the order fact denominator, testing cross-fact semantic queries. These ratios use the metric engine's aggregation and division, not row-level joins between facts.

## Simple aggregate marts

| Mart | Grain | Main aggregates |
| --- | --- | --- |
| `mart_order_city_currency_day_source` | Source order date, city, currency | Order status counts and delivered sales |
| `mart_delivery_city_hour_source` | Source wall-clock hour including date, city | Delivered order count and average delivery minutes |
| `mart_restaurant_currency_lifetime` | Restaurant, source currency across this snapshot | Order counts, delivered sales, average ratings and delivery minutes |
| `mart_order_item_city_day_source` | Source order date, city | Item line count, quantity, source and calculated item amounts, delta |

The source does not establish a timezone for order timestamps. `_source` marks a parsed source date or timestamp bucket. No UTC conversion occurs. Monetary aggregates retain their source currency; marts containing sales group by `currency`. The review insights mart remains disabled because its AI enrichment source belongs to Project 0.

## Semantic checks

- `dbt parse` recognizes six semantic models and 19 metrics.
- `mf validate-configs --skip-dw` reports zero errors, future errors, and warnings.
- `mf list dimensions --metrics gmv` exposes customer, restaurant, and calendar attributes through the core semantic joins.
- `mf list dimensions --metrics total_ordered_amount` exposes food attributes as well as order, customer, restaurant, and calendar paths.
- `mf list dimensions --metrics item_lines_per_order` finds common dimensions for the cross-fact ratio.
- A live MetricFlow query for `gmv`, `count_order_total`, and `aov` grouped by restaurant city returned values for all three metrics. A second query for `item_lines_per_order` and `ordered_quantity_per_order` grouped by `metric_time` returned daily values, verifying a cross-fact order/item query.
- The mart build created 2,210,132 delivery city-hour rows, 427,221 order city-currency-date rows, 427,221 order-item city-date rows, 148,541 restaurant-currency rows, and 4,018 time-spine dates. All 17 selected generic and singular data tests passed.

Example MetricFlow queries used against the live target warehouse:

```bash
mf query --metrics gmv,count_order_total,aov --group-by restaurant_id__city,metric_time
mf query --metrics total_ordered_quantity,avg_item_unit_price --group-by food_id__veg_or_non_veg
mf query --metrics item_lines_per_order,ordered_quantity_per_order --group-by metric_time
```

The two singular tests `assert_mart_grains` and `assert_mart_totals_match_core` check each declared mart grain and reconcile mart totals to both facts.
