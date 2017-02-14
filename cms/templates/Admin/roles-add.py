{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Add New Role</h1>

  <form class="myElements" method="post" action="">
  Name<br/><input id="name" type="text" name="name" value="" size="40" max="255" required><br/>
  Description<br/><input id="description" type="text" name="description" value="" size="40" max="255" required><br/><br/>

  Add Existing User(s)<br/>
  {% for u in u %}
    <input type="checkbox" value="{{u.id}}" name="atr"> {{u.username}}<br/>
  {% endfor %}
  <br/>

  <button type="submit" class="btn btn-success">Add</button>

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
