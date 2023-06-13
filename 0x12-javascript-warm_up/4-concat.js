#!/usr/bin/node
const args = Array.from(process.argv).slice(2);
const firstArg = args?.at(0);
const secondArg = args?.at(1);
console.log(`${firstArg} is ${secondArg}`);
