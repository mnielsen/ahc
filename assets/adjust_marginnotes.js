// Adjust the locations of the marginnotes so they're placed in the
// right spot, not too wide, and not overlapping with earlier notes.

var marginNotes = [].slice.call(
    document.getElementsByClassName("marginnote"));
var containerStyle = getComputedStyle(
    document.getElementById("container"));

function getStyleInt(style) {
    return parseInt(style.replace("px", ""));
}

resize = function() {
    var containerRight = getStyleInt(containerStyle["margin-left"])+
	getStyleInt(containerStyle.width);
    var possibleWidth = innerWidth-(0.72/0.7)*containerRight-40;
    var lastBottom = 0;
    var sidebar = document.getElementById("sidebar");
    if (sidebar) {
	var sidebarStyle = getComputedStyle(sidebar);
	lastBottom = getStyleInt(sidebarStyle.top)+
	    getStyleInt(sidebarStyle.height)+20;
    }
    for (var j=0; j < marginNotes.length; j++) {
	var note = marginNotes[j];
	note.style.left = "72%"; //(containerRight+40)+"px";
	note.style.width = Math.min(300, possibleWidth)+"px";
	var style = getComputedStyle(note);
	var top = getStyleInt(style.top);
	var height = getStyleInt(style.height);
	if (top < lastBottom+10) {
	    top = lastBottom+10;
	    note.style.top = top+"px";
	};
	lastBottom = top+height;
    };
}

window.onresize = resize;
resize();

