#!usr/bin/node

// script that imports a dict of occurrences by user id and computes a dict.

const dict = require('./101-data').dict;
const newDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(newDict[dict[key]])) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});

console.log(newDict);
