#!/usr/bin/node
const args = Array.from(process.argv).slice(2);
const message =
  args.length === 0
    ? 'No argument'
    : args.length === 1
      ? 'Argument found'
      : 'Arguments found';
console.log(message);
