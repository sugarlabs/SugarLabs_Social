
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
    checkNav()
    $(window).scroll(function () {
        checkNav()
        });
    function checkNav() {
        if($(window).scrollTop() >= 60) {
            $(".left-nav").css("margin-top", "-5%");
            $(".left-nav").css("padding-top", "3%")
            $(".btn-add-left-nav").css("margin-top", "50px")
        } else {
            $(".left-nav").css("margin-top", "0");
            $(".left-nav").css("padding-top", "0")
            $(".btn-add-left-nav").css("margin-top", "0")
        }
    }
//any images with the zoomimg will be zoomed in using viewer js when clicked
    $( ".zoomimg" ).click(function(e) {
        var viewer = new Viewer($(this).get(0), {
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
        img.src = ($(this).get(0).style.backgroundImage.split("\""))[1];
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
