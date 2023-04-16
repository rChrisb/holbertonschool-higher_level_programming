#!/usr/bin/node

const fileToRead = require('fs');
fileToRead.readFile(process.argv[2], 'utf-8', (error, fileContent) => {
  if (error) throw error;
  console.log(fileContent);
});
