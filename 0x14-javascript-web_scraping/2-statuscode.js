#!/usr/bin/node
const reponse = require('request');
reponse(process.argv[2], function (err, url) {
  if (err !== undefined) {
    console.log(err);
  } else {
    console.log('code: ' + url.statusCode);
  }
});
