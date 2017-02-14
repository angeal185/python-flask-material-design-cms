{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Pages</h1>
                <p><a href="/admin/pages/add/"><button class="btn btn-success">Add New</button></a></p>
              <div class="table-responsive">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th>Title</th>
                      <th>Last Update</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {%- for entry in pageData -%}
                    <tr>
                      <td>{{ entry.title }}</td>
                      <td>{{ moment(entry.modified).format('MMMM Do YYYY, h:mm a') }}</td>
                      <td>
                        <a href="/admin/pages/edit/{{entry.id}}/"><button class="btn btn-success">Edit</button></a>
                        <a href="/admin/pages/delete/{{ entry.id }}/"><button class="btn btn-danger">Delete</button></a>
                        <a href="{{entry.slug}}" target="_blank"><button class="btn btn-primary">View</button></a>
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
