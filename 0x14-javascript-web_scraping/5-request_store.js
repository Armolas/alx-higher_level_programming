#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');
request.get(url, (error, reponse, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
