const assert = require('assert');
const { solve } = require('./solution');

assert.strictEqual(solve("()"), true);
assert.strictEqual(solve("()[]{}"), true);
assert.strictEqual(solve("(]"), false);
assert.strictEqual(solve("([)]"), false);
assert.strictEqual(solve("("), false);
console.log('OK');
