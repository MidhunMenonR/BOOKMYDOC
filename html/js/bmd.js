/*NAVBAR*/

function openNav() {
	document.getElementById("mySidenav").style.width = "300px";
    document.getElementById("main").style.marginLeft = "300px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav(page) {
   	document.getElementById("mySidenav").style.width = "0";
	document.getElementById("main").style.marginLeft= "0";
    if (page ==1) {
    	document.body.style.backgroundColor = "white";
    }
    else if (page ==2) {
    	document.body.style.backgroundColor = "lightgrey";
    }
    
}

/*tab*/

function openTab(tab) {
	    var i;
	    var x = document.getElementsByClassName("tabContent");
	    for (i = 0; i < x.length; i++) {
	       x[i].style.display = "none";  
	    }
	    document.getElementById(tab).style.display = "block";  
	}