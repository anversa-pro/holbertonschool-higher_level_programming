#!/usr/bin/node
/*
Script that prints 3 lines using an array and a loop
*/
const myVar = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const i in myVar) {
  console.log(myVar[i]);
}
