#!/usr/bin/node

let argumentsList = [];

process.argv.forEach((element, index) => {
  if (index > 1) {
    argumentsList.push(element);
  }
});

console.log(`${argumentsList[0]} is ${argumentsList[1]}`);
