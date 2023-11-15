#!/usr/bin/node

//  function that prints the number of arguments already printed new args.
let count = 0;

exports.logMe = function logMe (item) {
  console.log(count + ': ' + item);
  count++;
};
