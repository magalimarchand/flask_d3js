$(document).ready(function() {

//to reload the page when resising the window
window.onresize = function(){ location.reload(); }

//to adjust the display of the navbar login dropdown
$('.dropdown-menu').offset({left:-60});

//to display the sidebar based on the selected navbar item url path
if(window.location.pathname.startsWith('/hardware')) 
	$('#ul_01').show();
else if(window.location.pathname.startsWith('/elasticsearch')) 
	$('#ul_02').show();
else if(window.location.pathname.startsWith('/splunk')) 
	$('#ul_03').show();
else if(window.location.pathname.startsWith('/centreon')) 
	$('#ul_04').show();
else if(window.location.pathname.startsWith('/examples')) 
	$('#ul_06').show();
else $('#ul_00').show();


});