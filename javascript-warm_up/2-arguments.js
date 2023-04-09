#!/usr/bin/node

let numberOfArgs = 0;

process.argv.forEach(element => {
	numberOfArgs++;
});

if (numberOfArgs < 3) console.log('No argument');
if (numberOfArgs == 3) console.log('Argument found');
if (numberOfArgs > 3) console.log('Arguments found');
