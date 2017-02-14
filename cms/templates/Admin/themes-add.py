{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Add New Theme</h1>

        {% for t in themeData %}
        <div class="row">
            <div class="col-md-4">
                <img class="img-responsive img-hover" src="{{t.theme_image}}" alt="">
            </div>
            <div class="col-md-8">
                <h3>{{t.theme_name}} {{t.theme_version}}</h3>
                <h4>{{t.theme_tags}}</h4>
                <p>{{t.theme_summary}}</p>
                <a class="btn btn-success" href="/admin/themes/install/{{t.theme_directory}}/">Install Theme</i></a>
            </div>
        </div>
        <hr>
        {% endfor %}

            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
    </div>
    <!-- /.container-fluid -->
</div>
<!-- /#page-wrapper -->
{% endblock %}
