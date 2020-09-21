#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {}
  }

  print () {
    let affichage;
    for (let index = 0; index < this.height; index++) {
      affichage = '';
      for (let index1 = 0; index1 < this.width; index1++) {
        affichage = affichage + 'X';
      }
      console.log(affichage);
    }
  }

  rotate () {
    const zabour = this.width;
    this.width = this.height;
    this.height = zabour;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};

const Rac = require('./5-square');
module.exports = class Square extends Rac {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charactere = '';
    if (c === undefined) {
      charactere = 'X';
    } else {
      charactere = c;
    }
    for (let index = 0; index < this.height; index++) {
      let ad = '';
      for (let index1 = 0; index1 < this.width; index1++) {
        ad = ad + charactere;
      }
      console.log(ad);
    }
  }
};
