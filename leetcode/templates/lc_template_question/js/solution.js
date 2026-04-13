function solve(input) {
  return input.trim();
}

if (require.main === module) {
  const fs = require('fs');
  const input = fs.readFileSync(0, 'utf8');
  console.log(solve(input));
}

module.exports = { solve };

