# Core layer review

Checkpoint: 20 October 2026. The core layer is built in `ZOMATO_DLR.CORE` using `DBT_LAYER_REFACTOR_ROLE`. Project 0 is unchanged.

## Grain and lineage

| Model | Grain | Rows | Main inputs |
| --- | --- | ---: | --- |
| `dim_customer` | One row per customer ID | 100,000 | `stg_zomato__user` |
| `dim_date` | One row per calendar date | 1,096 | `int_date_features` |
| `dim_food` | One row per food ID | 371,561 | `stg_zomato__food` |
| `dim_restaurant` | One row per restaurant ID | 148,541 | `stg_zomato__restaurant` |
| `fact_order` | One row per order ID | 10,000,000 | Four `int_order_*` models |
| `fact_order_item` | One row per order-item ID | 22,998,179 | `stg_zomato__order_item`, `int_order_base` |

`fact_order` joins order base, financials, and fulfillment by their tested unique `order_id`. It left joins the item rollup so the order grain is preserved even if a future order has no items. It keeps source order counts and amounts alongside item-derived counts and reconciliation deltas.

`fact_order_item` keeps every staged item and left joins order context by `order_id`. An orphan item stays visible, and its missing order relationship fails a dbt test. Both facts are rebuilt as tables from the Project 1 snapshot. The source has no reliable change marker for correct incremental updates; the old timestamp cutoff could miss late or corrected orders.

The core facts retain two different amount meanings: `sales_amount` is the order amount after discount, fee, and GST; `item_line_amount` is the sum of source item lines before those order-level adjustments. `delivered_sales_amount` is zero for orders that were not delivered.

## Validation

- `dbt build --select path:models/core --threads 1` created all six tables and passed 30 data tests.
- Dimension keys and order/item fact keys are unique and non-null where required.
- Foreign-key tests passed for order to customer, restaurant, and date, and item to order, restaurant, and food.
- Core order and item row counts match staging: 10,000,000 orders and 22,998,179 items.
- Aggregating `fact_order_item` back to order matches `fact_order` item line counts, quantities, source amounts, calculated amounts, and deltas.
- `item_amount_delta` remains nonzero on 32,716 orders, from 1.00 to 9.00. The discrepancy is preserved for the later business definition review.

## Example: item grain to order grain

For order `163847`, `fact_order_item` has four rows:

| order_item_id | food_id | quantity | line_amount |
| ---: | --- | ---: | ---: |
| 376968 | fd109018 | 2 | 284.00 |
| 376969 | fd1021023 | 1 | 89.00 |
| 376970 | fd122195 | 1 | 280.00 |
| 376971 | fd575970 | 1 | 194.00 |

The single `fact_order` row has `item_line_count = 4`, `item_quantity = 5`, and `item_line_amount = 847.00`. Its `sales_amount` is 924.00, while `delivered_sales_amount` is 0.00 because the order was cancelled. The item total and order sales amount describe different parts of the transaction.

Example review query:

```sql
SELECT
    order_id,
    order_status,
    city,
    sales_amount,
    delivered_sales_amount,
    item_line_count,
    item_quantity,
    item_line_amount,
    item_amount_delta
FROM ZOMATO_DLR.CORE.FACT_ORDER
WHERE order_id IN (163847, 163854, 163861)
ORDER BY order_id;
```

| order_id | status | city | sales_amount | delivered_sales_amount | item lines | quantity | item line amount | item delta |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 163847 | Cancelled | Delhi | 924.00 | 0.00 | 4 | 5 | 847.00 | 0.00 |
| 163854 | Delivered | Begusarai | 233.00 | 233.00 | 2 | 2 | 303.00 | 0.00 |
| 163861 | Delivered | Bangalore | 331.00 | 331.00 | 3 | 3 | 415.00 | 0.00 |
