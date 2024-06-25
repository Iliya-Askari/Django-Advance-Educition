{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}

{% block html %}
<p>This is an <strong>html</strong> message.</p>
<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKTezalux1__3KwbJ1Bt-WnQQkW82G1Nwy6g&s" alt="Nature Image"></p>
{% endblock %}
