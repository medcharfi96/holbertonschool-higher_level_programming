#!/usr/bin/node
exports.callMeMoby = function (x, TheFunction) {
  let count = 0;
  while (count < x) {
    TheFunction();
    count++;
  }
};
