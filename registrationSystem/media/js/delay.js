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

$(document).ready(function(){
		if(window.location.pathname == "/response")
			delayURL("/");
		else
			delayURL("/entry");
});
