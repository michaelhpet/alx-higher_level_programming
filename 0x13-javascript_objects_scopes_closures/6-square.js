#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    const character = c ?? 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
