WITH order_expected AS (
    SELECT
        currency
        , COUNT(*) AS order_count
        , SUM(IFF(is_delivered, 1, 0)) AS delivered_order_count
        , SUM(IFF(is_cancelled, 1, 0)) AS cancelled_order_count
        , SUM(IFF(is_refunded, 1, 0)) AS refunded_order_count
        , SUM(delivered_sales_amount) AS delivered_sales_amount
    FROM {{ ref('fact_order') }}
    GROUP BY currency
),
order_actual AS (
    SELECT
        currency
        , SUM(order_count) AS order_count
        , SUM(delivered_order_count) AS delivered_order_count
        , SUM(cancelled_order_count) AS cancelled_order_count
        , SUM(refunded_order_count) AS refunded_order_count
        , SUM(delivered_sales_amount) AS delivered_sales_amount
    FROM {{ ref('mart_order_city_currency_day_source') }}
    GROUP BY currency
),
order_diff AS (
    (SELECT * FROM order_expected EXCEPT SELECT * FROM order_actual)
    UNION ALL
    (SELECT * FROM order_actual EXCEPT SELECT * FROM order_expected)
),
restaurant_expected AS (
    SELECT
        order_date AS order_date_source
        , currency
        , COUNT(*) AS order_count
        , SUM(IFF(is_delivered, 1, 0)) AS delivered_order_count
        , SUM(IFF(is_cancelled, 1, 0)) AS cancelled_order_count
        , SUM(IFF(is_refunded, 1, 0)) AS refunded_order_count
        , SUM(delivered_sales_amount) AS delivered_sales_amount
        , COALESCE(SUM(customer_rating), 0) AS customer_rating_sum
        , COUNT(customer_rating) AS customer_rating_observation_count
        , COALESCE(SUM(IFF(is_delivered, delivery_time_min, NULL)), 0) AS delivery_time_sum_min
        , COUNT(IFF(is_delivered, delivery_time_min, NULL)) AS delivery_time_observation_count
    FROM {{ ref('fact_order') }}
    GROUP BY order_date, currency
),
restaurant_actual AS (
    SELECT
        order_date_source
        , currency
        , SUM(order_count) AS order_count
        , SUM(delivered_order_count) AS delivered_order_count
        , SUM(cancelled_order_count) AS cancelled_order_count
        , SUM(refunded_order_count) AS refunded_order_count
        , SUM(delivered_sales_amount) AS delivered_sales_amount
        , SUM(customer_rating_sum) AS customer_rating_sum
        , SUM(customer_rating_observation_count) AS customer_rating_observation_count
        , SUM(delivery_time_sum_min) AS delivery_time_sum_min
        , SUM(delivery_time_observation_count) AS delivery_time_observation_count
    FROM {{ ref('mart_order_restaurant_currency_day_source') }}
    GROUP BY order_date_source, currency
),
restaurant_diff AS (
    (SELECT * FROM restaurant_expected EXCEPT SELECT * FROM restaurant_actual)
    UNION ALL
    (SELECT * FROM restaurant_actual EXCEPT SELECT * FROM restaurant_expected)
),
delivery_expected AS (
    SELECT
        order_timestamp::DATE AS timestamp_date_source
        , COUNT(*) AS delivered_order_count
        , COALESCE(SUM(delivery_time_min), 0) AS delivery_time_sum_min
        , COUNT(delivery_time_min) AS delivery_time_observation_count
    FROM {{ ref('fact_order') }}
    WHERE is_delivered
    GROUP BY order_timestamp::DATE
),
delivery_actual AS (
    SELECT
        order_hour_source::DATE AS timestamp_date_source
        , SUM(delivered_order_count) AS delivered_order_count
        , SUM(delivery_time_sum_min) AS delivery_time_sum_min
        , SUM(delivery_time_observation_count) AS delivery_time_observation_count
    FROM {{ ref('mart_delivery_city_hour_source') }}
    GROUP BY order_hour_source::DATE
),
delivery_diff AS (
    (SELECT * FROM delivery_expected EXCEPT SELECT * FROM delivery_actual)
    UNION ALL
    (SELECT * FROM delivery_actual EXCEPT SELECT * FROM delivery_expected)
),
item_expected AS (
    SELECT
        COUNT(*) AS order_item_count
        , SUM(quantity) AS ordered_quantity
        , SUM(line_amount) AS source_line_amount
        , SUM(calculated_line_amount) AS calculated_line_amount
        , SUM(line_amount_delta) AS line_amount_delta
    FROM {{ ref('fact_order_item') }}
),
item_actual AS (
    SELECT
        SUM(order_item_count) AS order_item_count
        , SUM(ordered_quantity) AS ordered_quantity
        , SUM(source_line_amount) AS source_line_amount
        , SUM(calculated_line_amount) AS calculated_line_amount
        , SUM(line_amount_delta) AS line_amount_delta
    FROM {{ ref('mart_order_item_city_currency_day_source') }}
),
item_diff AS (
    (SELECT * FROM item_expected EXCEPT SELECT * FROM item_actual)
    UNION ALL
    (SELECT * FROM item_actual EXCEPT SELECT * FROM item_expected)
),
item_currency_expected AS (
    SELECT o.currency, SUM(i.line_amount) AS source_line_amount
    FROM {{ ref('fact_order') }} AS o
    INNER JOIN {{ ref('fact_order_item') }} AS i USING (order_id)
    GROUP BY o.currency
),
item_currency_actual AS (
    SELECT currency, SUM(source_line_amount) AS source_line_amount
    FROM {{ ref('mart_order_item_city_currency_day_source') }}
    GROUP BY currency
),
item_currency_diff AS (
    (SELECT * FROM item_currency_expected EXCEPT SELECT * FROM item_currency_actual)
    UNION ALL
    (SELECT * FROM item_currency_actual EXCEPT SELECT * FROM item_currency_expected)
)
SELECT 'order_city_currency_totals' AS check_name FROM order_diff
UNION ALL
SELECT 'restaurant_daily_currency_components' FROM restaurant_diff
UNION ALL
SELECT 'delivery_daily_components' FROM delivery_diff
UNION ALL
SELECT 'item_join_preserves_totals' FROM item_diff
UNION ALL
SELECT 'item_currency_totals' FROM item_currency_diff
