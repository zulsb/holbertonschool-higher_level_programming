#!/usr/bin/node
// This script that searches the second biggest integer.
function sBig (array) {
  if (arguments[0].length <= 1) {
    return 0;
  } else if (!arguments[0]) {
    return 0;
  } else {
    array.sort((x, y) => x - y);
    array.pop();
    return (array.pop());
  }
}
console.log(sBig(process.argv.slice(2)));
