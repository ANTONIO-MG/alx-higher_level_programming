#!/usr/bin/node

// class Square that defines a square and inherits from Square of 5-square.js.

const Squares = require('./5-square');

module.exports = class Square extends Squares {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let outer = this.size;
    let inner = this.size;
    let string = '';

    if (c === undefined) {
      c = 'X';
    }

    while (outer > 0) {
      while (inner > 0) {
        string += c;
        inner--;
      }
      console.log(string);
      outer--;
    }
  }
};
