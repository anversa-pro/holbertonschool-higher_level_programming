#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '/18/';
let movieCounter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const movie of JSON.parse(body).results) {
      for (const character of movie.characters) {
        if (character.includes(characterId)) {
          movieCounter++;
        }
      }
    }
    console.log(movieCounter);
  }
});
