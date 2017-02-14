{%- extends "Admin/base.py" -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">User Profile</h1>
              <form method="post" action="">
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" name="username" value="{{userData.username}}" readonly>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="email">Email</label>
                    <input type="text" class="form-control" id="email" name="email" value="{{userData.email}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="fullname">Name</label>
                    <input type="text" class="form-control" id="fullname" name="fullname" value="{{userData.name}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="image">Image</label>
                    <input type="text" class="form-control" id="image" name="image" value="{{userData.image}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="facebook">Facebook</label>
                    <input type="text" class="form-control" id="facebook" name="facebook" value="{{userData.facebook}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="twitter">Twitter</label>
                    <input type="text" class="form-control" id="twitter" name="twitter" value="{{userData.twitter}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="google">Google+</label>
                    <input type="text" class="form-control" id="google" name="google" value="{{userData.google}}">
                  </div>
                </div>
                <button type="submit" class="btn btn-success">Save User</button>
              </form>
              <form method="post" action="/admin/changepassword/">
                <input type="hidden" name="username" value="{{userData.username}}">
                <h2>Change Password</h2>
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
                <button type="submit" class="btn btn-success">Change Password</button>
              </form>
            </div>
        </div>
    </div>
</div>
{%- endblock -%}
