#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h) {
      if (w <= 0 || h <= 0) return;
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';
    for (let i = 0; i < this.width; i++) {
      line += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}
module.exports = Rectangle;
