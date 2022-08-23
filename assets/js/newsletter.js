
$('#newsletterform').submit(pForm); // listen to each form’s submit

function pForm(e) {
 e.preventDefault();
 console.log(e.target.id)
   
    var email=$('#'.concat(e.target.id)).find('#email')[0].value
    


    e.preventDefault(); // prevents default submit action
    $.ajax( {
        type: 'GET',
        url: 'newsletterform',
        data: {
           
            email:email,
           

        },
        success: function(data) {
       
         $(':input','#'.concat(e.target.id))
                  .not(':button, :submit, :reset, :hidden')
                  .val('')
                  .prop('checked', false)
                  .prop('selected', false);
         alert("Request Sent")
        }
    } );


}

