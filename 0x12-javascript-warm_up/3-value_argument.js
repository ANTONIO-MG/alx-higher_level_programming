#!/usr/bin/node

// script that prints the first argument passed to it.
let count = 0;
const things = process.argv.slice(2);
things.forEach(element => {
  count++;
  if (count <= 1) {
    console.log(element);
  }
});

if (count === 0) {
  console.log('No argument');
}