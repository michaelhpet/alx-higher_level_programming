#!/usr/bin/node
const request = require('request');

const endpoint = process.argv[2];
request(endpoint, { method: 'GET' }, (error, response, _) => {
  console.log(error ?? `code: ${response.statusCode}`);
});
