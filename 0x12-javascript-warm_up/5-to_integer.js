#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else if (typeof (parseInt(process.argv[2])) === 'number' && process.argv[2]) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
