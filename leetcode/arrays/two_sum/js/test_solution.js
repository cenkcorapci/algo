const assert = require('assert');
const { solve } = require('./solution');

assert.deepStrictEqual(solve([2,7,11,15], 9), [0,1]);
assert.deepStrictEqual(solve([1,2,3], 99), []);
console.log('OK');

