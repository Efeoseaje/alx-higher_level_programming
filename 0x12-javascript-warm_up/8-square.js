#!/usr/bin/node
/*
A script that prints a square
 */

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const x = process.argv[2];
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
