#!/usr/bin/node

const args = process.argv.slice(2);
const argsCounter = args.length;

if (argsCounter === 0) {
  console.log('No argument');
} else if (argsCounter === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
