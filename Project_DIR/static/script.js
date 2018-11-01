
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
});
