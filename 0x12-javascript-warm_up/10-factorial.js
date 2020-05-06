#!/usr/bin/node
// This script that computes and prints a factorial.
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
console.log(factorial(process.argv[2]));
