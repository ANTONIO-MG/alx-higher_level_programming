#!/usr/bin/node

// script that imports a dict of occurrences by user id and computes a dict.

const dict = require('./101-data').dict;

function main (inputDict) {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!resultDict[occurrences]) {
      resultDict[occurrences] = [];
    }

    resultDict[occurrences].push(userId.toString());
  }

  return resultDict;
}
