#include <iostream>
#include <vector>

#include "solution.h"

int Solve(const std::vector<int>& nums, int target) {
    std::vector<int> dp(target + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= target; ++i) {
        for (int num : nums) {
            if (i - num >= 0) {
                dp[i] += dp[i - num];
            }
        }
    }
    return dp[target];
}

#ifndef ALGO_TEST
int main() {
    std::cout << Solve({1, 2, 3}, 4) << std::endl;
    return 0;
}
#endif
