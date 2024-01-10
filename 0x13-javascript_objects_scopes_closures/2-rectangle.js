#!/usr/bin/node
Rectangle = class {
  constructor (w, h) {
    if (w < 1 || h < 1 || isNaN(w) || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
module.exports = Rectangle;
