{{ fullname }}
{{ underline }}

.. autoclass:: {{ name }}

    {% block methods %}
    .. automethod:: __init__

    {% if methods %}
    .. rubric:: Methods

    .. autosummary::
    {% for item in methods %}
       ~{{ name }}.{{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    .. raw:: html

        <br>

    {% block attributes %}
    {% if attributes %}
    .. rubric:: Attributes

    .. autosummary::
    {% for item in attributes %}
       ~{{ name }}.{{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}
