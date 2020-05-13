#!/usr/bin/node
const request = require('request');
const result = {};
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    JSON.parse(body).forEach(element => {
      if (element.completed === true) {
        if (result[element.userId] === undefined) {
          result[element.userId] = 0;
        }
        result[element.userId]++;
      }
    });
  }
  console.log(result);
});
