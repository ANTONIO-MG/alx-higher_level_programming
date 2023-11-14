#!/usr/bin/node

// script that prints a square, The first argument is the size of the square.
let outer = 0;
let inner = 0;
let string = '';

const things = process.argv.slice(2);

outer = parseInt(things[0]);
inner = outer;

if (outer < 0 || outer > 0) {
  while (outer > 0) {
    while (inner > 0) {
      string += 'X';
      inner--;
    }
    console.log(string);
    outer--;
  }
} else {
  console.log('Missing size');
}
