#!/usr/bin/node

const oldSquare = require("./5-square.js");

class Square extends oldSquare {
  charPrint(c) {
    if (c) {
      let line = "";
      for (let i = 0; i < this.width; i++) {
        line += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(line);
      }
    } else this.print();
  }
}
module.exports = Square;
