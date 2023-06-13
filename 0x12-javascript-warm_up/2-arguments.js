#!/usr/bin/node
const arguments = process.argv.slice(2);
const message =
  arguments.length === 0
    ? 'No argument'
    : arguments.length === 1
    ? 'Argument found'
    : 'Arguments found';
console.log(message);
