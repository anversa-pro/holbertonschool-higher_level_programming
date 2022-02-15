 
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (body, textStatus) => {
  if (textStatus === 'success') {
    $('#character').html(body.name);
  }
})