#!/usr/bin/node
/*
Empty class Rectangle that defines a rectangle
The constructor takes 2 arguments and a condition
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w * h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
