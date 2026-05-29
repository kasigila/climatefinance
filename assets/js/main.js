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

    // Responsive mmenu — delegated so dynamically loaded header works
    $(window).on('resize', function() {
        if($(window).width() <= 1199) {
            $('.collapse.navbar-collapse').removeClass('collapse');
        }else{
            $('.navbar-collapse').addClass('collapse');
        }
    });
    $(document).on('click', '.mobile-menu a', function() {
        $('.main-menu-wrap').addClass('open');
        $('.collapse.navbar-collapse').removeClass('collapse');
    });

    $('.mobile_menu a').on('click', function () {
        $(this).parent().toggleClass('open');
        $('.main-menu-wrap').toggleClass('open');
    });

    $(document).on('click', '.menu-close a, .menu-close', function () {
        $('.main-menu-wrap').removeClass('open')
    });
    function bindOffcanvasNav() {
      var $nav = $('.navbar-nav');
      if (!$nav.length || $nav.data('offcanvas-bound')) return;
      $nav.data('offcanvas-bound', true);

      if ($(window).width() <= 991 && $nav.find('.has-dropdown').length) {
        return;
      }

      var $sub = $nav.find('.dropdown-menu');
      $sub.parent().each(function() {
        if (!$(this).children('.menu-expand').length && !$(this).hasClass('has-dropdown')) {
          $(this).prepend('<span class="menu-expand"><i class="ri-arrow-down-s-line"></i></span>');
        }
      });
      $sub.slideUp();
      $nav.off('click.offcanvas').on('click.offcanvas', 'li a, li .menu-expand', function (e) {
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
        if ($this.is('a') || $this.is('span') || ($this.attr('class') || '').match(/\b(menu-expand)\b/)) {
            $this.parent().toggleClass('menu-open');
        } else if ($this.is('li') && ($this.attr('class') || '').match(/\b('dropdown-menu')\b/)) {
            $this.toggleClass('menu-open');
        }
    });
    }
    bindOffcanvasNav();
    document.addEventListener('headerLoaded', bindOffcanvasNav);

    // Mobile submenu: chevron toggles only; parent link navigates
    function bindMobileSubmenus() {
      var $nav = $('.navbar-nav');
      if (!$nav.length) return;

      $nav.find('.has-dropdown > .dropdown-menu').each(function() {
        if ($(window).width() <= 991 && !$(this).data('mobile-init')) {
          $(this).hide().data('mobile-init', true);
        }
      });

      if ($nav.data('mobile-submenu-bound')) return;
      $nav.data('mobile-submenu-bound', true);

      $nav.on('click.mobileSubmenu', '.nav-submenu-toggle', function(e) {
        if ($(window).width() > 991) return;
        e.preventDefault();
        e.stopPropagation();
        var $item = $(this).closest('.has-dropdown');
        var $menu = $item.children('.dropdown-menu');
        var isOpen = $item.hasClass('menu-open');
        $nav.find('.has-dropdown').not($item).removeClass('menu-open').children('.dropdown-menu').slideUp(200);
        $nav.find('.nav-submenu-toggle').not(this).attr('aria-expanded', 'false');
        if (isOpen) {
          $item.removeClass('menu-open');
          $menu.slideUp(200);
          $(this).attr('aria-expanded', 'false');
        } else {
          $item.addClass('menu-open');
          $menu.slideDown(200);
          $(this).attr('aria-expanded', 'true');
        }
      });
    }
    bindMobileSubmenus();
    document.addEventListener('headerLoaded', bindMobileSubmenus);
    $(window).on('resize', function() {
      if ($(window).width() <= 991) bindMobileSubmenus();
    });

    // Entire service/impact cards tappable on mobile
    function bindMobileCardTap() {
      if ($(window).width() > 767) return;
      $('.ds-card, .ds-service-icon-card').each(function() {
        var $card = $(this);
        if ($card.data('tap-bound')) return;
        var $link = $card.find('h3 a, .link, .ds-card-title a').first();
        if (!$link.length) return;
        $card.data('tap-bound', true).addClass('is-tappable').on('click', function(e) {
          if ($(e.target).closest('a').length) return;
          window.location.href = $link.attr('href');
        });
      });
    }
    bindMobileCardTap();
    $(window).on('resize', bindMobileCardTap);

    // COP global forums — show more photos on mobile
    $(document).on('click', '.cop-show-more-btn', function() {
      var $btn = $(this);
      var $gallery = $($btn.data('target'));
      var expanded = $gallery.toggleClass('is-expanded').hasClass('is-expanded');
      $btn.text(expanded ? 'Show Fewer Photos' : 'Show More Photos').attr('aria-expanded', expanded ? 'true' : 'false');
    });

    // Donation page — scroll to partnership form
    $(document).on('click', '.donation-cta-scroll', function(e) {
      var $target = $('#donation-form');
      if (!$target.length) return;
      e.preventDefault();
      $('html, body').animate({ scrollTop: $target.offset().top - 80 }, 500);
    });

    // Homepage — show/hide extra service cards on mobile
    $(document).on('click', '#home-services-toggle', function() {
      var $btn = $(this);
      var $grid = $('#home-services-grid');
      var expanded = $grid.toggleClass('is-expanded').hasClass('is-expanded');
      $btn.text(expanded ? 'Show Fewer Services' : 'Show All Services').attr('aria-expanded', expanded ? 'true' : 'false');
    });

    // Scroll reveal (IntersectionObserver)
    (function initReveal() {
        if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            document.querySelectorAll('.reveal').forEach(function(el) { el.classList.add('visible'); });
            return;
        }
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        document.querySelectorAll('.reveal').forEach(function(el) { observer.observe(el); });
    })();

    // Animated stat counters
    (function initStatCounters() {
        var stats = document.querySelectorAll('.ds-stat-dark .num[data-count]');
        if (!stats.length) return;
        function animate(el) {
            if (el.dataset.animated) return;
            el.dataset.animated = '1';
            var target = parseFloat(el.getAttribute('data-count') || '0');
            var prefix = el.getAttribute('data-prefix') || '';
            var suffix = el.getAttribute('data-suffix') || '';
            var isFloat = String(target).indexOf('.') > -1 || el.getAttribute('data-count').indexOf('.') > -1;
            var start = performance.now();
            var duration = 1500;
            function frame(now) {
                var p = Math.min((now - start) / duration, 1);
                var eased = 1 - Math.pow(1 - p, 3);
                var value = target * eased;
                el.textContent = prefix + (isFloat ? value.toFixed(1) : Math.round(value)) + suffix;
                if (p < 1) requestAnimationFrame(frame);
            }
            requestAnimationFrame(frame);
        }
        if (!('IntersectionObserver' in window)) {
            stats.forEach(animate);
            return;
        }
        var obs = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    animate(entry.target);
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });
        stats.forEach(function(el) { obs.observe(el); });
    })();

    // Scroll animation
    if (typeof AOS !== 'undefined') AOS.init();

    //Back To top
    function BackToTop() {
        $('.back-to-top').on('click', function (e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: 0
            }, 100);
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
    var slider = document.getElementById('slider');
    if (localStorage.getItem('clim_theme') === 'theme-dark') {
        setTheme('theme-dark');
        if (slider) slider.checked = false;
    } else {
        setTheme('theme-light');
        if (slider) slider.checked = true;
    }
})();