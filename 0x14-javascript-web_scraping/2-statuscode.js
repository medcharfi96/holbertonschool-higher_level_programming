#!/usr/bin/node
const reponse = require('request');
reponse(process.argv[2], function (err, urlADREss) {
  if (!err) {
    console.log('code: ' + urlADREss.statusCode);
  } else {
    console.log(err);
  }
});
