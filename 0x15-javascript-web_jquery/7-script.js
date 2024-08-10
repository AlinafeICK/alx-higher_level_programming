// This script fetches the character name from the provided API URL
// and displays it in the <div> with id "character".

$(document).ready(function() {
    // Define the URL to fetch data from
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  
    // Perform the AJAX GET request
    $.get(apiUrl, function(data) {
      // Extract the character name from the response data
      const characterName = data.name;
  
      // Display the character name in the <div> with id "character"
      $('#character').text(characterName);
    });
  });