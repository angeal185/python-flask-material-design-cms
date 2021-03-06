{%- extends "Base/base.py" -%}
{%- block content -%}
<div class="col-md-12">
	<h1 class="page-header">
	{{s.siteName}}<br/>
		<small>{{s.siteSubheading}}</small>
	</h1>
{%- for b in blogData -%}
<h2><a href="{{b.slug}}">{{b.title}}</a></h2>
<p>by <a href="/author/{{b.author}}">{{b.author}}</a> <span class="glyphicon glyphicon-time"></span> Posted on {{ moment(b.date).format('MMMM Do YYYY, h:mm a') }}</p>
<img class="img-responsive" src="{{b.image}}" alt="">
<hr>
<p>{{first_paragraph(b.content|safe)}}</p>
<a class="btn btn-primary" href="{{b.slug}}">Read More <span class="glyphicon glyphicon-chevron-right"></span></a>
{%- endfor -%}
</div>
{%- endblock -%}
