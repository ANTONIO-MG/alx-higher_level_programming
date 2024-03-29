#!/usr/bin/node

// a class Rectangle that defines a rectangle.
// The constructor must take 2 arguments w and h.
// Initialize the instance attribute width with the value of w.
// Initialize the instance attribute height with the value of h.
// If w or h is equal to 0 or not a positive integer, create an empty object

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      // this will get passed..
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let outer = this.height;
    let inner = this.width;
    let string = '';

    while (outer > 0) {
      while (inner > 0) {
        string += 'X';
        inner--;
      }
      console.log(string);
      outer--;
    }
  }
};
