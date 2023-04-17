#!/usr/bin/node

const request = require('request');
const fileToWriteIn = require('fs');
request(process.argv[2], (error, response, content) => {
  if (error) throw error;
  fileToWriteIn.writeFile(process.argv[3], content, (error) => {
    if (error) throw error;
  });
});
