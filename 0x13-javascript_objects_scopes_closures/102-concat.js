#!/usr/bin/node
const fs = require('fs');

const file0 = process.argv[2];
const file1 = process.argv[3];
const outFile = process.argv[4];

const content0 = fs.readFileSync(file0);
const content1 = fs.readFileSync(file1);
const outContent = content0 + content1;
fs.writeFileSync(outFile, outContent);
