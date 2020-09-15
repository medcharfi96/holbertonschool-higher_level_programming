#!/usr/bin/node
function factrouh (rbk) {
  if (isNaN(rbk) || rbk === 1) {
    return (1);
  } else {
    return factrouh(rbk - 1) * rbk;
  }
}
console.log(factrouh(parseInt(process.argv[2])));
