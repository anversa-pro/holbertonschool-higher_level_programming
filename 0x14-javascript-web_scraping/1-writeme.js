#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, error);

function error (err) {
  if (err) {
    return console.error(err);
  }
}
