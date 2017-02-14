{% extends "Admin/base.py" %}

{% block pagewrapper %}
<!-- Page Content -->
<div id="page-wrapper">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-12">
                <h1 class="page-header">Add New Page</h1>

  <form class="myElements" method="post" action="">
  <div style="margin-bottom:25px;">
    <div style="float:left;margin-right:10px;">
      Page Title<br/><input id="title" type="text" name="title" value="" size="70" required>
    </div>

    <div style="float:left;">
      Page URL<br/><input id="slug" type="text" name="slug" value="" size="40" required>
    </div>
    <div style="clear:both;"></div>
  </div>

  <textarea id="content" name="content" rows="25" cols="60"></textarea>

  <div style="width:300px;float:left;margin-bottom:7px;margin-top:10px;">
    Subheading Text<br><small>(shown under title, optional)</small><br/><input type="text" name="subheading" value="" size="70" placeholder="Optional">
  </div>
  <div style="clear:both;"></div>

  <div style="width:300px;float:left;margin-bottom:7px;margin-top:10px;">
    Featured IMG URL<br><small>(best w:1900px, height:600-872px)</small><br/><input type="text" name="featureimg" value="" size="70" placeholder="Optional">
  </div>
  <div style="clear:both;"></div>

  <!-- <input type="submit" value="Save"> -->
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

{% block footerjs %}
<script src="//cdn.ckeditor.com/4.5.8/standard/ckeditor.js"></script>
<script>
CKEDITOR.replace('content',{
    width: '100%',
    height: '400px',
    uiColor: '#9AB8F3'
});
</script>

<script>
$(document).ready(function () {
  $("#title").bind("keyup input paste", function() {
    var bla = $('#title').val().toLowerCase().replace(/ /g,"-").replace(/,|<|>|'|!|@|#/g,"");
    $("#slug").val("/" + bla + "/");
  });
});
</script>
{% endblock %}
