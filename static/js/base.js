function show_message(msg, succsess, caption, delay)
{
    if(succsess===undefined) succsess=true;
    if(delay===undefined) delay=5000;
    if(caption===undefined) 
    {
        if(succsess)
        {
            caption="Success!";    
        }
        else
        {
            caption="Fail!";    
        }
    }
    
    var message_class='alert-success';
    if(!succsess) var message_class='alert-danger';
        
    
    var $message =  $("<div class='alert " + message_class + " alert-dismissable'>\
                      <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>\
                      <strong>" + caption + "</strong> " + msg + "\
                    </div>");
    
    $( ".messages-wrapper" ).append( $message );

    if(delay>0)
    {
        setTimeout(function() {
            $($message).remove();
        }, delay);
    }
}


$( document ).ready(function() {
    //LEFT SIDEBAR OPENER
    $('.left-sidebar .ls-opener').click(function(){
        $('.left-sidebar').toggleClass('minimized');    
        $('.content-page').toggleClass('fullscreen');   
    });
    
    
    //ѕсевдо—елект
    $( ".pseudo-select-btn" ).click(function() {
        var opened = $(this).children('.ps-button-text').hasClass('up');

        $('.dropdown-list').addClass('dropdown-hidden');
        $('.dropdown-list').removeClass('opened');
        $('.ps-button-text').removeClass('up');
        
        if(!opened) 
        {
            $(this).children('.ps-button-text').addClass('up');
            $(this).next('.dropdown-list').removeClass('dropdown-hidden');
            var this_dl = $(this).next('.dropdown-list');
            setTimeout(function() {
                $(this_dl).addClass('opened');
            }, 200);
        }
    });
    
    $('html').click(function(event) {
        if( !$(event.target).hasClass('button-dropdown') && !$(event.target).hasClass('ps-button-text') )
        {
            $( ".dropdown-list" ).addClass('dropdown-hidden');
            $('.pseudo-select-btn .ps-button-text').removeClass('up');
            $('.dropdown-list').removeClass('opened');
        }
    });
    
    $( ".pseudo-select .dropdown-list div" ).click(function() {
        
        
        var elemId = $(this).data('value');
        var ps_element = $(this).closest('.pseudo-select');
        var dropdown_element = $(ps_element).children('.dropdown-list');
        var pstext_element = $(ps_element).children('.pseudo-select-btn').children('.ps-button-text');
                
        
        var selected_text = $(pstext_element).html();
        var new_text =  $(this).text();
        var targetName = $(ps_element).data('target');
               
        $(dropdown_element).toggleClass('dropdown-hidden');
        $(dropdown_element).find('div').removeClass('element-selected');
        
        $(pstext_element).html(new_text);
        $(pstext_element).attr('data-value', elemId);

        
        $(this).addClass('element-selected');
        
        $(pstext_element).removeClass('up');
        
        $("input[name='"+ targetName +"']").val(elemId);  
    });
    
    
    
    
    
});