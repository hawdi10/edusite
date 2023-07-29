var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
	return new bootstrap.Tooltip(tooltipTriggerEl)
});

jQuery(".responsive-menu-body ul li").has("ul").append("<span class='responsive-menu-span'><i class='bi bi-caret-down-fill'></i></span>");

jQuery(".responsive-menu-body ul li .responsive-menu-span").click(function () {
	jQuery(this).prev("ul").slideToggle();
	jQuery(this).find("i").toggleClass("bi-caret-down-fill");
	jQuery(this).find("i").toggleClass("bi-caret-up-fill");
});

jQuery(".Header-Panel-Access").click(function(){
	jQuery(".Header-Panel-Access-holder").toggleClass("Header-Panel-Access-holder-show");
});

jQuery('.products-slider').owlCarousel({
	loop: false,
	margin: 10,
	autoplay: true,
	rtl: true,
	dots: false,
	nav: true,
	responsiveClass: true,
	autoplayHoverPause:true,
	responsive: {
		0: {
			items: 1,
		},
		400: {
			items: 2,

		},
		600: {
			items: 3,

		},
		1000: {
			items: 4,
		}
	}
});

jQuery('.products-slider-rel').owlCarousel({
	loop: false,
	margin: 10,
	autoplay: true,
	rtl: true,
	dots: false,
	nav: false,
	responsiveClass: true,
	autoplayHoverPause:true,
	responsive: {
		0: {
			items: 1,
		},
		400: {
			items: 2,

		},
		600: {
			items: 3,

		},
		1000: {
			items: 5,
		}
	}
});

jQuery('.products-slider-category').owlCarousel({
	loop: false,
	margin: 10,
	autoplay: true,
	rtl: true,
	dots: false,
	nav: true,
	responsiveClass: true,
	autoplayHoverPause:true,
	responsive: {
		0: {
			items: 1,
		},
		400: {
			items: 2,

		},
		600: {
			items: 3,

		},
		800: {
			items: 4,

		},
		1000: {
			items: 5,
		}
	}
});

jQuery('.index-slider-wrap').owlCarousel({
	loop: true,
	margin: 0,
	autoplay: true,
	rtl: true,
	dots: false,
	nav: true,
	responsiveClass: true,
	autoplayHoverPause:true,
	responsive: {
		0: {
			items: 1,
		},
		1000: {
			items: 1,
		}
	}
});

jQuery('.single-product-gallery-min').owlCarousel({
	loop: false,
	margin: 7,
	autoplay: true,
	rtl: true,
	dots: false,
	nav: false,
	responsiveClass: true,
	autoplayHoverPause:true,
	responsive: {
		0: {
			items: 4,
		},
		576: {
			items: 5,
		},
		1000: {
			items: 6,
		}
	}
});

jQuery('.timer').startTimer();

jQuery(".scroll-top").click(function(){
	jQuery("body,html").animate({
		scrollTop: 0
	}, 1000);
});

jQuery(".filter-item-main .filter-box-show").click(function(){
	jQuery(this).next().slideToggle();
});

jQuery(".faq-item-title").click(function(){
	jQuery(this).next("div").slideToggle();
	jQuery(this).find("i").toggleClass("bi-chevron-down");
	jQuery(this).find("i").toggleClass("bi-chevron-up");
});