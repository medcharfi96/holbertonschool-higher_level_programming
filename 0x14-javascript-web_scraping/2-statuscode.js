#!/usr/bin/node
const reponse = require('request');
reponse(process.argv[2], function (err, url) {
  if (!err) {
    console.log('code: ' + url.statusCode);
  } else {
    console.log(err);
  }
});
