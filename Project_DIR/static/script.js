
//to toggle active class of left menu with current page
$(document).ready(function () {
    var url = window.location;
    $('.left-nav-btn-div a[href="'+ url +'"]').parent().addClass('left-nav-active');
    $('.left-nav-btn-div a').filter(function() {
         return this.href == url;
    }).parent().addClass('left-nav-active');
    console.log("hey");

});
