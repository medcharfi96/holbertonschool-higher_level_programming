#!/usr/bin/node
const process = require('process');
const rps = require('request');
const URLADRess = process.argv;
rps(URLADRess[2], (error, response, body) => {
  if (!error) {
    let counter = 0;
    for (const f of JSON.parse(body).results) {
      if (f.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        counter = counter + 1;
      }
    }
    console.log(counter);
  } else {
    return console.log(error);
  }
});
