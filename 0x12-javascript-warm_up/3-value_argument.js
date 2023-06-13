#!/usr/bin/node
const args = Array.from(process.argv).slice(2);
const message = args?.at(0) ?? 'No argument';
console.log(message);
