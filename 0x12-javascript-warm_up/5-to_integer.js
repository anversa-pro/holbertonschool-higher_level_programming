#!/usr/bin/node
/*
Script script that prints My number
if the first argument can be converted to an integer:
*/
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
