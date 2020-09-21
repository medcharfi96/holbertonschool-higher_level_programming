#!/usr/bin/node
exports.esrever = function (list) {
  const nnewlist = [];
  let i = list.length - 1;
  while (i >= 0) {
    nnewlist.push(list[i]);
    i--;
  }
  return nnewlist;
};
