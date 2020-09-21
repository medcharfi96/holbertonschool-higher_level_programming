#!/usr/bin/node

exports.converter = function (base) {
  return function (zabour) {
    return zabour.toString(base);
  };
};
