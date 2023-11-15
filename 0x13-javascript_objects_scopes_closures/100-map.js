#!/usr/bin/node

// script that imports an array and computes a new array.
//  new list = value equal to initial list, multipled by the index in the list
const compute = require('./100-data').list;

console.log(compute);
console.log(compute.map((x, idx) => x * idx));