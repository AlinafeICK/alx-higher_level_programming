// This script updates the text of the <header> element to "New Header!!!"
// when the user clicks on the <div> with id "update_header".

$(document).ready(function() {
    $('#update_header').click(function() {
      $('header').text('New Header!!!');
    });
  });
  