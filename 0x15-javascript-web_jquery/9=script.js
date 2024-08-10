// This script fetches the French translation of "hello" from the given API
// and displays it inside the <div> with id "hello".

$(function() {
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    });
});
