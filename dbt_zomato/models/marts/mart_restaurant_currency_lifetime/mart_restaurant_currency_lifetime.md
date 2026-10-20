{% docs mart_restaurant_currency_lifetime %}
One row per restaurant and source currency across the current snapshot. Restaurant attributes come from dim_restaurant; counts, amount, and averages come from fact_order.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_restaurant_id %}
Restaurant identifier on orders.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_currency %}
Source currency; monetary values are not converted.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_restaurant_name %}
Restaurant name from the dimension.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_city %}
Restaurant city from the dimension.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_cuisine %}
Restaurant cuisine from the dimension.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_order_count %}
All order rows.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_delivered_order_count %}
Delivered order rows.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_delivered_sales_amount %}
Sum of delivered sales amount.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_avg_customer_rating %}
Average nonnull order customer rating.
{% enddocs %}

{% docs mart_restaurant_currency_lifetime_avg_delivery_time_min %}
Average nonnull delivered-order duration in minutes.
{% enddocs %}
