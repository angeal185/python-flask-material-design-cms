{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Roles</h1>
                <p><a href="/admin/users/roles/add/"><button class="btn btn-success">Add New</button></a></p>

   <div class="table-responsive">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>Role</th>
          <th>Description</th>
          <th>Members</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>

      {% for r in roles %}
      <tr>
         <td>{{r.rolename}}</td>
         <td>{{r.roledesc}}</td>
         <td>{{ get_role_num(r.id) }}</td>
         <td><a href="/admin/users/roles/edit/{{r.id}}/"><button class="btn btn-primary">Edit</button></a> {% if r.rolename != "SuperAdmin" %} <a href="/admin/users/roles/delete/{{r.id}}/"><button class="btn btn-danger">Delete</button></a></td>{% endif %}
      </tr>
      {% endfor %}

      </tbody>
    </table>
  </div>

            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
    </div>
    <!-- /.container-fluid -->
</div>
<!-- /#page-wrapper -->
{% endblock %}
