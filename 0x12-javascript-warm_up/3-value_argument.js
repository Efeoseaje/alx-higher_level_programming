#!/usr/bin/node

/*
Prints the first argument passed to it
 */
console.log(process.agrv[2] ? process.argv[2] : 'No argument');
