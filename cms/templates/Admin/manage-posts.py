{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Posts</h1>
                <p><a href="/admin/posts/add/"><button class="btn btn-success">Add New</button></a></p>
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
                    {%- for entry in postData -%}
                    <tr>
                      <td>
                        {{ entry.title }}<br/>
                        <small>by: {{ entry.author }} on {{ moment(entry.date).format('MMMM Do YYYY, h:mm a') }}</small>
                      </td>
                      <td>{{ moment(entry.modified).format('MMMM Do YYYY, h:mm a') }}</td>
                      <td>
                        <a href="/admin/posts/edit/{{entry.id}}/"><button class="btn btn-success">Edit</button></a>
                        <a href="/admin/posts/delete/{{ entry.id }}/"><button class="btn btn-danger">Delete</button></a>
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
