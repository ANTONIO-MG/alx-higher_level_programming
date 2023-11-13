#!/usr/bin/node

//   script that prints 3 lines: using array string loop
let loop = 0;
const lineOne = 'C is fun';
const lineTwo = 'Python is cool';
const lineThree = 'JavaScript is amazing';
const ar = [lineOne, lineTwo, lineThree];

while (loop <= 2) {
  console.log(ar[loop]);
  loop++;
}
