#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(endpoint, (error, response, body) => {
  if (error) console.log(error);
  else if (response.statusCode !== 200) {
    console.log('Error code: ' + response.statusCode);
  } else console.log(JSON.parse(body).title);
});
