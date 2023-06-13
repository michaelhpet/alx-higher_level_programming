#!/usr/bin/node
let times = process.argv[2];
if (!times || !Number(times)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < times; i++) console.log('C is fun');
}
