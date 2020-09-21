#!/usr/bin/node
const lista1 = require('./101-data.js').dict;
const lista2 = {};
for (const key in lista1) {
  if (lista2[lista1[key]] !== undefined) {
    lista2[lista1[key]].push(key);
  } else {
    lista2[lista1[key]] = [key];
  }
}
console.log(lista2);
