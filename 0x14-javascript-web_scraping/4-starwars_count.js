#!/usr/bin/node
const request = require('request');

const endpoint = process.argv[2];
request(endpoint, (error, _, body) => {
  if (error) return;

  const results = JSON.parse(body).results;
  const count = results.reduce((count, m) => {
    return m.characters.find((c) => c.endsWith('/18/')) ? ++count : count;
  }, 0);
  console.log(count);
});
