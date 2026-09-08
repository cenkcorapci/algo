function solve(nums, target) {
  const dp = Array(target + 1).fill(0);
  dp[0] = 1;
  for (let i = 1; i <= target; i++) {
    for (const num of nums) {
      if (i - num >= 0) dp[i] += dp[i - num];
    }
  }
  return dp[target];
}

if (require.main === module) {
  console.log(solve([1, 2, 3], 4));
}

module.exports = { solve };
