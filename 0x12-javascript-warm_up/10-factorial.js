#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
const factorialNumber = parseInt(process.argv[2]);
console.log(factorialCalculation(factorialNumber));

function factorialCalculation (a) {
  let calculation = 1;
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  for (let i = 1; i <= a; i++) {
    calculation *= i;
  }
  return (calculation);
}
