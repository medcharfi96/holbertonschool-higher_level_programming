#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let index = 0;
  while (index < list.lenght) {
    if (list[index] === searchElement) {
      count = count + 1;
    }
    index++;
  }
  return (count);
};
