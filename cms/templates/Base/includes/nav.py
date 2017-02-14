<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
	<div class="container">
		<div class="navbar-header">
			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
{% for navS in navS %}<span class="{{navS.class}}"></span>{% endfor %}
			</button>
			<a class="navbar-brand" href="/">{{s.siteName}}</a>
		</div>
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
{% for navL in navL %}<li><a href="/{{navL.href}}">{{navL.name}}</a></li>{% endfor %}
	{% if g.user.is_authenticated %}
{% for navAuth in navAuth %}<li><a href="/{{navAuth.href}}">{{navAuth.name}}</a></li>{% endfor %}
		{% else %}<li><a href="/login/">Login</a></li>{% endif %}
			</ul>
		</div>
	</div>
</nav>