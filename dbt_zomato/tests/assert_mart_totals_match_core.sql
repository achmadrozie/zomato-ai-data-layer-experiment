WITH order_fact AS (
    SELECT COUNT(*) AS order_count, SUM(delivered_sales_amount) AS delivered_sales_amount
    FROM {{ ref('fact_order') }}
),
order_mart AS (
    SELECT SUM(order_count) AS order_count, SUM(delivered_sales_amount) AS delivered_sales_amount
    FROM {{ ref('mart_order_city_currency_day_source') }}
),
delivery_fact AS (
    SELECT COUNT(*) AS delivered_order_count
    FROM {{ ref('fact_order') }}
    WHERE is_delivered
),
delivery_mart AS (
    SELECT SUM(delivered_order_count) AS delivered_order_count
    FROM {{ ref('mart_delivery_city_hour_source') }}
),
restaurant_mart AS (
    SELECT SUM(order_count) AS order_count, SUM(delivered_sales_amount) AS delivered_sales_amount
    FROM {{ ref('mart_restaurant_currency_lifetime') }}
),
item_fact AS (
    SELECT
        COUNT(*) AS order_item_count
        , SUM(quantity) AS ordered_quantity
        , SUM(line_amount) AS source_line_amount
        , SUM(line_amount_delta) AS line_amount_delta
    FROM {{ ref('fact_order_item') }}
),
item_mart AS (
    SELECT
        SUM(order_item_count) AS order_item_count
        , SUM(ordered_quantity) AS ordered_quantity
        , SUM(source_line_amount) AS source_line_amount
        , SUM(line_amount_delta) AS line_amount_delta
    FROM {{ ref('mart_order_item_city_day_source') }}
)
SELECT 'order_city_day' AS check_name
WHERE EXISTS (
    SELECT 1 FROM order_fact f CROSS JOIN order_mart m
    WHERE f.order_count != m.order_count
        OR f.delivered_sales_amount IS DISTINCT FROM m.delivered_sales_amount
)
UNION ALL
SELECT 'delivery_city_hour'
WHERE EXISTS (
    SELECT 1 FROM delivery_fact f CROSS JOIN delivery_mart m
    WHERE f.delivered_order_count != m.delivered_order_count
)
UNION ALL
SELECT 'restaurant_lifetime'
WHERE EXISTS (
    SELECT 1 FROM order_fact f CROSS JOIN restaurant_mart m
    WHERE f.order_count != m.order_count
        OR f.delivered_sales_amount IS DISTINCT FROM m.delivered_sales_amount
)
UNION ALL
SELECT 'order_item_city_day'
WHERE EXISTS (
    SELECT 1 FROM item_fact f CROSS JOIN item_mart m
    WHERE f.order_item_count != m.order_item_count
        OR f.ordered_quantity IS DISTINCT FROM m.ordered_quantity
        OR f.source_line_amount IS DISTINCT FROM m.source_line_amount
        OR f.line_amount_delta IS DISTINCT FROM m.line_amount_delta
)
