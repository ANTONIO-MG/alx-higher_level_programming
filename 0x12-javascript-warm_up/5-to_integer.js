#!/usr/bin/node

// script that prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer print “Not a number”
let count = 0;
let number;
const things = process.argv.slice(2);
things.forEach(element => {
  count++;
  if (count === 1) {
    number = element;
  }
});

console.log('My number: ' + parseInt(number));
