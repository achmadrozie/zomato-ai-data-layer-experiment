{% macro assert_project1_target() %}
    {% if target.database | upper != 'ZOMATO_DLR' %}
        {{ exceptions.raise_compiler_error('Project 1 must target ZOMATO_DLR, not ' ~ target.database) }}
    {% endif %}
    select 1
{% endmacro %}
