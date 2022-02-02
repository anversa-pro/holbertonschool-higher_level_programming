#!/usr/bin/node
const process = require('process');
const request = require('request');
const movieId = String(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movieCharacters = JSON.parse(body).characters;
    movieCharacters.forEach(requestCh);
  }
});

function requestCh (eachCharacter) {
  request(eachCharacter, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}
