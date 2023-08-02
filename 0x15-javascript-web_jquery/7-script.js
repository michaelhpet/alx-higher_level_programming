const character = $('div#character');
$.get(
  'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  (response) => {
    character.html(response.name);
  }
);
