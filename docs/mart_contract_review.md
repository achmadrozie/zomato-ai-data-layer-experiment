# Mart contract correction

All four active marts now follow `mart_<subject>_<dimensions>_<time bucket>_source`. The source timestamp timezone is unverified, so `_source` remains the explicit time marker. `order_date_source` comes from the separately supplied order-date field; the hourly timestamp bucket is derived from `order_timestamp` and includes its date.

| Model | Unique grain | Additive measures |
| --- | --- | --- |
| `mart_order_city_currency_day_source` | Order date, order city, currency | Order/status counts, delivered sales |
| `mart_delivery_city_hour_source` | Source timestamp hour, order city; Delivered orders only | Delivered order count, duration sum and duration-observation count |
| `mart_order_restaurant_currency_day_source` | Order date, restaurant ID, currency | Order/status counts, delivered sales, rating sum/count and delivered-duration sum/count |
| `mart_order_item_city_currency_day_source` | Order date, order city, parent-order currency; all statuses | Item-line count, quantity, source amount, calculated amount, delta |

The former restaurant lifetime table was an aggregate of order facts. Changing its date grain makes it suitable for the time-bucketed mart contract. Moving it into core would introduce a summary alongside the entity/fact grains without resolving its missing date or average-reaggregation problem. Restaurant display attributes remain in `dim_restaurant`; its unique ID permits a many-to-one join when needed.

The item mart left joins the unique parent order to obtain currency. No order-level measures are summed from that join. Unmatched items remain visible as null-currency rows that fail validation. Grouping by currency prevents the new mart from combining source monetary amounts across currencies.

## Average and ratio components

Every active mart exposes additive measures rather than stored averages, rates, or percentiles. Rating observations include any order with a nonnull numeric rating. Delivery observations include only Delivered orders with a nonnull numeric duration. Zero observations give zero sum/count components and an undefined average.

For example, daily restaurant rows can be rolled up to a month using:

```sql
SELECT
    DATE_TRUNC('MONTH', order_date_source) AS order_month_source,
    currency,
    SUM(delivered_sales_amount) AS delivered_sales_amount,
    SUM(delivery_time_sum_min)
        / NULLIF(SUM(delivery_time_observation_count), 0) AS avg_delivery_time_min,
    SUM(customer_rating_sum)
        / NULLIF(SUM(customer_rating_observation_count), 0) AS avg_customer_rating
FROM ZOMATO_DLR.MARTS.MART_ORDER_RESTAURANT_CURRENCY_DAY_SOURCE
GROUP BY order_month_source, currency;
```

`delivered_order_count` is not the duration denominator when a Delivered order has no duration. The same distinction applies to order count and rating-observation count. Existing semantic metrics calculate their averages directly on core, with matching populations.

## Legacy models and relations

The nonactive Project 0 review-insights SQL/Markdown/YAML and AI source declaration live in `archive/project0`, outside dbt model paths. They are not core models or active Project 1 marts.

After a successful replacement build, `snowflake/project1/02_retire_legacy_marts.sql` moves explicit superseded Project 1 tables from `ZOMATO_DLR.MARTS` into `ZOMATO_DLR.SNAPSHOTS` under `RETIRED_20261020_...` names. This preserves the previous outputs for inspection and removes their names from the active mart schema. The script touches only named Project 1 tables and does not overwrite an existing archive destination.

## Validation

`assert_mart_grains` checks all four composite keys. `assert_mart_totals_match_core` verifies status/amount totals by currency, restaurant-mart sum/count components rolled up by date and currency, delivery components rolled up by timestamp date, and item row/quantity/amount preservation plus monetary totals by currency. These checks exercise larger-grain aggregation and the new parent-order join.

The corrected Snowflake build completed on 20 October 2026: all four tables built and all 25 selected data tests passed, with zero warnings/errors. Table row counts were 2,210,132 delivery city-hour rows; 427,221 order city-currency-day rows; 427,221 item city-currency-day rows; and 9,243,921 restaurant-currency-day rows. The restaurant daily grain is close to the 10-million-row order fact, so this mart provides limited row-count compression; no performance improvement is assumed from its existence.

After validation, the legacy lifetime and item-without-currency tables were moved to `ZOMATO_DLR.SNAPSHOTS.RETIRED_20261020_...`. Warehouse metadata confirmed that `MARTS` contains exactly the four current tables listed above; the other named legacy tables did not exist in Project 1.
