#!/usr/bin/node
const request = require('request');

const endpoint = process.argv[2];
request(endpoint, function (error, response, body) {
  if (error) return;
  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completed = tasks.reduce((completed, task) => {
      if (task.completed) {
        if (!completed[task.userId]) completed[task.userId] = 1;
        else completed[task.userId] += 1;
      }
      return completed;
    }, {});

    console.log(completed);
  }
});
