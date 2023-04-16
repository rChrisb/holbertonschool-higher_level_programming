#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, content) => {
  if (error) throw error;
  console.log(`code: ${response.statusCode}`);
});
