#!/usr/bin/node
const fs = require('fs');

const filename = process.argv[2];
fs.readFile(filename, { encoding: 'utf-8' }, function (err, data) {
  console.log(err ?? data);
});
