#!/usr/bin/node
const fs = require('fs');
const info = process.argv[3];
const lien = process.argv[2];
fs.writeFileSync(lien, info, (err) => {
  if (err) {
    console.log(err);
  }
});
