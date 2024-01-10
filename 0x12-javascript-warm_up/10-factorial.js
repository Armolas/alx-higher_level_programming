#!/usr/bin/node

const argv = process.argv;

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n < 1) {
    return 1;
  } else {
    return parseInt(n) * factorial(parseInt(n) - 1);
  }
}

console.log(factorial(argv[2]));
