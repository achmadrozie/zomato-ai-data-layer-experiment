{% docs mart_order_city_currency_day_source %}
One row per source order date, city, and currency. Counts all orders and statuses, and sums delivered sales without currency conversion.
{% enddocs %}

{% docs mart_order_city_currency_day_source_order_date_source %}
Date parsed from the source order timestamp; its timezone is unverified.
{% enddocs %}

{% docs mart_order_city_currency_day_source_city %}
City recorded on the order.
{% enddocs %}

{% docs mart_order_city_currency_day_source_currency %}
Source currency; monetary values are not converted.
{% enddocs %}

{% docs mart_order_city_currency_day_source_order_count %}
All order rows.
{% enddocs %}

{% docs mart_order_city_currency_day_source_delivered_order_count %}
Delivered order rows.
{% enddocs %}

{% docs mart_order_city_currency_day_source_cancelled_order_count %}
Cancelled order rows.
{% enddocs %}

{% docs mart_order_city_currency_day_source_refunded_order_count %}
Refunded order rows.
{% enddocs %}

{% docs mart_order_city_currency_day_source_delivered_sales_amount %}
Sum of delivered sales amount.
{% enddocs %}
