WITH order_agg AS (
    SELECT
        restaurant_id
        , currency
        , COUNT(*) AS order_count
        , COALESCE(COUNT_IF(is_delivered), 0) AS delivered_order_count
        , SUM(delivered_sales_amount) AS delivered_sales_amount
        , AVG(customer_rating) AS avg_customer_rating
        , AVG(IFF(is_delivered, delivery_time_min, NULL)) AS avg_delivery_time_min
    FROM {{ ref('fact_order') }}
    GROUP BY restaurant_id, currency
)
SELECT
    o.restaurant_id
    , o.currency
    , r.restaurant_name
    , r.city
    , r.cuisine
    , o.order_count
    , o.delivered_order_count
    , o.delivered_sales_amount
    , o.avg_customer_rating
    , o.avg_delivery_time_min
FROM order_agg AS o
LEFT JOIN {{ ref('dim_restaurant') }} AS r
    ON o.restaurant_id = r.restaurant_id
