#!/usr/bin/node
const argv = process.argv[2];
let square;
if (isNaN(argv)) {
  console.log('Missing number');
} else {
  for (let i = 0; i < argv; i++) {
    square = '';
    for (let j = 0; j < argv; j++) {
      square = square + 'X';
    }
    console.log(square);
  }
}
