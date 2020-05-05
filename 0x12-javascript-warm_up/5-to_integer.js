#!/usr/bin/node
// This script that prints My number: <first argument converted in integer>.
if (!isNaN(process.argv[2])) {
  console.log('My number: %i', process.argv[2]);
} else {
  console.log('Not a number');
}
