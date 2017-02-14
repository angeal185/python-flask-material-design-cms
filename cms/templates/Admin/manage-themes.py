{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Themes</h1>
                <p><a href="/admin/themes/add/"><button class="btn btn-success">Add New</button></a></p>
              <div class="table-responsive">
                <table class="table table-striped">
                  <tbody>
                    <tr>
                      <td width="325">
                        <img src="{{activeTheme.basics.image}}" width="325">
                      </td>
                      <td>
                        <strong>{{activeTheme.basics.name}} {{activeTheme.basics.version}}</strong>
                        <button class="btn btn-primary btn-xs" type="button">Active Theme!</button><br/>
                        {{activeTheme.basics.summary}}<br/>
                        <a href="{{activeTheme.basics.website}}" target="_blank">{{activeTheme.basics.website}}</a><br/>
                        <a href="mailto:{{activeTheme.basics.email}}">{{activeTheme.basics.email}}</a><br/>
                      </td>
                    </tr>
                    
                    {%- for t in themeData -%}
                    {%- if t.basics.directory != s.theme -%}
                    <tr>
                      <td width="325">
                        <img src="{{t.basics.image}}" width="325">
                      </td>
                      <td>
                        <strong>{{t.basics.name}} {{t.basics.version}}</strong><br/>
                        {{t.basics.summary}}<br/>
                        <a href="{{t.basics.website}}" target="_blank">{{t.basics.website}}</a><br/>
                        <a href="mailto:{{t.basics.email}}">{{t.basics.email}}</a><br/>
                        <br/>
                        <a href="/admin/themes/activate/{{t.basics.directory}}/"><button class="btn btn-success">Activate</button></a>
                        <a href="/admin/themes/delete/{{t.basics.directory}}/"><button class="btn btn-danger">Delete</button></a>
                      </td>
                    </tr>
                    {%- endif -%}
                    {%- endfor -%}
                  </tbody>
                </table>
              </div>
            </div>
        </div>
    </div>
</div>
{%- endblock -%}
