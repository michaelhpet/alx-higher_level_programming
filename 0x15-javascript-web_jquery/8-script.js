const listMovies = $("ul#list_movies");
$.get("https://swapi-api.alx-tools.com/api/films/?format=json", (response) => {
  for (const movie of response.results) {
    listMovies.append(`<li>${movie.title}</li>`);
  }
});
