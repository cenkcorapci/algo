function solve(n) {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result = (result << 1) | (n & 1);
    n >>>= 1;
  }
  return result >>> 0;
}

if (require.main === module) {
  console.log(solve(43261596));
}

module.exports = { solve };
