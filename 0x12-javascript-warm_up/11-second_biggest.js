#!/usr/bin/node
let i = 0;
const tab = [];
if (process.argv.length > 3) {
  for (i = 0; i < process.argv.length; i++) {
    if (typeof (parseInt(process.argv[i])) === 'number') {
      tab.push(process.argv[i]);
    }
  }
} else {
  console.log(0);
}
tab.sort();
console.log(tab[tab.length - 2]);
