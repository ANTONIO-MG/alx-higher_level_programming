#!/usr/bin/node

// function that returns the number of occurrences in a list.
// given the list and the item being serached for

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  list.forEach(element => {
    if (element === searchElement) {
      count++;
    }
  });

  return (count);
};
