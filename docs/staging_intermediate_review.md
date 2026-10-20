# Staging and intermediate review

Checkpoint: 20 October 2026. All queries and dbt runs target `ZOMATO_DLR` using `DBT_LAYER_REFACTOR_ROLE`. Project 0 is unchanged.

## Source audit

| Source table | Rows at Project 1 initialization | Key observation |
| --- | ---: | --- |
| `FOOD` | 371,561 | `F_ID` is alphanumeric. |
| `MENU` | 1,179,936 | `MENU_ID` is alphanumeric and repeats. `(MENU_ID, F_ID)` is unique across the snapshot. |
| `ORDERS` | 10,000,000 | Date range is 2024-01-01 through 2026-06-30. Source amounts reconcile with `subtotal - discount + delivery_fee + gst`. |
| `ORDER_ITEMS` | 22,998,179 | `F_ID` is alphanumeric; all 10 million orders have items. |
| `RESTAURANTS` | 148,541 | Ratings may contain `--`, rating counts contain text, and cost contains a currency symbol. |
| `REVIEWS` | 300,000 | Review dates parse successfully. |
| `USERS` | 100,000 | Project 1 copy excludes `PASSWORD`. |

The source does not identify the timezone of `ORDERS.ORDER_TIMESTAMP`. Staging parses it as `TIMESTAMP_NTZ` and intermediate calls it `order_timestamp_source`. No UTC conversion is applied.

## Layer contracts

- `STAGING`: seven views, one per source table. They trim text, parse numeric/date fields, standardize order status, and retain source rows. Food and menu IDs remain text. The menu grain is `(menu_id, food_id)`.
- `INTERMEDIATE`: six views. `int_date_spine` and `int_date_features` provide calendar attributes. `int_order_base`, `int_order_financials`, and `int_order_fulfillment` each have one row per order. `int_order_item_rollup` groups items to one row per order.
- Financial and item rollups expose reconciliation deltas instead of silently changing source values. Downstream core and marts are outside this checkpoint.

## Validation

- Seven staging views and six intermediate views were created successfully.
- `int_date_spine` covers 2024-01-01 through 2026-12-31 with 1,096 dates.
- `int_order_item_rollup` contains 10,000,000 orders. The item line count and quantity match `ORDERS.ITEMS_COUNT` and `ORDERS.SALES_QTY` for every order in the snapshot.
- Order-level `sales_amount_delta` is zero for all 10,000,000 orders (dbt reconciliation test).
- Item-level `item_amount_delta` is nonzero for 32,716 of 10,000,000 orders, ranging from 1.00 to 9.00. This is a source discrepancy to examine before core financial definitions are changed.
- `MENU` contains 1,048,575 distinct menu IDs across 1,179,936 rows. The 1,179,936 `(menu_id, food_id)` pairs are distinct.

Run the checkpoint from the repository root with the Project 1 dbt profile:

```sh
dbt build --select path:models/staging path:models/intermediate \
  --project-dir dbt_zomato --profiles-dir .local/dbt --threads 1
```

## Example output

This query combines the four order intermediate views without exposing customer fields:

```sql
SELECT
    b.order_id,
    b.order_timestamp_source,
    b.city,
    f.sales_amount,
    f.calculated_sales_amount,
    f.sales_amount_delta,
    u.order_status,
    i.item_line_count,
    i.item_quantity
FROM ZOMATO_DLR.INTERMEDIATE.INT_ORDER_BASE b
JOIN ZOMATO_DLR.INTERMEDIATE.INT_ORDER_FINANCIALS f USING (order_id)
JOIN ZOMATO_DLR.INTERMEDIATE.INT_ORDER_FULFILLMENT u USING (order_id)
JOIN ZOMATO_DLR.INTERMEDIATE.INT_ORDER_ITEM_ROLLUP i USING (order_id)
WHERE b.order_id IN (163847, 163854, 163861)
ORDER BY b.order_id;
```

| order_id | order_timestamp_source | city | sales_amount | calculated_sales_amount | delta | status | item lines | quantity |
| ---: | --- | --- | ---: | ---: | ---: | --- | ---: | ---: |
| 163847 | 2025-05-30 13:37:27 | Delhi | 924.00 | 924.00 | 0.00 | Cancelled | 4 | 5 |
| 163854 | 2025-09-04 08:22:56 | Begusarai | 233.00 | 233.00 | 0.00 | Delivered | 2 | 2 |
| 163861 | 2026-06-26 14:32:25 | Bangalore | 331.00 | 331.00 | 0.00 | Delivered | 3 | 3 |

For a staging example, `STAGING.STG_ZOMATO__MENU` has `menu_id = 'mn0'`, `restaurant_id = 567335`, `food_id = 'fd0'`, and `price = 40.00` in one source row. The same menu ID appears with another food ID, illustrating why `menu_id` alone is not unique.
