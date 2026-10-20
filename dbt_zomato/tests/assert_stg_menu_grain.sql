SELECT menu_id, food_id
FROM {{ ref('stg_zomato__menu') }}
GROUP BY menu_id, food_id
HAVING COUNT(*) > 1
