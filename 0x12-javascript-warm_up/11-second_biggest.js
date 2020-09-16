#!/usr/bin/node
let i = 0;
const tab = [];
let res;
if (process.argv.length > 3) {
  for (i = 0; i < process.argv.length; i++) {
    if (isNaN(process.argv[i])) {
      continue;
    } else if (typeof (parseInt(process.argv[i])) === 'number') {
      tab.push(parseInt(process.argv[i]));
    }
  }
  tab.sort(function (a, b) { return a - b; });
  res = tab[tab.length - 2];
} else {
  res = 0;
}
console.log(res);
