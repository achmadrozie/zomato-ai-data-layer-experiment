{% docs mart_delivery_city_hour_source %}
One row per source wall-clock hour and city for delivered orders. The hour includes the date; no timezone conversion or SLA threshold is applied.
{% enddocs %}

{% docs mart_delivery_city_hour_source_order_hour_source %}
Source order timestamp truncated to the hour, with no timezone conversion.
{% enddocs %}

{% docs mart_delivery_city_hour_source_city %}
City recorded on the order.
{% enddocs %}

{% docs mart_delivery_city_hour_source_delivered_order_count %}
Delivered order rows.
{% enddocs %}

{% docs mart_delivery_city_hour_source_avg_delivery_time_min %}
Average nonnull delivery duration in minutes.
{% enddocs %}
