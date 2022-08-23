
$('#submitcontactform').click(
    function rds () {
    var name=$('#name')[0].value;
    var email=$('#email')[0].value;
    var website=$('#website')[0].value;
    var message=$('#message')[0].value;
    
    //if(!name) alert('Enter name and other details');
    if(name && email && message && website)
        $.ajax({
            url: '/contactform',
            type: 'get',
            data: {
                name:name,
                email:email,
                website:website,
                description: message
            },
            success: function(msg) {
                alert('Request sent');
                $(':input','#contact-page-form')
                  .not(':button, :submit, :reset, :hidden')
                  .val('')
                  .prop('checked', false)
                  .prop('selected', false);
            }
        });
    }
    
    
    );
    
    