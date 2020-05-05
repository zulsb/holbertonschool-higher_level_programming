#!/usr/bin/node
// This script that prints the first argument.
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
