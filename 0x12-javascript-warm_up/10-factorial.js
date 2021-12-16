#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
const factorialNumber = parseInt(process.argv[2]);

if (!factorialNumber) {
  console.log(1);
} else {
  factorialCalculation(factorialNumber);
}

function factorialCalculation (a) {
  let calculation = 1;
  for (let i = a; i > 1; i--) {
    calculation *= i;
  }
  console.log(calculation);
}
