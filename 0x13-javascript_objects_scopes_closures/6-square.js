#!/usr/bin/node

// class Square that defines a square and inherits from Square of 5-square.js.

const Squares = require('./5-square');

module.exports = class Square extends Squares {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
