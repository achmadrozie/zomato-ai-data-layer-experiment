{% macro assert_project1_target() %}
    {% if target.database | upper != 'ZOMATO_LAYER_REFACTOR' %}
        {{ exceptions.raise_compiler_error('Project 1 must target ZOMATO_LAYER_REFACTOR, not ' ~ target.database) }}
    {% endif %}
    select 1
{% endmacro %}
