{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Add New Plugin</h1>

        {% for p in pluginData %}
        <div class="row">
            <div class="col-md-4">
                <img class="img-responsive img-hover" src="{{p.plugin_image}}" alt="">
            </div>
            <div class="col-md-8">
                <h3>{{p.plugin_name}} {{p.plugin_version}}</h3>
                <h4>{{p.plugin_tags}}</h4>
                <p>{{p.plugin_summary}}</p>
                <a class="btn btn-success" href="/admin/plugins/install/{{p.plugin_directory}}/">Install Plugin</i></a>
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
