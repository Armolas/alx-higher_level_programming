#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return null;
  } else {
    const result = parseInt(a) + parseInt(b);
    return result;
  }
}

const sum = add(argv[2], argv[3]);

if (sum == null) {
  console.log('NaN');
} else {
  console.log(sum);
}
