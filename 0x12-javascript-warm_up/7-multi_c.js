#!/usr/bin/node
let count = 0;
if (process.argv.length < 3) {
	console.log('Missing number of occurrences');
} while (count <  process.argv[2]) {
	console.log('C is fun');
	count++;
}