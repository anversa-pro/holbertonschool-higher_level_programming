#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
const factorialNumber = parseInt(process.argv[2]);
let factorialResult = 1;

if (!factorialNumber) {
  console.log(factorialResult);
} else {
  for (let i = factorialNumber; i > 1; i--) {
    factorialResult *= i;
  }
  console.log(factorialResult);
}
