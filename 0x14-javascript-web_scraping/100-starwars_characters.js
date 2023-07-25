#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(endpoint, { method: 'GET' }, (error, _, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, i) {
  request(characters[i], { method: 'GET' }, (error, _, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).name);
    if (i < characters.length - 1) printCharacters(characters, ++i);
  });
}
