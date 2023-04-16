#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, content) => {
  console.log(`code: ${response.statusCode}`);
});
