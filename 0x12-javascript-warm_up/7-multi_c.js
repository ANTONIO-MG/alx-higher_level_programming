#!/usr/bin/node

//   script that prints x times “C is fun”, x is the first argument.
let loop = 0;

const things = process.argv.slice(2);

loop = parseInt(things[0]);

console.log(loop);

if (loop < 0 || loop > 0) {
  while (loop > 0) {
    console.log('C is fun');
    loop--;
  }
} else {
  console.log('Missing number of occurrences');
}
