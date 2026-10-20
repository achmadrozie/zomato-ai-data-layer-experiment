SELECT
    DATE_TRUNC('HOUR', order_timestamp) AS order_hour_source
    , city
    , COUNT(*) AS delivered_order_count
    , AVG(delivery_time_min) AS avg_delivery_time_min
FROM {{ ref('fact_order') }}
WHERE is_delivered
GROUP BY DATE_TRUNC('HOUR', order_timestamp), city
