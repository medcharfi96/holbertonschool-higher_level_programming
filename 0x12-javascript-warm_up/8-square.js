#!/usr/bin/node
let count = 0;
if (process.argv.length < 3) {
  console.log('Missing size');
} else if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let j;
  let sortie = '';
  for (count = 0; count < parseInt(process.argv[2]); count++) {
    for (j = 0; j < parseInt(process.argv[2]); j++) {
      sortie += 'X';
    }
    console.log(sortie);
    sortie = '';
  }
}
