#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const res = JSON.parse(body);
  const films = res.results;
  let present = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        present = present + 1;
      }
    }
  }
  console.log(present);
});
