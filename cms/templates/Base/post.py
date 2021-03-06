{% extends "Base/base.py" %}

{% block pagetitle %}
  <title>{{postData.title}} :: {{s.siteName}}</title>
{% endblock %}

{% block content %}
  <div class="col-md-8">
       <h1 class="page-header">
          {{postData.title}}
       </h1>

       <p>by <a href="#">{{postData.author}}</a> <span class="glyphicon glyphicon-time"></span> Posted on {{moment(postData.date).format('MMMM Do YYYY, h:mm a') }}</p>
       <img class="img-responsive" src="{{postData.image}}" alt="">
       <hr>

       {{ postData.content|safe}}

       {% if postData.tags|length > 0 %}
       <br/><small>Tags: {{process_tags(postData.tags)|safe}}</small><br/><br/>
       {% endif %}

       {{ s.commentCode|safe }}

  </div>

  <div class="col-md-4">

    <div class="well">
    {{ s.siteAds|safe }}
    </div>

  </div>

{% endblock %}
