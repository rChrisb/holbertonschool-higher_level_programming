#!/usr/bin/node

let numberOfTimes = process.argv[2];

if (process.argv[2] < 0) {
  numberOfTimes = 0;
  process.argv[2] *= -1;
}
if (!Number.isInteger(+process.argv[2])) { console.log('Missing number of occurrences'); } else {
  for (let times = 0; times < numberOfTimes; times++) {
    console.log('C is fun');
  }
}
