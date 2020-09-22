#!/usr/bin/node
const repose = require('request');
const urlADress = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
repose(urlADress, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
