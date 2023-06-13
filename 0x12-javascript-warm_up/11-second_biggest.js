#!/usr/bin/node
const numbers = process.argv.slice(2).map((n) => Number(n));
let biggest = numbers.sort((a, b) => b - a)[1] ?? 0;
if (numbers.length === 1) biggest = 0;
console.log(biggest);
