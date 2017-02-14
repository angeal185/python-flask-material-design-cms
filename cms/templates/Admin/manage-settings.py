{%- extends "Admin/base.py" -%}
{%- block headjs -%}
<script src="//cdnjs.cloudflare.com/ajax/libs/jscolor/2.0.4/jscolor.min.js" type="text/javascript"></script>
{%- endblock -%}
{%- block pagewrapper -%}
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Manage Settings</h1>
              <form method="post" action="">
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="siteName">Site Name</label>
                    <input type="text" class="form-control" id="siteName" name="siteName"value="{{s.siteName}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="siteSubheading">Site SubHeading</label>
                    <input type="text" class="form-control" id="siteSubheading" name="siteSubheading" value="{{s.siteSubheading}}">
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="commentCode">Comment Code (Disqus)</label>
                    <textarea class="form-control" rows="3" id="commentCode" name="commentCode">{{s.commentCode}}</textarea>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="googleAnal">Google Analytics</label>
                    <textarea class="form-control" rows="3" id="googleAnal" name="googleAnal">{{s.googleAnal}}</textarea>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <label for="siteAds">Adsense/Ad Code</label>
                    <textarea class="form-control" rows="3" id="siteAds" name="siteAds">{{s.siteAds}}</textarea>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group col-md-4">
                    <button type="submit" class="btn btn-default">Save Settings</button>
                  </div>
                </div>
              </form>
            </div>
        </div>
    </div>
</div>
{%- endblock -%}
