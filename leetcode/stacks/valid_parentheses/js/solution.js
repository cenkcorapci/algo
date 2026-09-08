function solve(s) {
  const open = [];
  const pairs = { ")": "(", "]": "[", "}": "{" };
  for (const c of s) {
    if (c === "(" || c === "[" || c === "{") {
      open.push(c);
      continue;
    }
    if (open.length === 0 || open.pop() !== pairs[c]) return false;
  }
  return open.length === 0;
}

if (require.main === module) {
  console.log(solve("()[]{}"));
}

module.exports = { solve };
