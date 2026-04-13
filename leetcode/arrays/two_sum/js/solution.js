function solve(nums, target) {
  const seen = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (seen.has(complement)) return [seen.get(complement), i];
    seen.set(nums[i], i);
  }
  return [];
}

if (require.main === module) {
  console.log(solve([2,7,11,15], 9));
}

module.exports = { solve };

