#!/usr/bin/node
/*
a script that prints a message depending of the number of arguments passed
*/
const { argv } = require('process');

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length > 2) {
  console.log('Arguments found');
}
