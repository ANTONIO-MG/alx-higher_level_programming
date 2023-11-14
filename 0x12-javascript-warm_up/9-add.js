#!/usr/bin/node

// script that prints the addition of 2 integers.

function add (a, b) {
  return (Number(a) + Number(b));
}

const arr = process.argv.slice(2);

const intOne = arr[0];
const intTwo = arr[1];

if (intOne === (isNaN) || intTwo === (isNaN)) {
  console.log('NaN');
}

console.log(add(intOne, intTwo));
