#!/usr/bin/node
const dict = require('./101-data').dict;
const ids = [...new Set(Object.values(dict))];
const result = ids.reduce((newDict, id) => {
  newDict[id] = Object.keys(dict).filter((key) => dict[key] === id);
  return newDict;
}, {});
console.log(result);
