#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, jsonContent) => {
  if (error) throw error;
  const content = JSON.parse(jsonContent);
  let counter = 0;
  content.results.forEach((element) => {
    if (element.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) { counter++; }
  });
  console.log(counter);
});
