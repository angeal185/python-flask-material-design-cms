{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Files</h1>
              <h2>Upload New File</h2>
              <form action="" method=post enctype=multipart/form-data>
                <span class="btn btn-default btn-file"><input type="file" name="file"></span>
                <button type="submit" class="btn btn-success">Upload</button>
              </form>
              <hr>
              <h2>File Manager</h2>
              Current path: {{config.UPLOAD_FOLDER}}{%- if request.args.get('path') -%}{{ request.args.get('path') }}{%- endif -%}
              <div class="table-responsive">
                <table class="table table-striped">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>Size</th>
                      <th>Modified Time</th>
                      <th>Delete?</th>
                    </tr>
                  </thead>
                  <tbody>
                    {%- for item in tree.children recursive -%}
                    <tr>
                      {%- if item.size -%}
                      <td><i class="fa fa-file fa-fw"></i> <a href="/static/upload/{{item.name}}" target="_blank">{{item.name}}</a></td>
                      <td>{{ item.size|filesizeformat(item.size) }}</td>
                      <td>{{ moment(item.mtime).format('MMMM Do YYYY, h:mm a') }}</td>
                      {%- if request.args.get('path') -%}
                      <td><a href="/admin/files/delete/?path={{ request.args.get('path') }}&filename={{item.name}}">
                        <button class="btn btn-danger">Delete</button></a>
                      </td>
                      {%- else -%}
                      <td><a href="/admin/files/delete/?filename={{item.name}}"><button class="btn btn-danger">Delete</button></a></td>
                      {%- endif -%}
                      {%- else -%}
                      <td><i class="fa fa-folder fa-fw"></i> <a href="/admin/files?path={{item.name}}/">{{item.name}}</a></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      {%- endif -%}
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
