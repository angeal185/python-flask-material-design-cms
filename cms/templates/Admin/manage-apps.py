{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Apps</h1>
                <p>
                  <a href="/admin/plugins/restart/"><button class="btn btn-danger">Destroy</button></a>
                </p>
				<div class="table-responsive">
				<table class="table table-striped">
				  <tbody>
				  {%- for p in pluginData -%}
				  <tr>
					<td width="325">
					  <img src="{{p.basics.image}}" width="325">
					</td>
					<td>
					  {{p.basics.name}} {{p.basics.version}}<br/>
					  {{p.basics.summary|safe}}<br/>
					  <a href="{{p.basics.website}}" target="_blank">{{p.basics.website}}</a><br/>
					  <a href="mailto:{{p.basics.email}}">{{p.basics.email}}<br/>
					  <br/>
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
