#!/usr/bin/node

// script that prints a message depending of the number of arguments passed.
let count = 0;
const things = process.argv.slice(2);
things.forEach(element => {
  count++;
});

if (count <= 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log('Argument found');
} else if (count >= 2) {
  console.log('Arguments found');
}
