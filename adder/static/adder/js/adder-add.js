$( document ).ready(function() {
    $( ".pseudo-select.competitor .dropdown-list div" ).click(function() {
        var competitor_id = $(this).data('value');
        var competitor_name =  $(this).text();
        var insert_html = "<div class='ep-row no-border competitors-list' data-id='" + competitor_id + "'>";
            insert_html += "<div class='ep-col ep-label'>";
            insert_html += "<label>" + competitor_name + ":</label>";
            insert_html += "</div>";  
            insert_html += "<div class='ep-col ep-data'>";                    
            insert_html += "<input type='text' class='competitor_input' name='competitor[" + competitor_id + "]'  autocomplete='off'>";
            
            insert_html += "<div class='del_competitor'>";
            insert_html += "<i class='fa fa-trash-o'></i>";  
            insert_html += "</div>";
            
            
            insert_html += "</div>";
            insert_html += "</div>";
                
                
        $('.ep-row').last().after(insert_html);
        var del_elem = $('.ep-row .del_competitor').last();
        $(del_elem).click(function() {
            del_competitor_click($(this))
        });
        
        $('.pseudo-select.competitor .ps-button-text').html('');
        $(this).hide();
    });
    
    $('#add_new_import_item .btn-controls .btn-default').click(function() {
        add_new_import_item_clear();   
    });
    $('#add_new_import_item .btn-controls .btn-primary.save_and_new').click(function() {
        save_imported_item_and_add_new();    
    });
    $('#add_new_import_item .btn-controls .btn-primary.save').click(function() {
        save_imported_item_and_add_exit();    
    });
    
    $('.competitors-list .del_competitor').click(function() {
        del_competitor_click($(this))    
    });

});
function add_new_import_item_clear(level) {
    if(level===undefined)
    {
        level='all'    
    }
    
    if(level=='all')
    {   
        $('#add_new_import_item .pseudo-select .ps-button-text').text('');    
        $('#add_new_import_item .competitors-list').remove();
        $('#add_new_import_item #ps-competitor-select .dropdown-list div').show(); 
        $('#add_new_import_item input:not([name="csrfmiddlewaretoken"]):not([name="num_import"])').val('');
    }
    $('#add_new_import_item input:not([name="csrfmiddlewaretoken"]):not([name="num_import"]):not([name="city"]):not([name="category"])').val('');
    $('#add_new_import_item .dropdown-list div').removeClass('element-selected');  
    $('#add_new_import_item input').removeClass('required');
    $('#add_new_import_item .pseudo-select-btn').removeClass('required'); 
    
}

function del_competitor_click(element) {
    var row = $(element).parent().parent();
    var competitor_id = $(row).data('id');
    
    $(row).remove();
    
    $( ".pseudo-select.competitor .dropdown-list div" ).each(function( index ) 
    {
        if($(this).data('value')==competitor_id)
        {
            $(this).show();
        }
    });

    var url = $('.page_params .delete_analog_url').text();
    if(url!==undefined)
    {
        if($(row).hasClass('exist'))
        {
            var csrf_token_val = $('.page_params .csrf_token input[name="csrfmiddlewaretoken"]').val(); 
            $.ajax({
                type: 'POST',
                url: url,
                data: {
                        analog_id: competitor_id,
                        csrfmiddlewaretoken: csrf_token_val,
                    }
            }).done(function(data) {
                if(data=="ok")
                {
                    show_message('', true);    
                }
                else
                {
                    show_message(data, false);     
                }
            }).fail(function() {
                show_message('Удалить не удалось', false);
            });
        }
    } 
    
}

function check_form_required(){
    var required_check=true;
    $( "#add_new_import_item input[required]" ).each(function( index ) 
    {
        if($(this).val()=="")
        {
            $(this).addClass('required')
            required_check=false; 
            if($(this).attr('type')=='hidden')
            {
                var input_name=$(this).attr('name');
                $( "#add_new_import_item .pseudo-select" ).each(function( index ) 
                {
                    if($(this).data('target')==input_name)
                    {
                        $(this).children('.pseudo-select-btn').addClass('required');    
                    }
                });
            }
            
        }
        else
        {
            $(this).removeClass('required');
            if($(this).attr('type')=='hidden')
            {
                var input_name=$(this).attr('name');
                $( "#add_new_import_item .pseudo-select" ).each(function( index ) 
                {
                    if($(this).data('target')==input_name)
                    {
                        $(this).children('.pseudo-select-btn').removeClass('required');    
                    }
                });
            }        
        }
    });
    
    return required_check; 
}

function save_imported_item_and_add_new(){
    var form = $('#add_new_import_item');
    if(!check_form_required()) return;
        
    $.ajax({
        type: $(form).attr('method'),
        url: $(form).attr('action'),
        data: $(form).serialize()
    }).done(function(data) {
        if(data=="ok")
        {
            show_message('', true);    
        }
        else
        {
            show_message(data, false);     
        }
        add_new_import_item_clear('1');
    }).fail(function() {
        show_message('Cохранить не удалось', false);
    });
    
}
function save_imported_item_and_add_exit(){
    var form = $('#add_new_import_item');
    if(!check_form_required()) return;
    
    $.ajax({
        type: $(form).attr('method'),
        url: $(form).attr('action'),
        data: $(form).serialize()
    }).done(function(data) {
        if(data=="ok")
        {
            show_message('', true);
            window.location.href = $('.page_params .back_url').text();   
        }
        else
        {
            show_message(data, false);     
        }
    }).fail(function(data) {
        show_message('Cохранить не удалось', false);
    });
    
}



