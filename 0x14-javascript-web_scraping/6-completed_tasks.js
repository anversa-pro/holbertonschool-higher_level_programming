#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const userCompletedTasks = {};

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  else {
    const result = JSON.parse(body);
    for (const user of result) {
      if (user.completed === true) {
        const idToAdd = user.userId;
        if (!userCompletedTasks[idToAdd]) {
          userCompletedTasks[idToAdd] = 1;
        } else {
          userCompletedTasks[idToAdd] += 1;
        }
      }
    }
    console.log(userCompletedTasks);
  }
});
