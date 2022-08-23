
$('form.whitepaper').submit(processForm); // listen to each form’s submit

function processForm(e) {
 e.preventDefault();
 console.log(e.target.id)
    var firstname=$('#'.concat(e.target.id)).find('#firstname')[0].value
    var lastname=$('#'.concat(e.target.id)).find('#lastname')[0].value
    var email=$('#'.concat(e.target.id)).find('#email')[0].value
    var company=$('#'.concat(e.target.id)).find('#company')[0].value
    var jobtitle=$('#'.concat(e.target.id)).find('#jobtitle')[0].value
    var Country=$('#'.concat(e.target.id)).find('#Country')[0].value
    var Industry=$('#'.concat(e.target.id)).find('#Industry')[0].value
    var Intrests=$('#'.concat(e.target.id)).find('#Intrests')[0].value


    e.preventDefault(); // prevents default submit action
    $.ajax( {
        type: 'GET',
        url: 'paperfrom',
        data: {
            id:e.target.id,
            firstname:firstname,
            lastname:lastname,
            email:email,
            company:company,
            jobtitle:jobtitle,
            country:Country,
            Industry:Industry,
            Intrests:Intrests,

        },
        success: function(data) {
            console.log('button.'.concat(e.target.id))
         $('button.'.concat(e.target.id)).trigger('click')
         $(':input','#'.concat(e.target.id))
                  .not(':button, :submit, :reset, :hidden')
                  .val('')
                  .prop('checked', false)
                  .prop('selected', false);
         alert("hi")
        }
    } );


}