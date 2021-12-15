#!/usr/bin/node
/*
Script that prints x times a phrase
*/
const myPhrase = 'C is fun';
const printingTimes = process.argv[2];

if (parseInt(printingTimes)) {
  for (let i = 0; i < printingTimes; i++) {
    console.log(myPhrase);
  }
} else {
  console.log('Missing number of occurrences');
}
