#!/usr/bin/node
/*
Script that prints the addition of 2 integers
*/
const firstNumber = parseInt(process.argv[2]);
const secondNumber = parseInt(process.argv[3]);

if (firstNumber && secondNumber) {
  add(firstNumber, secondNumber);
} else {
  console.log(secondNumber);
}
function add (a, b) {
  const addition = a + b;
  console.log(addition);
}
