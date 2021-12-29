//sidebar
function w3_open() {
		document.getElementById("Sidebar").style.display = "block";
		document.getElementById("Overlay").style.display = "block";
}

function w3_close() {
		document.getElementById("Sidebar").style.display = "none";
		document.getElementById("Overlay").style.display = "none";
}



//top button
var mybutton = document.getElementById("topBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {

		if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
				mybutton.style.display = "block";
		} else {
				mybutton.style.display = "none";
		}

}


function topFunction() {

		document.body.scrollTop = 0;
		document.documentElement.scrollTop = 0;

}



//voice meeting 

$(function(){

          var winW = $(window).width();
		var winH = $(window).height();
		var maxHeight = winH;

		if (winW <= 767) {
				$('.user_speech_content_area').css('max-height','none');
		} else {
				$('.user_speech_content_area').css("max-height", maxHeight - 150);
		}
})


$(window).resize(function () {

          var winW = $(window).width();
		var winH = $(window).height();

          if (winW <= 767) {

				$('.real_time_list_area').show();
				$('.real_time_list').addClass('active');
          		$('.user_speech_area').hide();
				$('.user_speech').removeClass('active');
				$('.user_speech_content_area').css('max-height','none');

          } else {

				$('.real_time_list_area').show();
				$('.user_speech_area').show();
          		var maxHeight = winH - 150;

          }

          $('.user_speech_content_area').css("max-height", maxHeight);
          
});


$('.user_speech').click(function () {
		$('.user_speech_area').show();
		$('.real_time_list_area').hide();
		$('.user_speech').addClass('active');
		$('.real_time_list').removeClass('active');
})

$('.real_time_list').click(function () {
		$('.user_speech_area').hide();
		$('.real_time_list_area').show();
		$('.real_time_list').addClass('active');
		$('.user_speech').removeClass('active');
})





//
$(function () {
		$('[data-toggle="popover"]').popover()
})