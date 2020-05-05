#!/usr/bin/node
// This script that prints a square.
if (!isNaN(process.argv[2])) {
  for (let a = 0; a < process.argv[2]; a++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
