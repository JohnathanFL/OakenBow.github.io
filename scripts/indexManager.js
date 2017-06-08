if (window.location.hash) {
    $("#dynbody").load(window.location.hash);
}
$(window).on('hashchange', function (e) {
    $("#dynbody").load(window.location.hash + ".html")
})