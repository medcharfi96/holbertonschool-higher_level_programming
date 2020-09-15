#!/usr/bin/node
let count = 2;
const tab = [];
let res;
if (process.argv.length < 4 || process.argv[3] === 1) {
	res = 0;
} else {
	while (count < process.argv.length) {
		if (typeof(parseInt(process.argv[count])) === 'number') {
			tab.join(process.argv[count]);
		}

	}
}
tab.sort;
res = tab[tab.length - 1];
console.log(res);