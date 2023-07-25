#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const endpoint = process.argv[2];
const filename = process.argv[3];
request(endpoint).pipe(fs.createWriteStream(filename));
