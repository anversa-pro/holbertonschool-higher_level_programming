#!/usr/bin/node
/*
Script that prints the first argument passed to it
*/
if (process.argv[2]) {
  console.log(process.argv[2]);
} else if (!process.argv[2]) {
  console.log('No argument');
}
