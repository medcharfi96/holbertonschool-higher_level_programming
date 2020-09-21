#!/usr/bin/node

const zavour = require('./100-data').list;
console.log(zavour);
const lisssss = zavour.map((x, i) => x * i);
console.log(lisssss);
