function htmlDecode(input){
		var e = document.createElement('div');
		e.innerHTML = input;
		return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
	}
function addZero(i) {
    if (i < 10) {
      i = "0" + i;
    }
    return i;
}
function tempFtoC(fahrenheit) {
    return (fahrenheit - 32) / 1.8;
}
function tempCtoF(celsius){
    return celsius * 1.8 + 32;
}
function tempFtoK(fahrenheit) {
    return (fahrenheit + 459.67) * 5 / 9;
}
function nothing(obj) {
    return obj;
}
  
var INPUT_TEMP_MODE = "fahrenheit";
var tempSetting = "celsius";
var TEMP_FUNC_ENUM = Object.freeze({"celsius":tempFtoC, "fahrenheit":nothing, "kelvin":tempFtoK});
var ICON_ENUM =  Object.freeze({"clear-day":"☀️", "clear-night":"☀️", "rain":"🌧️",
    "snow":"🌨️","sleet":"⛆","wind":"💨","fog":"🌫️️","cloudy":"☁️",
    "partly-cloudy-day":"⛅","partly-cloudy-night":"⛅",
    /* The following features are not defined yet*/"hail":"💧","thunderstorm":"💧","tornado":"💧"});

var MONTH_LIST = Object.freeze(["January", "February", "March", "April", "May", "June", "July",
                                "Auguest", "September", "October", "November", "December"]);
var MONTH_SHORT_LIST = Object.freeze(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                                    "Aug", "Sep", "Oct", "Nov", "Dec"]);

String.prototype.format = function () {
    var i = 0, args = arguments;
    return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
    });
};