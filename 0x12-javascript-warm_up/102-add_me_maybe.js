#!/usr/bin/node
// script that executes x time a function
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  theFunction(number);
};
