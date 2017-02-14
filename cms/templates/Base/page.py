{%- extends "Base/base.py" -%}
{%- block pagetitle -%}
<title>{{pageData.title}} :: {{s.siteName}}</title>
{%- endblock -%}
{%- block content -%}
<div class="col-md-12">
	<h1 class="page-header">
	{{pageData.title}}
	</h1>
	<article>
		{{ pageData.content|safe }}
	</article>
</div>
{%- endblock -%}
