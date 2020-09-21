#!/usr/bin/node
const fs = require('fs');
const zed = require('process').argv[2];
const zed1 = require('process').argv[3];
const zed2 = require('process').argv[4];
const data1 = fs.readFileSync(zed, 'utf8');
const data2 = fs.readFileSync(zed1, 'utf8');
fs.appendFileSync(zed2, data1 + data2);
