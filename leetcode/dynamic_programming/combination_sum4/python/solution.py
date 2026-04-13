from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]


def solve(nums: List[int], target: int) -> int:
    return Solution().combinationSum4(nums, target)


if __name__ == "__main__":
    # quick sanity-run
    print(solve([1, 2, 3], 4))

