var $notlist = $("#notification-list");
var $notbubble = $(".notification-bubble");
var toggle = true;
$(document).ready(function($) {
	$notbubble.click(function() {

 	  if(toggle){
         slideOut();
         toggle = false;
     }
     else{
         slideIn();
         toggle = true;
     }
 });
});
function slideOut(){
		$notlist.slideDown('400', function() {
         
      });
}
function slideIn(){
		$notlist.slideUp('400', function() {
         
      });
}