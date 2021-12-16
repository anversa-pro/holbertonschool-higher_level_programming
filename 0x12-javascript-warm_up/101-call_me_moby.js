#!/usr/bin/node
// script that executes x time a function
exports.callMeMoby = function (x, theFunction) {
  for (; x > 0; x--) {
    theFunction();
  }
};
