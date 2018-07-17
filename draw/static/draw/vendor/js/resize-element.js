



var fitToScreen = function(selector) {
    // the screen height
    var height = document.documentElement.clientHeight;
    // the screen width
    var width = document.documentElement.clientWidth;
    // $(selector).height = height;
    // $(selector).width = width;
    // alert(selector + "" + width + " " + height);
    // alert(selector + "" + $(selector).width() + " " + $(selector).height());
    $(selector).width(width);
    $(selector).height(height);
}

var fitToHeight = function(selector) {
    var height = document.documentElement.clientHeight;
    var width = document.documentElement.clientWidth;

    var originalWidth = $(selector).width();
    var originalHeight = $(selector).height();
    var newWidth = height * originalWidth / originalHeight;
    alert(newWidth + ", " + originalWidth + ", " +  originalHeight);
    var newHeight = height;

    $(selector).width(newWidth);
    $(selector).height(newHeight);
}

var fitToHeightWH = function(selector, width, height) {
    var originalWidth = $(selector).width();
    var originalHeight = $(selector).height();
    var newWidth = height * originalWidth / originalHeight;
    alert(newWidth + ", " + originalWidth + ", " +  originalHeight);
    var newHeight = height;

    $(selector).width(newWidth);
    $(selector).height(newHeight);
}

// var fitToWidth