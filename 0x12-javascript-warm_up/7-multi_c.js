#!/usr/bin/node
// This script that prints x times “C is fun”.
if (!isNaN(process.argv[2])) {
  for (let a = 0; a < process.argv[2]; a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
