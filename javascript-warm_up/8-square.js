#!/usr/bin/node

let line = '';

if (!Number.isInteger(+process.argv[2])) console.log('Missing size');
for (let i = 0; i < process.argv[2]; i++) {
  line += 'X';
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(line);
}
