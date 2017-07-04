$(document).ready(function() {
	//Show or Hide Content
	$("a").click(function() {
		var href = $(this).attr('href');
        $(href).show();
        $(href).siblings().hide();
	});
	//Stick Nav to top of Window
	var nav = $('#nav');
	var navHomeY = nav.offset().top;
	var isFixed = false;
	var $w = $(window);
	$w.scroll(function() {
		var scrollTop = $w.scrollTop();
		var shouldBeFixed = scrollTop > navHomeY;
		if (shouldBeFixed && !isFixed) {
			nav.css({
				position:'fixed',
				top:0,
				left:nav.offset().left,
				width:nav.width()
			});
			isFixed = true;
		}
		else if (!shouldBeFixed && isFixed) {
			nav.css({position:'static'});
			isFixed = false;
		}
	});
});