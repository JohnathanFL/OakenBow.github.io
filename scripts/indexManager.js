$("#dynbody").load("scripts.html");

$(window).on('hashchange', function(e)) {
    $("#dynbody").load(window.location.hash + ".html")
}