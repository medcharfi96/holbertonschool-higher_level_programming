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
};
