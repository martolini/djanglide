$(document).ready(function($) {
	// $("body").click(function(e) {
 // 	  var elClicked = e.target;
 //      if($(elClicked).is('#book-local-button')){
 //            startPopup();
 //      }
 //      else if(!($(elClicked).is('#pop-up-book')) &&  !($(elClicked).is('#book-local-button'))) {
 //         	closePopup();
 //      }
 // });
       $('#book-local-button').click(function(){
            startPopup();
       });
       $('#close-pop-up').click(function(){
            closePopup();
       })
});
function startPopup(){
		$("#pop-up-book").fadeTo('400', 1.0);
		$("#profile-body").fadeTo('400', 0.2);
}
function closePopup(){
		$("#pop-up-book").fadeTo('400', 0.0);
		$("#profile-body").fadeTo('400', 1.0);
}