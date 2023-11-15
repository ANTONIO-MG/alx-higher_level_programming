#!/usr/bin/node

// a class Rectangle that defines a rectangle.
// The constructor must take 2 arguments w and h.
// Initialize the instance attribute width with the value of w.
// Initialize the instance attribute height with the value of h.
// If w or h is equal to 0 or not a positive integer, create an empty object
// method called print() that prints the rectangle using the character X
// method called rotate() exchanges the width and the height.
// method called double() multiples the width and the height by 2.

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 || h <= 0) || (w === undefined || h === undefined)) {
      // this will get passed..
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print (char = 'X') {
    let outer = this.height;
    let inner = this.width;
    let string = '';

    while (outer > 0) {
      while (inner > 0) {
        string += char;
        inner--;
      }
      console.log(string);
      outer--;
    }
  }

  rotate () {
    const tempOne = this.height;
    const tempTwo = this.width;
    this.height = tempTwo;
    this.width = tempOne;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
