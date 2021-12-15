#!/usr/bin/node
/*
Script that prints a square with an x
*/
let myLine = '';
const printingTimes = process.argv[2];

if (parseInt(printingTimes)) {
  for (let i = 0; i < printingTimes; i++) {
    myLine += 'X';
  }
  for (let j = 0; j < printingTimes; j++) {
    console.log(myLine);
  }
} else {
  console.log('Missing size');
}
