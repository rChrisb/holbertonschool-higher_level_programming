#!/usr/bin/node

console.log(
  Number.isInteger(+process.argv[2])
    ? 'My number: ' + process.argv[2]
    : 'Not a number'
);
