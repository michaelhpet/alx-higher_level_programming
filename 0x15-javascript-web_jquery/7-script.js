const character = $("div#character");
fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json").then((r) =>
  r.json().then((response) => {
    character.html(response.name);
  })
);
