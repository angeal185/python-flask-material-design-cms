{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Users</h1>
                <p>
                  <a href="/admin/users/add/"><button class="btn btn-success">Add New</button></a>
                </p>
              <div class="table-responsive">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th>Username</th>
                      <th>Email</th>
                      <th>Registered</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {%- for entry in userData -%}
                    <tr>
                      <td>{{ entry.username }}</td>
                      <td><a href="mailto:{{ entry.email }}">{{ entry.email }}</a></td>
                      <td>{{ moment(entry.registered_on).format('MMMM Do YYYY, h:mm a') }}</td>
                      <td>
                        <a href="/admin/users/profile/{{entry.username}}/"><button class="btn btn-primary">Edit</button></a>
                        <a href="/admin/users/delete/{{ entry.id }}/"><button class="btn btn-danger">Delete</button></a>
                      </td>
                    </tr>
                    {%- endfor -%}
                  </tbody>
                </table>
              </div>
            </div>
        </div>
    </div>
</div>
{%- endblock -%}
