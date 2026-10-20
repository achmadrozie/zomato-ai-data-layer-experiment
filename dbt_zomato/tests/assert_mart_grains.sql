SELECT 'mart_order_city_currency_day_utc' AS model_name
FROM {{ ref('mart_order_city_currency_day_utc') }}
GROUP BY order_date_utc, city, currency
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_delivery_city_hour_utc' AS model_name
FROM {{ ref('mart_delivery_city_hour_utc') }}
GROUP BY order_hour_utc, city
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_order_restaurant_currency_day_utc' AS model_name
FROM {{ ref('mart_order_restaurant_currency_day_utc') }}
GROUP BY order_date_utc, restaurant_id, currency
HAVING COUNT(*) > 1

UNION ALL

SELECT 'mart_order_item_city_currency_day_utc' AS model_name
FROM {{ ref('mart_order_item_city_currency_day_utc') }}
GROUP BY order_date_utc, city, currency
HAVING COUNT(*) > 1
