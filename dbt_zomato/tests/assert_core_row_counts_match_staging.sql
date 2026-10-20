WITH counts AS (
    SELECT
        (SELECT COUNT(*) FROM {{ ref('stg_zomato__order') }}) AS staged_orders
        , (SELECT COUNT(*) FROM {{ ref('fact_order') }}) AS core_orders
        , (SELECT COUNT(*) FROM {{ ref('stg_zomato__order_item') }}) AS staged_items
        , (SELECT COUNT(*) FROM {{ ref('fact_order_item') }}) AS core_items
)

SELECT *
FROM counts
WHERE staged_orders <> core_orders
    OR staged_items <> core_items
