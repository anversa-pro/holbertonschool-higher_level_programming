#!/usr/bin/node
/*
Script searches the second biggest integer in the list of arguments.
*/

let bigger = Number.MIN_SAFE_INTEGER;
let biggest = Number.MIN_SAFE_INTEGER;

if ((process.argv.length - 2) <= 1) {
  console.log(0);
} else {
  for (const i in process.argv) {
    const evalNumber = parseInt(process.argv[i]);
    if (evalNumber > bigger && evalNumber > biggest) {
      bigger = biggest;
      biggest = evalNumber;
    } else if (evalNumber > bigger && evalNumber < biggest) {
      bigger = evalNumber;
    }
  }
  console.log(bigger);
}
