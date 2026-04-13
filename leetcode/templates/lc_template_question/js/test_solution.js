const assert = require('assert');
const { solve } = require('./solution');

if (solve('  abc  \n') !== 'abc') {
  throw new Error('trim failed');
}

console.log('OK');

