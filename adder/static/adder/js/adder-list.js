$( document ).ready(function() {
    $('.import-list-table .td_comment input').focusout(function() {
        save_import_row_comment($(this).data('id'), $(this).val());    
    });

});


function save_import_row_comment(row_id, comment_text){
    var save_url = $('.page_params .comment_save_url').text();  
    var csrf_token_val = $('.page_params .csrf_token input[name="csrfmiddlewaretoken"]').val(); 
    $.ajax({
        type: 'POST',
        url: save_url,
        data: {
                comment: comment_text,
                id: row_id,
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
        show_message('Cохранить не удалось', false);
    });
    
}



