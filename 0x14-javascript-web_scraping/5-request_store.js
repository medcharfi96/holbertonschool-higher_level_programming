#!/usr/bin/node
const filesystem = require('fs');
const process = require('process');
const rps = require('request');
const data1 = process.argv[2];
const data0 = process.argv[3];

rps(data1, (error, response, body) => {
  if (!error) {
    filesystem.writeFileSync(data0, body, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  } else {
    console.log(error);
  }
});
