function delayURL(url) {
    var delay = $("#time").html();
    if(delay > 0) {
        delay--;
        $("#time").html(delay);
    } else {
        window.top.location.href = url;
    }
    setTimeout("delayURL('" + url + "')", 1000);
}

$(document).ready(delayURL("/"))
