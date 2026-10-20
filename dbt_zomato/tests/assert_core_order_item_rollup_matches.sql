WITH item_rollup AS (
    SELECT
        order_id
        , COUNT(*) AS item_line_count
        , SUM(quantity) AS item_quantity
        , SUM(line_amount)::NUMBER(18, 2) AS item_line_amount
        , SUM(calculated_line_amount)::NUMBER(18, 2) AS calculated_item_amount
        , SUM(line_amount_delta)::NUMBER(18, 2) AS item_amount_delta
    FROM {{ ref('fact_order_item') }}
    GROUP BY order_id
)

SELECT COALESCE(o.order_id, i.order_id) AS order_id
FROM {{ ref('fact_order') }} o
FULL OUTER JOIN item_rollup i USING (order_id)
WHERE o.order_id IS NULL
    OR i.order_id IS NULL
    OR o.item_line_count <> i.item_line_count
    OR o.item_quantity <> i.item_quantity
    OR o.item_line_amount <> i.item_line_amount
    OR o.calculated_item_amount <> i.calculated_item_amount
    OR o.item_amount_delta <> i.item_amount_delta
