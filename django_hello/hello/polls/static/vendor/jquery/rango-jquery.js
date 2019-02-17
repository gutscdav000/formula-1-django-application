$(document).ready(function() {

    // redirect when table row is clicked
   $(".jq-redirect").on('click', function() {
     var url = $(this).data("id");
     location.href = '/polls/' + url
   } );


   //modal functions
   $(".js-open-modal").click(function(){
     var modal = $('.modal');
     modal.modal('toggle');
     modal.show();
 });

 $(".js-close-modal").click(function(){
   var modal = $('.modal');
   modal.modal('toggle');
   modal.hide();
 });

 //if you click on anything except the modal itself or the "open modal" link, close the modal
 $(document).click(function(event) {
   if (!$(event.target).closest(".modal,.js-open-modal").length) {
     var modal = $("body").find(".modal");
     modal.modal('toggle');
     modal.hide();
   }
 });


 // populate form with row attributes & show modal
  $('tr').on('click', function() {
    var promise = getTableHeaders($('#request_path').val());
    var headerArr;
    var formElement;
    //console.log(promise);


    // remove previous content
    $('.dynamic-form').remove();

    // put td's in text array
    var rowId = $(this).data('row');
    var rowText = $('tr[data-row=' + rowId + ']').text();
    var textArr = rowText.trim().split('\n');
    textArr.splice($.inArray("Open Popup", textArr), 1);
    textArr.splice($.inArray("", textArr), 1);

    // load modal form once ajax call completes
    promise.then(function() {
      headerArr = promise.responseJSON.message;
      $(promise.responseJSON.message).each(function(i){
        console.log('head: ' + i +'\t' + promise.responseJSON.message[i]);
       });


       formElement = '<div class="dynamic-form"><div class="row">';
       $(textArr).each(function(i) {

         formElement += '<div class="column">'
         textArr[i] = $.trim(textArr[i]);
         console.log(i + ': ' + textArr[i]);

         formElement += headerArr[i] + ':\t';
         formElement += '<input type="text" name="'+ i +'"value="' + textArr[i] + '">\n</div>\n';
       });

       formElement += '<input type="hidden" name="headList" id="headList" value="'+ promise.responseJSON.message +'">';
       formElement += '<input type="submit">\n</div></div>';

       var modal = $('.modal');
       modal.find('form').append(formElement);
    });

  });


});

// function grabs table headers to populate modal window field with labels
function getTableHeaders(request_path) {
  console.log(request_path);
  return $.ajax({
    type : "GET",
    url : "/polls/get_table_headers/",
    dataType : "json",
    async : "true",
    data : { csrfmiddlewaretoken : '{{csrf_token}}', path : request_path },
  });
}
