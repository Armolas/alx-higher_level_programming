#!/usr/bin/node
const square = require('./5-square');

const Square = class extends square {
  charPrint (c) {
    let char;
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect = rect + char;
      }
      console.log(rect);
    }
  }
};
module.exports = Square;
