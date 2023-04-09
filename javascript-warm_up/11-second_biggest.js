#!/usr/bin/node

if (!process.argv[2]) console.log(0);
if (process.argv.length === 3) console.log(0);

let max = 0;
let secondMax = 0;
const newList = [];

for (let i = 0; i < process.argv.length - 2; i++) {
  if (max < process.argv[i]) max = process.argv[i];
}
for (let i = 0; i < (process.argv).slice(2).length; i++) {
  if (process.argv[i] !== max) newList.push(process.argv[i]);
}

for (let i = 0; i < newList.length - 2; i++) {
  if (secondMax < newList[i]) secondMax = newList[i];
}
console.log(secondMax);
