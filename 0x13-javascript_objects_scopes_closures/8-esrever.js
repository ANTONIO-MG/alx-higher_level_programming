#!/usr/bin/node

// function that returns the reversed version of a list without use of reverse.
exports.esrever = function esrever (list) {
  const newList = [];
  let count = list.length - 1;

  while (count >= 0) {
    newList.push(list[count]);
    count--;
  }

  return (newList);
};
