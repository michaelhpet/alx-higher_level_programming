#!/usr/bin/node
const args = Array.from(process.argv).slice(2);
const message = typeof args[0] === 'undefined' ? 'No argument' : args[0];
console.log(message);
