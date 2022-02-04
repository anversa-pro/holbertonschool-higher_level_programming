#!/usr/bin/node
const squaresix = require('./5-square');

class Square extends squaresix {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
