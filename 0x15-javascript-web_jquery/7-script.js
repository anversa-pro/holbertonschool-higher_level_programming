$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
  $('#character').html(data.name);
});