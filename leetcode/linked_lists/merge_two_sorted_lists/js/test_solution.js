const assert = require('assert');
const { solve } = require('./solution');

assert.deepStrictEqual(solve([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]);
assert.deepStrictEqual(solve([], [0]), [0]);
assert.deepStrictEqual(solve([1, 2, 3], []), [1, 2, 3]);
console.log('OK');
