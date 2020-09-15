#!/usr/bin/node
let i = 0;
const tab = [];
let res;
if (process.argv.length > 3) {
  for (i = 0; i < process.argv.length; i++) {
    if (typeof (parseInt(process.argv[i])) === 'number') {
      tab.push(process.argv[i]);
    }
  }
  tab.sort();
  res = tab[tab.length - 2];
} else {
  res = 0;
}

console.log(res);
