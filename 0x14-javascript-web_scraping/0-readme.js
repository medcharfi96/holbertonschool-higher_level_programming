#!/usr/bin/node
const fs = require('fs');
const path = process.argv;

fs.readFile(path[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
