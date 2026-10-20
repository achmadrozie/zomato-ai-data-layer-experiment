SELECT
    b.order_id
    , b.source_items_count
    , i.item_line_count
    , b.source_sales_qty
    , i.item_quantity
FROM {{ ref('int_order_base') }} b
INNER JOIN {{ ref('int_order_item_rollup') }} i USING (order_id)
WHERE b.source_items_count <> i.item_line_count
    OR b.source_sales_qty <> i.item_quantity
