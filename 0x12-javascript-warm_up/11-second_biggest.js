#!/usr/bin/node

const argv = process.argv;
let high = 0;
let low = 0;
if (argv.length < 4) {
  console.log(low);
} else {
  for (let i = 0; i < argv.length; i++) {
    if (parseInt(argv[i]) > high) {
      high = parseInt(argv[i]);
    }
  }
  for (let i = 0; i < argv.length; i++) {
    if (parseInt(argv[i]) > low && parseInt(argv[i]) < high) {
      low = parseInt(argv[i]);
    }
  }
  console.log(low);
}
