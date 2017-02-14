{%- extends "Base/base.py" -%}
{%- block header -%}{%- endblock -%}{%- block content -%}
<div id="loginModal" class="modal show" tabindex="-1" role="dialog" aria-hidden="true" style="margin-top:10em">
  <div class="modal-dialog">
  <div class="modal-content">
      <div class="modal-header">
	{#-<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>-#}
          <h1 class="text-center">{{s.siteName}} Login</h1>
      </div>
      <div class="modal-body">
          <form class="form col-md-12 center-block" method="post">
            <div class="form-group">
              <input type="text" name="username" class="form-control input-lg" placeholder="Username">
            </div>
            <div class="form-group">
              <input type="password" name="password" class="form-control input-lg" placeholder="Password">
            </div>
            <div class="form-group">
              <button class="btn btn-primary btn-lg btn-block">Sign In</button>
              {#<span class="pull-right"><a href="#">Register</a></span><span><a href="#">Need help?</a></span>#}
            </div>
          </form>
      </div>
      <div class="modal-footer">
          <div class="col-md-12">
            {#-<button class="btn" data-dismiss="modal" aria-hidden="true">Cancel</button>-#}
          </div>
      </div>
  </div>
  </div>
</div>
{%- endblock -%}{%- block footer -%}{%- endblock -%}
