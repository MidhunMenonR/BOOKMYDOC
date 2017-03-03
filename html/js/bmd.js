

//document.getElementById("myBtn").addEventListener("click", displayDate);

/*NAVBAR*/

function openNav() {
	if(screen.width >768){
		document.getElementById("mySidenav").style.width = "300px";
	    document.getElementById("main").style.marginLeft = "300px";
    }
    else{
    	document.getElementById("mySidenav").style.width = "150px";
	    document.getElementById("main").style.marginLeft = "150px";	
    }

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

function openTab(tab,tabnum) {
	    var i;
	    var x = document.getElementsByClassName("tabContent");
	    for (i = 0; i < x.length; i++) {
	       x[i].style.display = "none";  
	    }
	    document.getElementById(tab).style.display = "block";
	    if (tabnum==1) {
	    	document.getElementById('tab1').style.borderTop = "solid 10px black"; 
	    	document.getElementById('tab2').style.border = "none"; 
	    	document.getElementById('tab3').style.border = "none"; 
	    	document.getElementById('tab1').style.backgroundColor = "white";
	    	document.getElementById('tab2').style.backgroundColor = "black";
	    	document.getElementById('tab3').style.backgroundColor = "black";

	    	document.getElementById('tablink1').style.color = "black";
	    	document.getElementById('tablink2').style.color = "white";
	    	document.getElementById('tablink3').style.color = "white";
	    } 
	    else if (tabnum==2) {
	    	document.getElementById('tab2').style.borderTop = "solid 10px black"; 
	    	document.getElementById('tab1').style.border = "none"; 
	    	document.getElementById('tab3').style.border = "none";
	    	document.getElementById('tab2').style.backgroundColor = "white";
	    	document.getElementById('tab1').style.backgroundColor = "black";
	    	document.getElementById('tab3').style.backgroundColor = "black"; 

	    	document.getElementById('tablink2').style.color = "black";
	    	document.getElementById('tablink1').style.color = "white";
	    	document.getElementById('tablink3').style.color = "white";
	    } 
	    else{
	    	document.getElementById('tab3').style.borderTop = "solid 10px black"; 
	    	document.getElementById('tab2').style.border = "none"; 
	    	document.getElementById('tab1').style.border = "none"; 
	    	document.getElementById('tab3').style.backgroundColor = "white";
	    	document.getElementById('tab2').style.backgroundColor = "black";
	    	document.getElementById('tab1').style.backgroundColor = "black";

	    	document.getElementById('tablink3').style.color = "black";
	    	document.getElementById('tablink2').style.color = "white";
	    	document.getElementById('tablink1').style.color = "white";
	    } 
}

/*Search*/



