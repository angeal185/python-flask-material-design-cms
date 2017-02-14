<!DOCTYPE html>
<html lang="{{meta.lang}}">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{{meta.description}}">
<meta name="author" content="{{meta.author}}">
<title>{{ s.siteName }} :: Admin</title>
{%- include "Admin/includes/css.py" -%}
{%- block headjs -%}{%- endblock -%}
</head>
<body>
<div id="wrapper">
{%- include "Admin/includes/nav.py" -%}
{%- block pagewrapper -%}
    <div id="page-wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header">Blank</h1>
                </div>
            </div>
        </div>
    </div>
{%- endblock -%}
</div>
{%- include "Admin/includes/footerJs.py" -%}
<script></script>
{{ moment.include_moment() }}
{% block footerjs %}{% endblock %}
</body>
</html>
