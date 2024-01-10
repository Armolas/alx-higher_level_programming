#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w < 1 || h < 1 || isNaN(w) || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect = rect + 'X';
      }
      console.log(rect);
    }
  }
};
module.exports = Rectangle;
