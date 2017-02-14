{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Add New User</h1>

        <form method="post" action="">
        <div class="row">
          <div class="form-group col-md-4">
            <label for="username">Username</label>
            <input type="text" class="form-control" id="username" name="username">
          </div>
        </div>

        <div class="row">
          <div class="form-group col-md-4">
            <label for="password1">Password</label>
            <input type="password" class="form-control" id="password1" name="password1">
          </div>
        </div>

        <div class="row">
          <div class="form-group col-md-4">
            <label for="password2">Confirm Password</label>
            <input type="password" class="form-control" id="password2" name="password2">
          </div>
        </div>

        <div class="row">
          <div class="form-group col-md-4">
            <label for="email">Email</label>
            <input type="text" class="form-control" id="email" name="email">
          </div>
        </div>

        <div class="row">
          <div class="form-group col-md-4">
            <button type="submit" class="btn btn-success">Add User</button>
          </div>
        </div>

	</form>

            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->
    </div>
    <!-- /.container-fluid -->
</div>
<!-- /#page-wrapper -->
{% endblock %}
