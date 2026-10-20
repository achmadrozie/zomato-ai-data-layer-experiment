SELECT order_id
FROM {{ ref('int_order_financials') }}
WHERE sales_amount_delta IS NULL OR sales_amount_delta <> 0
