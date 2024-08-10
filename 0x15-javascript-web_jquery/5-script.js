$(document).ready(function() {
    $('#add_item').click(function() {
      // Create a new <li> element with the text "Item"
      const newItem = $('<li>Item</li>');
      // Append the new <li> element to the <ul class="my_list">
      $('ul.my_list').append(newItem);
    });
  });