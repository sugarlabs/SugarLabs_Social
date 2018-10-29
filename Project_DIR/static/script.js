
//to toggle active class of left menu with current page
$(document).ready(function () {
    var url = window.location;
    $('.left-nav-btn-div a[href="'+ url +'"]').parent().addClass('left-nav-active');
    $('.left-nav-btn-div a').filter(function() {
         return this.href == url;
    }).parent().addClass('left-nav-active');

    $('.left-nav-btn-div a[href="'+ url +'"]').parent().addClass('left-nav-active');
    $('.left-nav-btn-div a').filter(function() {
         return this.href == url;
    }).parent().addClass('left-nav-active');
//any images with the zoomimg will be zoomed in using viewer js when clicked
    $( ".zoomimg" ).click(function(e) {
        var viewer = new Viewer(e.toElement, {
          button: true,
          transition: true,
          backdrop: true,
          navbar: false,
          toolbar: false,
          title: false,
          tooltip: false,
          hidden: function () {
            viewer.destroy();
          },
        });

        // image.click();
        viewer.show();
      });
      $( ".pzoomimg" ).click(function(e) {
        var img = new Image();
        img.src = (e.toElement.style.backgroundImage.split("\""))[1];
        console.log(img.src);
        var viewer = new Viewer(img, {
          button: true,
          transition: true,
          backdrop: true,
          navbar: false,
          toolbar: false,
          title: false,
          tooltip: false,
          hidden: function () {
            viewer.destroy();
          },
        });

        // image.click();
        viewer.show();
      });

});
