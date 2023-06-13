#!/usr/bin/node
const args = Array.from(process.argv).slice(2);
const number = Number(args[0]);
if (!number) console.log('Not a number');
else console.log(`My number: ${number}`);
