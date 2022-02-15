$.get('https://swapi-api.hbtn.io/api/films/?format=json', (body, textStatus) => {
    if (textStatus === 'success') {
      const movies = body.results;
      movies.forEach(movie => {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });