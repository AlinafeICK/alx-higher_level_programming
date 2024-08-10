// This script fetches the list of movie titles from the provided API URL
// and displays them as list items in the <ul> with id "list_movies".

$(document).ready(function() {
    // Define the URL to fetch data from
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  
    // Perform the AJAX GET request
    $.get(apiUrl, function(data) {
      // Iterate over each film in the response data
      data.results.forEach(function(film) {
        // Create a new <li> element for each film title
        const listItem = $('<li></li>').text(film.title);
        // Append the new <li> element to the <ul> with id "list_movies"
        $('#list_movies').append(listItem);
      });
    });
  });