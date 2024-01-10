#!/usr/bin/node

let num = -1;
exports.logMe = function (item) {
  num += 1;
  console.log(num + ': ' + item);
};
