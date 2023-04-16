#!/usr/bin/node

const fileToWriteIn = require('fs');
fileToWriteIn.writeFile(process.argv[2], process.argv[3], (error) => {
  if (error) throw error;
});
