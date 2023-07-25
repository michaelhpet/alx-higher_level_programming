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
  for (const endpoint of characters) {
    request(endpoint, { method: 'GET' }, (error, _, body) => {
      if (error) console.log(error);
      console.log(JSON.parse(body).name);
    });
  }
});
