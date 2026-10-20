SELECT 'mart_order_city_currency_day_source' AS model_name
FROM {{ ref('mart_order_city_currency_day_source') }}
GROUP BY order_date_source, city, currency
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_delivery_city_hour_source' AS model_name
FROM {{ ref('mart_delivery_city_hour_source') }}
GROUP BY order_hour_source, city
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_order_restaurant_currency_day_source' AS model_name
FROM {{ ref('mart_order_restaurant_currency_day_source') }}
GROUP BY order_date_source, restaurant_id, currency
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_order_item_city_currency_day_source' AS model_name
FROM {{ ref('mart_order_item_city_currency_day_source') }}
GROUP BY order_date_source, city, currency
HAVING COUNT(*) > 1
