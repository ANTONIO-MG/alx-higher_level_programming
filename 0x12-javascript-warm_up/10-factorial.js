#!/usr/bin/node

// script that computes and prints a factorial of a number.

function factorial(a) {
  a = Number(a); // Convert to a number

  if (isNaN(a)) {
    console.log('NaN');
    return; // Exit the function if the input is not a valid number
  }

  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const arr = process.argv.slice(2);

const input = arr[0];

factorialResult = factorial(input);

console.log(factorialResult);
