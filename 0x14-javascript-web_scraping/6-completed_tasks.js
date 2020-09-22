#!/usr/bin/node
const rps = require('request');
rps(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const taskFini = {};
  JSON.parse(body).forEach(task => {
    if (task.completed === true) {
      if (taskFini[task.userId] === undefined) {
        taskFini[task.userId] = 1;
      } else {
        taskFini[task.userId] = taskFini[task.userId] + 1;
      }
    }
    console.log(taskFini);
  });
});
