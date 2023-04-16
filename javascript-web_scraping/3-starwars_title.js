#!/usr/bin/node

const request = require("request");

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, content) => {
    if (error) throw error;
    const parsedContent = JSON.parse(content);
    console.log(parsedContent.title);
  }
);
