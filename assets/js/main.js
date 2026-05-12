(function ($) {
    "use strict";

    // Buy Now Btn
    // $('body').append("<a href='#' class='buy-now-btn' target='_blank'><img src='assets/img/envato.png' alt='envato'/>Buy Now</a>"); 
    
    //Preloader
    $(window).on('load', function (event) {
        $('.js-preloader').delay(500).fadeOut(500);
    });
    
    //Open Search Box
    $('.searchbtn').on('click', function() {
        $('.search-area').toggleClass('open');
    });
    $('.close-searchbox').on('click', function() {
        $('.search-area').removeClass('open');
    });

    // Language Dropdown
    $(".language-option").each(function () {
        var each = $(this)
        each.find(".lang-name").html(each.find(".language-dropdown-menu a:nth-child(1)").text());
        var allOptions = $(".language-dropdown-menu").children('a');
        each.find(".language-dropdown-menu").on("click", "a", function () {
            allOptions.removeClass('selected');
            $(this).addClass('selected');
            $(this).closest(".language-option").find(".lang-name").html($(this).text());
        });
    })
    
      //Counter
      $(".odometer").appear(function (e) {
        var odo = $(".odometer");
        odo.each(function () {
            var countNumber = $(this).attr("data-count");
            $(this).html(countNumber);
        });
    });
    
    //Progressbar
    $(window).scroll(function () {
        // if ($(window).scrollTop() > 100) { // scroll down abit and get the action   
        $('.progress-bar').each(function () {
            $(this).find('.progress-content').animate({
                width: $(this).attr('data-percentage')
            }, 2000);

            $(this).find('.progress-number-mark').animate({ left: $(this).attr('data-percentage') }, {
                duration: 2000,
                step: function (now, fx) {
                    var data = Math.round(now);
                    $(this).find('.percent').html(data + '%');
                }
            });
        });
        // }
    });

    // Progressbar Animation on Scroll
    if ($('.skills').length) {
        var offsetTop = $('.skills').offset().top;
        $(window).scroll(function() {
            var height = $(window).height();
            if ($(window).scrollTop() + height > offsetTop) {
                $('.skillbar').each(function() {
                    $(this).find('.skillbar-bar').animate({
                        width: $(this).attr('data-percent')
                    }, 1500);
                });
            }
        });
    }

    //Tweenmax js
    $('.hero-wrap').mousemove(function (e) {
        var wx = $(window).width();
        var wy = $(window).height();
        var x = e.pageX - this.offsetLeft;
        var y = e.pageY - this.offsetTop;
        var newx = x - wx / 2;
        var newy = y - wy / 2;
        $('.hero-content').each(function () {
            var speed = $(this).attr('data-speed');
            if ($(this).attr('data-revert')) speed *= -.4;
            TweenMax.to($(this), 1, { x: (1 - newx * speed), y: (1 - newy * speed) });
        });
    });
    
    //Hero Slider
    $(".hero-slider-one").owlCarousel({
        nav: true,
        dots: true,
        loop: true,
        margin: 20,
        items: 1,
        animateOut: 'fadeOut',
        thumbs: false,
        smartSpeed: 1300,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        navText: ['<i class="ri-arrow-left-s-line"></i>', '<i class="ri-arrow-right-s-line"></i>'],
        responsiveClass: true,
        autoHeight: true,
    });

    // Prevent utility anchors from exposing template URLs or jumping unexpectedly.
    $('a[href="#"].back-to-top, .menu-close a[href="#"], .mobile-menu a[href="#"]').on('click', function(e) {
        e.preventDefault();
    });

    // Lightweight YouTube preview: click swaps thumbnail card for an iframe embed.
    $('.js-video-preview').on('click', function(e) {
        e.preventDefault();
        var wrap = $(this);
        var src = wrap.data('video-src');
        var title = wrap.data('video-title') || 'Africa Climate Finance video';
        if (!src) return;
        wrap.html('<iframe src="' + src + '" title="' + title + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>');
        wrap.addClass('is-playing');
    });

    // Home ESG tabs.
    $('.home-sdg-tab').on('click', function() {
        var tab = $(this);
        $('.home-sdg-tab').removeClass('active').attr('aria-selected', 'false');
        tab.addClass('active').attr('aria-selected', 'true');
        $('.home-sdg-panel').removeClass('active');
        $('#' + tab.attr('aria-controls')).addClass('active');
    });

    // About page section tabs smooth scroll.
    $('.ds-impact-nav a[href^="#"]').on('click', function(e) {
        var target = $($(this).attr('href'));
        if (!target.length) return;
        e.preventDefault();
        $('.ds-impact-nav .ds-pill').removeClass('active');
        $(this).addClass('active');
        $('html, body').animate({ scrollTop: target.offset().top - 90 }, 500);
    });

    //Testimonial Slider 
    $(".testimonial-slider-one").owlCarousel({
        nav: true,
        dots: false,
        loop: true,
        navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
        margin: 25,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 3,
            }
        }
    });

    //Project Slider 
    $(".project-slider-one").owlCarousel({
        nav: true,
        dots: true,
        loop: true,
        navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
        margin: 25,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 3,
            }
        }
    });
    $(".project-slider-two").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 25,
        items: 1,
        center:true,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1.06,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 3.3,
            },
            1400: {
                items: 4.3,
            }
        }
    });
    $(".project-slider-three").owlCarousel({
        nav: true,
        dots: true,
        loop: true,
        margin: 25,
        navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 1,
            },
            992: {
                items: 1,
            },
            1200: {
                items: 2,
            }
        }
    });

    //Team Slider 
    $(".team-slider-one").owlCarousel({
        nav: true,
        dots: true,
        loop: true,
        navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
        margin: 25,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 4,
            }
        }
    });
    $(".team-slider-two").owlCarousel({
        nav: true,
        dots: true,
        loop: true,
        navText: ['<i class="flaticon-left-arrow"></i>', '<i class="flaticon-right-arrow"></i>'],
        margin: 25,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: false,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: {
                items: 1,
            },
            768: {
                items: 2,
            },
            1200: {
                items: 3,
            }
        }
    });

    //Blog Slider (Partners) - autoplay, no nav arrows
    $(".blog-slider-one").owlCarousel({
        nav: false,
        dots: true,
        loop: true,
        margin: 25,
        items: 1,
        thumbs: false,
        smartSpeed: 1300,
        autoplay: true,
        autoplayTimeout: 3500,
        autoplayHoverPause: false,
        responsiveClass: true,
        autoHeight: true,
        responsive: {
            0: { items: 1 },
            768: { items: 2 },
            1200: { items: 3 }
        }
    });

    //sticky Header
    var wind = $(window);
    var sticky = $('.header-wrap');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

    // Responsive mmenu
    $(window).on('resize', function() {
        if($(window).width() <= 1199) {
            $('.collapse.navbar-collapse').removeClass('collapse');
        }else{
            $('.navbar-collapse').addClass('collapse');
        }
    });
    $('.mobile-menu a').on('click', function() {
        $('.main-menu-wrap').addClass('open');
        $('.collapse.navbar-collapse').removeClass('collapse');
    });

    $('.mobile_menu a').on('click', function () {
        $(this).parent().toggleClass('open');
        $('.main-menu-wrap').toggleClass('open');
    });

    $('.menu-close').on('click', function () {
        $('.main-menu-wrap').removeClass('open')
    });
    $('.mobile-top-bar').on('click', function () {
        $('.header-top').addClass('open')
    });
    $('.close-header-top button').on('click', function () {
        $('.header-top').removeClass('open')
    });
    var $offcanvasNav = $('.navbar-nav'),
    $offcanvasNavSubMenu = $offcanvasNav.find('.dropdown-menu');
    $offcanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="ri-arrow-down-s-line"></i></span>');
    $offcanvasNavSubMenu.slideUp();
    $offcanvasNav.on('click', 'li a, li .menu-expand', function (e) {
        var $this = $(this);
        if (($this.attr('href') === '#' || $this.hasClass('menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.siblings('ul').slideUp('slow');
            } else {
                $this.closest('li').siblings('li').find('ul:visible').slideUp('slow');
                $this.siblings('ul').slideDown('slow');
            }
        }
        if ($this.is('a') || $this.is('span') || $this.attr('class').match(/\b(menu-expand)\b/)) {
            $this.parent().toggleClass('menu-open');
        } else if ($this.is('li') && $this.attr('class').match(/\b('dropdown-menu')\b/)) {
            $this.toggleClass('menu-open');
        }
    });

    // Scroll animation
    AOS.init();

    //Back To top
    function BackToTop() {
        $('.back-to-top').on('click', function () {
            $('html, body').animate({
                scrollTop: 0
            }, 100);
            return false;
        });

        $(document).scroll(function () {
            var y = $(this).scrollTop();
            if (y > 600) {
                $('.back-to-top').fadeIn();
                $('.back-to-top').addClass('open');
            } else {
                $('.back-to-top').fadeOut();
                $('.back-to-top').removeClass('open');
            }
        });
    }
    BackToTop();

})(jQuery);

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('clim_theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('clim_theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('clim_theme') === 'theme-dark') {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    } else {
        setTheme('theme-light');
        document.getElementById('slider').checked = true;
    }
})();