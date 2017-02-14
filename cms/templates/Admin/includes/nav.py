<nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
	<div class="navbar-header">
		<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
{% for navS in navS %}<span class="{{navS.class}}"></span>{% endfor %}
		</button>
		<a class="navbar-brand" href="/">{{ s.siteName }} Home</a>
	</div>
	<ul class="nav navbar-top-links navbar-right">
{% for navAuth in navAuth %}<li><a href="/{{navAuth.href}}">{{navAuth.name}}<i class="fa fa-{{navAuth.icon}} fa-fw"></i></a></li>{% endfor %}
	</ul>
	<div class="navbar-default sidebar" role="navigation">
		<div class="sidebar-nav navbar-collapse">
			<ul class="nav" id="side-menu">
				{% for navL in navL %}<li><a href="/{{navL.href}}"><i class="fa fa-{{navL.icon}} fa-fw"></i> {{navL.name}}</a></li>{% endfor %}
			</ul>
		</div>
	</div>
</nav>