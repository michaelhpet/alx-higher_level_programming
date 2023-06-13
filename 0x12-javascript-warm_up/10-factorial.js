#!/usr/bin/node
const number = process.argv[2];
console.log(factorial(Number(number)));

function factorial (n) {
  if (!n || n < 2) return 1;
  return n * factorial(n - 1);
}
