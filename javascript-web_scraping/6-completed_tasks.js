#!/usr/bin/node

const request = require("request");
const taskMap = {};
request(process.argv[2], (error, response, jsonContent) => {
  if (error) throw error;
  content = JSON.parse(jsonContent);
  const taskCompleted = [];
  content.forEach((task) => {
    if (task.completed) taskCompleted.push(task);
  });
  for (let i = 0; i < taskCompleted.length; i++) {
    let userId = taskCompleted[i].userId;
    if (!taskMap[userId]) taskMap[userId] = 1;
    else taskMap[userId]++;
  }
  console.log(taskMap);
});
