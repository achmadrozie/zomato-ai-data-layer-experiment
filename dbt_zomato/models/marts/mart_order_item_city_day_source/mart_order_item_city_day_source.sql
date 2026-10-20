SELECT
    order_date AS order_date_source
    , city
    , COUNT(*) AS order_item_count
    , SUM(quantity) AS ordered_quantity
    , SUM(line_amount) AS source_line_amount
    , SUM(calculated_line_amount) AS calculated_line_amount
    , SUM(line_amount_delta) AS line_amount_delta
FROM {{ ref('fact_order_item') }}
GROUP BY order_date, city
