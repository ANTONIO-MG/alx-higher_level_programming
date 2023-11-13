#!/usr/bin/node

// script that prints two arguments passed to it, joined by: “ is ”
let count = 0;
let item1 = '';
let item2 = '';
const things = process.argv.slice(2);
things.forEach(element => {
  count++;
  if (count <= 1) {
    item1 = element;
  } else if (count === 2) {
    item2 = element;
  }
});

if (count === 0) {
  console.log('undefined is undefined');
} else if (count === 1) {
  console.log(item1 + ' is undefined');
} else if (count === 2) {
  console.log(item1 + ' is ' + item2);
}
