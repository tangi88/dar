$(document).ready(function(){

	var sitePlusMinus = function() {
		$('.js-btn-minus').on('click', function(e){
            var current_amount = 0;
			e.preventDefault();
			if ( $(this).closest('.input-group').find('.form-control').val() != 0  ) {
                current_amount = parseInt($(this).closest('.input-group').find('.form-control').val()) - 1;
			}

            $(this).closest('.input-group').find('.form-control').val(parseInt(current_amount));
		});
		$('.js-btn-plus').on('click', function(e){
		    var current_amount = parseInt($(this).closest('.input-group').find('.form-control').val()) + 1;
			e.preventDefault();

			$(this).closest('.input-group').find('.form-control').val(current_amount);
		});
	};

	sitePlusMinus();

});

(function($) {

    "use strict";

    var carousel = function() {
        $('.home-slider').owlCarousel({
            loop:true,
            autoplay: true,
            margin:0,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            nav:true,
            dots: true,
            autoplayHoverPause: false,
            items: 1,
            navText : ["<span class='ion-ios-arrow-back'></span>",
                        "<span class='ion-ios-arrow-forward'></span>"],
            responsive:{
              0:{
                items:1
              },
              600:{
                items:1
              },
              1000:{
                items:1
              }
            }
        });
    };

    carousel();

	var siteMenuClone = function() {

		$('body').on('click', '.navbar-toggler', function(e) {
            var $this = $(this);
            var nav = $('#ftco-nav');
			e.preventDefault();

            if ( $this.hasClass('collapsed') ) {
                $this.removeClass('collapsed');
                $this.attr({
                  'aria-expanded' : 'true',
                });
                nav.addClass('show');
            } else {
                $this.addClass('collapsed');
                $this.attr({
                  'aria-expanded' : 'false',
                });
                nav.removeClass('show');
            }
        });

	};

	siteMenuClone();

})(jQuery);