var $notlist = $("#notification-list");
var $notbubble = $(".notification-bubble");
var toggle = true;
var variable = 1;
var alreadySeen = false;
$(document).ready(function($) {
	$notbubble.click(function() {
    $notbubble.css('background-color', 'rgb(75,158,205)');
    $(".notification-bubble > p").html('0');
 	  if(toggle){
         slideOut();
         toggle = false;

     }
     else{
         slideIn();
         toggle = true;
     }
     if(alreadySeen){
      $("#notification-list").html('NO NOTIFICATIONS');
     }
     alreadySeen = true;

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