#!/usr/bin/node

const request = require('request');
const tasksMap = {};
request(process.argv[2], (error, response, jsonContent) => {
  if (error) throw error;
  const content = JSON.parse(jsonContent);
  const tasksCompleted = [];
  content.forEach((task) => {
    if (task.completed) tasksCompleted.push(task);
  });
  for (let i = 0; i < tasksCompleted.length; i++) {
    const userId = tasksCompleted[i].userId;
    if (!tasksMap[userId]) tasksMap[userId] = 1;
    else tasksMap[userId]++;
  }
  console.log(tasksMap);
});
