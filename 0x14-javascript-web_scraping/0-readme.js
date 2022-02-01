#!/usr/bin/node

const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf8', error);

function error (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
}
