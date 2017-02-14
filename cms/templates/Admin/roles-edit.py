{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Edit Role</h1>

  <form class="myElements" method="post" action="">
  Name<br/><input id="name" type="text" name="name" value="{{role.rolename}}" size="40" max="255" required><br/>
  Description<br/><input id="description" class="" type="text" name="description" value="{{role.roledesc}}" size="40" max="255" required><br/><br/>

  Edit User(s)<br/>
  {% for u in u %}
    <input class="" type="checkbox" value="{{u.id}}" name="atr" {% for r in roleMembers %}{% if u.id == r.user_id %}checked="checked"{% endif %}{% endfor %}> {{get_displayname(u.id)}}<br/>
  {% endfor %}
  <br/>

  <button type="submit" class="btn btn-success">Save</button>

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
