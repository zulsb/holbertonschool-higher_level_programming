#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const search = JSON.parse(body).results;
    for (let i = 0; i < search.length; i++) {
      const characters = search[i].characters;
      for (let c = 0; c < characters.length; c++) {
        if (characters[c].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
