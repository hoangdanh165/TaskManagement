$(document).ready(function() {
    var $alert = $(".alert");
    // Start the alert fade out after 4 seconds
    window.setTimeout(function() {
        $alert.fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 4000);
});

$(document).ready(function() {
    $('.progress-bar').animate({width: "100%"}, 4000);
});