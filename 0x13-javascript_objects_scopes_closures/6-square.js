#!/usr/bin/node
const Rac = require('./5-square');
module.exports = class Square extends Rac {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      let ad = '';
      for (let index1 = 0; index1 < this.width; index1++) {
        ad = ad + c;
      }
      console.log(ad);
    }
  }
};
