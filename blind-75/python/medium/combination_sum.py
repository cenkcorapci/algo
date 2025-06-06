from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

    The test cases are generated so that the answer can fit in a 32-bit integer.
        :param self:
        :param nums:
        :param target:
        :return:
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]


sol = Solution()
sol.combinationSum4([1, 2, 3], 4)
