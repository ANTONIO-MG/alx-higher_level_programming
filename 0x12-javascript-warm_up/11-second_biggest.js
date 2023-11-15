#!/usr/bin/node

// script that searches the second biggest integer in the list of arguments.
let max = 0;

let number = process.argv.slice(2);

max = number[0];

number.forEach((num) => {
  if (num > max) {
    max = num;
  }
});

number.slice(index, 1);
