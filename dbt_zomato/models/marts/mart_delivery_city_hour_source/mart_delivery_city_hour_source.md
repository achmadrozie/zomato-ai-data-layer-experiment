{% docs mart_delivery_city_hour_source %}
One row per source timestamp hour and order city among Delivered orders. All measures are additive over disjoint buckets. The timestamp hour includes its date; its timezone is unverified. Average delivery minutes is SUM(delivery_time_sum_min) / NULLIF(SUM(delivery_time_observation_count), 0).
{% enddocs %}

{% docs mart_delivery_city_hour_source_order_hour_source %}
Source wall-clock order timestamp truncated to the hour, including the date; no timezone conversion.
{% enddocs %}

{% docs mart_delivery_city_hour_source_city %}
City recorded on the order.
{% enddocs %}

{% docs mart_delivery_city_hour_source_delivered_order_count %}
Count of Delivered order rows, including rows with a null duration.
{% enddocs %}

{% docs mart_delivery_city_hour_source_delivery_time_sum_min %}
Sum of nonnull delivery durations in minutes; zero when there are no observations.
{% enddocs %}

{% docs mart_delivery_city_hour_source_delivery_time_observation_count %}
Count of Delivered orders with a nonnull duration; denominator for average duration.
{% enddocs %}
