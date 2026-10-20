{% docs mart_order_item_city_day_source %}
One row per source order date and city, aggregating item lines. The source line amount and calculated line amount remain separate so discrepancies are visible.
{% enddocs %}

{% docs mart_order_item_city_day_source_order_date_source %}
Date parsed from the source order timestamp; its timezone is unverified.
{% enddocs %}

{% docs mart_order_item_city_day_source_city %}
City recorded on the parent order.
{% enddocs %}

{% docs mart_order_item_city_day_source_order_item_count %}
Number of item lines.
{% enddocs %}

{% docs mart_order_item_city_day_source_ordered_quantity %}
Sum of item quantities.
{% enddocs %}

{% docs mart_order_item_city_day_source_source_line_amount %}
Sum of source item line amounts.
{% enddocs %}

{% docs mart_order_item_city_day_source_calculated_line_amount %}
Sum of price times quantity.
{% enddocs %}

{% docs mart_order_item_city_day_source_line_amount_delta %}
Sum of source minus calculated line amount.
{% enddocs %}
