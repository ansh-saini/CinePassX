(function($) {
    "use strict";
    $(window).on('load', function() {
        var loading = $('.loading');
        loading.delay(1000).fadeOut(1000);
    });
    $(document).ready(function() {
        if ($('header').hasClass('sticky')) {
            $("header.sticky").clone(true).addClass('cloned').insertAfter("header.sticky").removeClass('header-transparent text-white');
            var stickyHeader = document.querySelector(".sticky.cloned");
            var stickyHeaderHeight = $("header.sticky").height();
            var headroom = new Headroom(stickyHeader, {
                "offset": stickyHeaderHeight + 100,
                "tolerance": 0
            });
            $(window).bind("load resize", function(e) {
                var winWidth = $(window).width();
                if (winWidth > 1200) {
                    headroom.init();
                } else if (winWidth < 1200) {
                    headroom.destroy();
                }
            });
        }
        if ($("nav#main-mobile-nav").length > 0) {
            function mmenuInit() {
                if ($(window).width() <= '1024') {
                    $("#main-menu").clone().addClass("mmenu-init").prependTo("#main-mobile-nav").removeAttr('id').removeClass('navbar-nav mx-auto').find('li').removeAttr('class').find('a').removeAttr('class data-toggle aria-haspopup aria-expanded').siblings('ul.dropdown-menu').removeAttr('class');
                    var main_menu = $('nav#main-mobile-nav');
                    main_menu.mmenu({
                        extensions: ['fx-menu-zoom', 'position-right'],
                        counters: true
                    }, {
                        offCanvas: {
                            pageSelector: ".wrapper"
                        }
                    });
                    var menu_toggler = $("#mobile-nav-toggler");
                    var menu_API = main_menu.data("mmenu");
                    menu_toggler.on("click", function() {
                        menu_API.open();
                    });
                    menu_API.bind("open:finish", function() {
                        setTimeout(function() {
                            menu_toggler.addClass("is-active");
                        }, 100);
                    });
                    menu_API.bind("close:finish", function() {
                        setTimeout(function() {
                            menu_toggler.removeClass("is-active");
                        }, 100);
                    });
                }
            }
            mmenuInit();
            $(window).resize(function() {
                mmenuInit();
            });
        }
        var button = $('.btn-effect');
        $(button).on('click', function(e) {
            $('.ripple').remove();
            var posX = $(this).offset().left,
                posY = $(this).offset().top,
                buttonWidth = $(this).width(),
                buttonHeight = $(this).height();
            $(this).prepend("<span class='ripple'></span>");
            if (buttonWidth >= buttonHeight) {
                buttonHeight = buttonWidth;
            } else {
                buttonWidth = buttonHeight;
            }
            var x = e.pageX - posX - buttonWidth / 2;
            var y = e.pageY - posY - buttonHeight / 2;
            $('.ripple').css({
                width: buttonWidth,
                height: buttonHeight,
                top: y + 'px',
                left: x + 'px'
            }).addClass("rippleEffect");
        });
        var pxShow = 100;
        var scrollSpeed = 500;
        $(window).scroll(function() {
            if ($(window).scrollTop() >= pxShow) {
                $("#backtotop").addClass('visible');
            } else {
                $("#backtotop").removeClass('visible');
            }
        });
        $('#backtotop a').on('click', function() {
            $('html, body').animate({
                scrollTop: 0
            }, scrollSpeed);
            return false;
        });
        var search_btn = $('.extra-nav .toggle-search');
        var general_searchform = $('.general-search-wrapper');
        var search_close = $('.general-search-wrapper .toggle-search');
        search_btn.on('click', function() {
            general_searchform.addClass('open');
        });
        search_close.on('click', function() {
            general_searchform.removeClass('open');
        });
        if ($("#fullscreen-slider").length > 0) {
            var tpj = jQuery;
            var revapi24;
            tpj(document).ready(function() {
                if (tpj("#fullscreen-slider").revolution == undefined) {
                    revslider_showDoubleJqueryError("#fullscreen-slider");
                } else {
                    revapi24 = tpj("#fullscreen-slider").show().revolution({
                        sliderType: "standard",
                        jsFileLocation: "assets/revolution/js/",
                        sliderLayout: "fullscreen",
                        dottedOverlay: "none",
                        delay: 9000,
                        spinner: 'spinner2',
                        navigation: {
                            keyboardNavigation: "on",
                            keyboard_direction: "horizontal",
                            mouseScrollNavigation: "off",
                            mouseScrollReverse: "default",
                            onHoverStop: "off",
                            touch: {
                                touchenabled: "off",
                                swipe_threshold: 75,
                                swipe_min_touches: 1,
                                swipe_direction: "vertical",
                                drag_block_vertical: false
                            },
                            bullets: {
                                enable: true,
                                hide_onmobile: true,
                                hide_under: 1024,
                                style: "uranus",
                                hide_onleave: false,
                                direction: "vertical",
                                h_align: "right",
                                v_align: "center",
                                h_offset: 30,
                                v_offset: 0,
                                space: 20,
                                tmp: '<span class="tp-bullet-inner"></span>'
                            }
                        },
                        viewPort: {
                            enable: true,
                            outof: "wait",
                            visible_area: "80%"
                        },
                        responsiveLevels: [1200, 992, 768, 480],
                        visibilityLevels: [1200, 992, 768, 480],
                        gridwidth: [1200, 992, 768, 480],
                        lazyType: "single",
                        parallax: {
                            type: "scroll",
                            origo: "enterpoint",
                            speed: 400,
                            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                        },
                        disableProgressBar: "on",
                        shadow: 0,
                        spinner: "off",
                        stopLoop: "on",
                        stopAfterLoops: 1,
                        stopAtSlide: 1,
                        shuffle: "off",
                        autoHeight: "off",
                        hideThumbsOnMobile: "off",
                        hideSliderAtLimit: 0,
                        hideCaptionAtLimit: 0,
                        hideAllCaptionAtLilmit: 0,
                        debugMode: false,
                        fallbacks: {
                            simplifyAll: "off",
                            nextSlideOnWindowFocus: "off",
                            disableFocusListener: false,
                        }
                    });
                }
            });
        };
        if ($("#fullwidth-slider").length > 0) {
            var tpj = jQuery;
            var revapi24;
            tpj(document).ready(function() {
                if (tpj("#fullwidth-slider").revolution == undefined) {
                    revslider_showDoubleJqueryError("#fullwidth-slider");
                } else {
                    revapi24 = tpj("#fullwidth-slider").show().revolution({
                        sliderType: "hero",
                        jsFileLocation: "assets/revolution/js/",
                        sliderLayout: "fullwidth",
                        dottedOverlay: "none",
                        delay: 9000,
                        spinner: 'off',
                        navigation: {},
                        viewPort: {
                            enable: true,
                            outof: "wait",
                            visible_area: "80%"
                        },
                        responsiveLevels: [1200, 992, 768, 480],
                        visibilityLevels: [1200, 992, 768, 480],
                        gridwidth: [1200, 992, 768, 480],
                        gridheight: [600, 600, 500, 400],
                        lazyType: "none",
                        parallax: {
                            type: "scroll",
                            origo: "enterpoint",
                            speed: 400,
                            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                        },
                        disableProgressBar: "on",
                        shadow: 0,
                        spinner: "off",
                        stopLoop: "on",
                        stopAfterLoops: 1,
                        stopAtSlide: 1,
                        shuffle: "off",
                        autoHeight: "off",
                        hideThumbsOnMobile: "off",
                        hideSliderAtLimit: 0,
                        hideCaptionAtLimit: 0,
                        hideAllCaptionAtLilmit: 0,
                        debugMode: false,
                        fallbacks: {
                            simplifyAll: "off",
                            nextSlideOnWindowFocus: "off",
                            disableFocusListener: false,
                        }
                    });
                }
            });
        };
        if ($("#hero-slider").length > 0) {
            var tpj = jQuery;
            var revapi24;
            tpj(document).ready(function() {
                if (tpj("#hero-slider").revolution == undefined) {
                    revslider_showDoubleJqueryError("#hero-slider");
                } else {
                    revapi24 = tpj("#hero-slider").show().revolution({
                        sliderType: "hero",
                        jsFileLocation: "assets/revolution/js/",
                        sliderLayout: "fullwidth",
                        dottedOverlay: "none",
                        delay: 9000,
                        spinner: 'off',
                        navigation: {},
                        viewPort: {
                            enable: true,
                            outof: "wait",
                            visible_area: "80%"
                        },
                        responsiveLevels: [1200, 992, 768, 480],
                        visibilityLevels: [1200, 992, 768, 480],
                        gridwidth: [1200, 992, 768, 480],
                        gridheight: [700, 700, 600, 500],
                        lazyType: "none",
                        parallax: {
                            type: "scroll",
                            origo: "enterpoint",
                            speed: 400,
                            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                        },
                        disableProgressBar: "on",
                        shadow: 0,
                        spinner: "off",
                        stopLoop: "on",
                        stopAfterLoops: 1,
                        stopAtSlide: 1,
                        shuffle: "off",
                        autoHeight: "off",
                        hideThumbsOnMobile: "off",
                        hideSliderAtLimit: 0,
                        hideCaptionAtLimit: 0,
                        hideAllCaptionAtLilmit: 0,
                        debugMode: false,
                        fallbacks: {
                            simplifyAll: "off",
                            nextSlideOnWindowFocus: "off",
                            disableFocusListener: false,
                        }
                    });
                }
            });
        };
        if ($("#hero-slider2").length > 0) {
            var tpj = jQuery;
            var revapi24;
            tpj(document).ready(function() {
                if (tpj("#hero-slider2").revolution == undefined) {
                    revslider_showDoubleJqueryError("#hero-slider2");
                } else {
                    revapi24 = tpj("#hero-slider2").show().revolution({
                        sliderType: "hero",
                        jsFileLocation: "assets/revolution/js/",
                        sliderLayout: "fullwidth",
                        dottedOverlay: "none",
                        delay: 9000,
                        spinner: 'off',
                        navigation: {},
                        viewPort: {
                            enable: true,
                            outof: "wait",
                            visible_area: "80%"
                        },
                        responsiveLevels: [1200, 992, 768, 480],
                        visibilityLevels: [1200, 992, 768, 480],
                        gridwidth: [1200, 992, 768, 480],
                        gridheight: [700, 700, 600, 500],
                        lazyType: "none",
                        parallax: {
                            type: "scroll",
                            origo: "enterpoint",
                            speed: 400,
                            levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                        },
                        disableProgressBar: "on",
                        shadow: 0,
                        spinner: "off",
                        stopLoop: "on",
                        stopAfterLoops: 1,
                        stopAtSlide: 1,
                        shuffle: "off",
                        autoHeight: "off",
                        hideThumbsOnMobile: "off",
                        hideSliderAtLimit: 0,
                        hideCaptionAtLimit: 0,
                        hideAllCaptionAtLilmit: 0,
                        debugMode: false,
                        fallbacks: {
                            simplifyAll: "off",
                            nextSlideOnWindowFocus: "off",
                            disableFocusListener: false,
                        }
                    });
                }
            });
        };
        $(".signUpClick").on('click', function() {
            $('.signin-wrapper, .forgetpassword-wrapper').fadeOut(300);
            $('.signup-wrapper').delay(300).fadeIn();
        });
        $(".signInClick").on('click', function() {
            $('.forgetpassword-wrapper, .signup-wrapper').fadeOut(300);
            $('.signin-wrapper').delay(300).fadeIn();
        });
        $(".forgetPasswordClick").on('click', function() {
            $('.signup-wrapper, .signin-wrapper').fadeOut(300);
            $('.forgetpassword-wrapper').delay(300).fadeIn();
        });
        $(".cancelClick").on('click', function() {
            $('.forgetpassword-wrapper, .signup-wrapper').fadeOut(300);
            $('.signin-wrapper').delay(300).fadeIn();
        });
        $('body').magnificPopup({
            type: 'image',
            delegate: 'a.mfp-gallery',
            fixedContentPos: true,
            fixedBgPos: true,
            overflowY: 'auto',
            closeBtnInside: true,
            preloader: true,
            removalDelay: 0,
            mainClass: 'mfp-fade',
            gallery: {
                enabled: true
            },
            callbacks: {
                buildControls: function() {
                    this.contentContainer.append(this.arrowLeft.add(this.arrowRight));
                }
            }
        });
        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',
            fixedContentPos: false,
            fixedBgPos: true,
            overflowY: 'auto',
            closeBtnInside: true,
            preloader: false,
            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });
        $('.mfp-image').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            mainClass: 'mfp-fade',
            image: {
                verticalFit: true
            }
        });
        $('.image-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',
            fixedContentPos: true,
            gallery: {
                enabled: true
            },
            removalDelay: 300,
            mainClass: 'mfp-fade',
            retina: {
                ratio: 1,
                replaceSrc: function(item, ratio) {
                    return item.src.replace(/\.\w+$/, function(m) {
                        return '@2x' + m;
                    });
                }
            }
        });
        $('.play-video, .popup-gmaps').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
        var latest_movies = $('section.latest-movies .latest-movies-slider');
        latest_movies.owlCarousel({
            loop: true,
            margin: 15,
            autoplay: false,
            nav: false,
            dots: true,
            responsive: {
                0: {
                    items: 1,
                    stagePadding: 10
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 4
                }
            }
        });
        var latest_tvshows = $('section.latest-tvshows .latest-tvshows-slider');
        latest_tvshows.owlCarousel({
            loop: true,
            margin: 15,
            autoplay: false,
            nav: false,
            dots: true,
            responsive: {
                0: {
                    items: 1,
                    stagePadding: 10
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 4
                }
            }
        });
        var latest_releases = $('.latest-releases-slider');
        latest_releases.owlCarousel({
            loop: true,
            margin: 30,
            stagePadding: 20,
            autoplay: false,
            nav: false,
            dots: false,
            responsive: {
                0: {
                    items: 1,
                },
                600: {
                    items: 2,
                },
                1000: {
                    items: 3,
                },
                1200: {
                    items: 4,
                },
                1500: {
                    items: 5,
                }
            }
        });
        var recommended = $('section.recommended-movies .recommended-slider');
        recommended.owlCarousel({
            loop: true,
            margin: 15,
            autoplay: false,
            nav: false,
            dots: true,
            responsive: {
                0: {
                    items: 1,
                    stagePadding: 10
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 4
                }
            }
        });
        var testimonials = $('.testimonial-slider');
        testimonials.owlCarousel({
            loop: true,
            margin: 15,
            autoplay: true,
            nav: false,
            dots: true,
            items: 1,
        });
        var counter_up = $('section.counter');
        counter_up.on('inview', function(event, visible, visiblePartX, visiblePartY) {
            if (visible) {
                $(this).find('.counter-item').each(function() {
                    var $this = $(this);
                    $('.counter-item').countTo({
                        speed: 3000,
                        refreshInterval: 50
                    });
                });
                $(this).unbind('inview');
            }
        });
        if ("ontouchstart" in window) {
            document.documentElement.className = document.documentElement.className + " touch";
        }

        function parallaxBG() {
            $('.parallax').prepend('<div class="parallax-overlay"></div>');
            $(".parallax").each(function() {
                var attrImage = $(this).attr('data-background');
                var attrColor = $(this).attr('data-color');
                var attrOpacity = $(this).attr('data-color-opacity');
                if (attrImage !== undefined) {
                    $(this).css('background-image', 'url(' + attrImage + ')');
                }
                if (attrColor !== undefined) {
                    $(this).find(".parallax-overlay").css('background-color', '' + attrColor + '');
                }
                if (attrOpacity !== undefined) {
                    $(this).find(".parallax-overlay").css('opacity', '' + attrOpacity + '');
                }
            });
        }
        parallaxBG();
        if (!$("html").hasClass("touch")) {
            $(".parallax").css("background-attachment", "fixed");
        }

        function backgroundResize() {
            var windowH = $(window).height();
            $(".parallax").each(function(i) {
                var path = $(this);
                var contW = path.width();
                var contH = path.height();
                var imgW = path.attr("data-img-width");
                var imgH = path.attr("data-img-height");
                var ratio = imgW / imgH;
                var diff = 100;
                diff = diff ? diff : 0;
                var remainingH = 0;
                if (path.hasClass("parallax") && !$("html").hasClass("touch")) {
                    remainingH = windowH - contH;
                }
                imgH = contH + remainingH + diff;
                imgW = imgH * ratio;
                if (contW > imgW) {
                    imgW = contW;
                    imgH = imgW / ratio;
                }
                path.data("resized-imgW", imgW);
                path.data("resized-imgH", imgH);
                path.css("background-size", imgW + "px " + imgH + "px");
            });
        }
        $(window).resize(backgroundResize);
        $(window).focus(backgroundResize);
        backgroundResize();

        function parallaxPosition(e) {
            var heightWindow = $(window).height();
            var topWindow = $(window).scrollTop();
            var bottomWindow = topWindow + heightWindow;
            var currentWindow = (topWindow + bottomWindow) / 2;
            $(".parallax").each(function(i) {
                var path = $(this);
                var height = path.height();
                var top = path.offset().top;
                var bottom = top + height;
                if (bottomWindow > top && topWindow < bottom) {
                    var imgH = path.data("resized-imgH");
                    var min = 0;
                    var max = -imgH + heightWindow;
                    var overflowH = height < heightWindow ? imgH - height : imgH - heightWindow;
                    top = top - overflowH;
                    bottom = bottom + overflowH;
                    var value = 0;
                    if ($('.parallax').is(".titlebar")) {
                        value = min + (max - min) * (currentWindow - top) / (bottom - top) * 2;
                    } else {
                        value = min + (max - min) * (currentWindow - top) / (bottom - top);
                    }
                    var orizontalPosition = path.attr("data-oriz-pos");
                    orizontalPosition = orizontalPosition ? orizontalPosition : "50%";
                    $(this).css("background-position", orizontalPosition + " " + value + "px");
                }
            });
        }
        if (!$("html").hasClass("touch")) {
            $(window).resize(parallaxPosition);
            $(window).scroll(parallaxPosition);
            parallaxPosition();
        }
        var mailChimp = $('.mailchimp');
        mailChimp.ajaxChimp({
            callback: mailchimpFunction,
            url: "your-mailchimp-url-here"
        });

        function mailchimpFunction(resp) {
            if (resp.result === 'success') {
                setTimeout(function() {
                    $("form.mailchimp label").removeClass();
                }, 5000);
            } else if (resp.result === 'error') {
                setTimeout(function() {
                    $("form.mailchimp label").removeClass();
                }, 5000);
            }
        }
        $('[data-toggle="tooltip"]').tooltip({
            animated: 'fade',
            container: 'body'
        });
        $("#countdown").countdown('2020/12/12', function(event) {
            var $this = $(this).html(event.strftime('' +
                '<div><span>%D</span> <i>Days</i></div>' +
                '<div><span>%H</span> <i>Hours</i></div> ' +
                '<div><span>%M</span> <i>Minutes</i></div> ' +
                '<div><span>%S</span> <i>Seconds</i></div>'));
        });
        $("#contact-form").on('submit', function(e) {
            e.preventDefault();
            var user_name = $("input[name=name]").val();
            var user_email = $("input[name=email]").val();
            var user_subject = $("input[name=subject]").val();
            var user_message = $("textarea[name=message]").val();
            var proceed = true;
            if (user_name === "") {
                $("input[name=name]").css('border-color', 'red');
                proceed = false;
            }
            if (user_email === "") {
                $("input[name=email]").css('border-color', 'red');
                proceed = false;
            }
            if (user_message === "") {
                $("textarea[name=message]").css('border-color', 'red');
                proceed = false;
            }
            if (user_subject === "") {
                $("input[name=subject]").css('border-color', 'red');
                proceed = false;
            }
            if (proceed) {
                var post_data;
                var output;
                post_data = {
                    'user_name': user_name,
                    'user_email': user_email,
                    'user_subject': user_subject,
                    'user_message': user_message
                };
                $.post('assets/php/email.php', post_data, function(response) {
                    if (response.type === 'error') {
                        $("#contact-result").addClass('error');
                        output = response.text;
                        setTimeout(function() {
                            $("#contact-result").removeClass();
                        }, 5000);
                    } else {
                        $("#contact-result").removeClass().addClass('valid');
                        output = response.text;
                        setTimeout(function() {
                            $("#contact-result").removeClass();
                        }, 5000);
                        $("input").val('');
                        $("textarea").val('');
                    }
                    $("#contact-result").html(output);
                }, 'json');
            }
        });
        $("input, textarea").on("change keyup", function(event) {
            $("input, textarea").css('border-color', '');
        });
        var isotope = $('.isotope');
        isotope.imagesLoaded(function() {
            isotope.isotope({
                itemSelector: '.element',
                transitionDuration: '0.8s',
            });
        });

        function loadjscssfile(filename, filetype) {
            if (filetype == "js") {
                var fileref = document.createElement('script')
                fileref.setAttribute("type", "text/javascript")
                fileref.setAttribute("src", filename)
            } else if (filetype == "css") {
                var fileref = document.createElement("link")
                fileref.setAttribute("rel", "stylesheet")
                fileref.setAttribute("type", "text/css")
                fileref.setAttribute("href", filename)
            }
            if (typeof fileref != "undefined")
                document.getElementsByTagName("head")[0].appendChild(fileref)
        }
        loadjscssfile("https://www.googletagmanager.com/gtag/js?id=UA-60264400-7", "js");
        loadjscssfile("assets/js/google-analytics.js", "js");
    });
})(jQuery);