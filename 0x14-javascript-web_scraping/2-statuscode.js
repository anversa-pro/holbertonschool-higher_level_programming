#!/usr/bin/node

const request = require('request');
const urlToGet = process.argv[2];

request(urlToGet, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
