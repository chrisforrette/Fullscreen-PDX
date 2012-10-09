/**
 * ProjectName
 * Handles all global behaviors and properties for the site
 *
 * Dependencies:
 * - jQuery
 *
 */

(function($) {

    var Fullscreen = {

        init: function() {
            
            var wrapper = $('.posts'),
                posts = wrapper.find('li'),
                postWidth = posts.first().outerWidth(),
                offOpacity = 0.25;
            
            wrapper.mCustomScrollbar({
                'horizontalScroll': true,
                'scrollInertia': 0,
                'callbacks': {
                    'onScroll': function() {
                        var crop = wrapper.find('.mCustomScrollBox'),
                            cropWidth = crop.width(),
                            maxOffset = cropWidth - postWidth,
                            container = wrapper.find('.mCSB_container'),
                            left = container.position().left;
                        
                        // Store post left offsets if they're not already there
                        
                        if (typeof posts.data('left') != 'number') {
                            posts
                                .each(function(index, el) {
                                    el = $(el);
                                    el.data('left', el.position().left);
                                });
                        }
                        
                        posts
                            .each(function(index, el) {
                                var el = $(el),
                                    offset = left + el.data('left');
                                
                                if (offset >= 0 && offset <= maxOffset) {
                                    var opacity = 1;
                                } else {
                                    if (offset < 0) {
                                        var diff = Math.abs(offset);
                                    } else {
                                        var diff = offset - maxOffset;
                                    }
                                    
                                    if (diff < postWidth) {
                                        var opacity = (offOpacity + ((1 - (diff/postWidth)) * (1 - offOpacity))).toFixed(2);
                                    } else {
                                        var opacity = offOpacity;
                                    }
                                }
                                el.css('opacity', opacity);
                                
                            });
                    }
                }
            });
        }

    };

    window.Fullscreen = Fullscreen;

    $(document).ready(function() {
        Fullscreen.init();
    });

})(jQuery);