#!/usr/bin/node

exports.converter = function (base) {
  function convertEr (n) {
    return n.toString(base);
  }
  return convertEr;
};
