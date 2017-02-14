<!DOCTYPE html>
<html lang="{{meta.lang}}">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{{meta.description}}">
<meta name="author" content="{{meta.author}}">
{%- block pagetitle -%}
<title>{{s.siteName}} :: {{s.siteSubheading}}</title>
{%- endblock -%}
{%- include "Base/includes/css.py" -%}
<style type="text/css">
  body {
	padding: 70px;
  }
</style>
{%- block styles -%}{%- endblock -%}
</head>
<body>
{%- block header -%}{%- include "Base/includes/nav.py" -%}{%- endblock -%}
{%- block container -%}
<div class="container">
	<div class="row">
		{%- block content -%}{%- endblock -%}
	</div>
</div>
{%- endblock -%}
{%- block footer -%}
{%- include "Base/includes/footer.py" -%}
{%- endblock -%}
{%- include "Base/includes/footerJs.py" -%}
{{ moment.include_moment() }}
{{s.googleAnal|safe}}
</body>
</html>
