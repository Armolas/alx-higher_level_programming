#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const todos = JSON.parse(body);
  let userId = 1;
  let complete = 0;
  const completed = {};
  for (const todo of todos) {
    if (todo.userId !== userId) {
      completed[userId] = complete;
      userId = todo.userId;
      complete = 0;
    }
    if (todo.completed === true) {
      complete = complete + 1;
    }
  }
  completed[userId] = complete;
  console.log(completed);
});
