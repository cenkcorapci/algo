#include <iostream>
#include <unordered_map>
#include <vector>

#include "solution.h"

std::vector<int> Solve(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen;
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        auto it = seen.find(complement);
        if (it != seen.end()) {
            return {it->second, i};
        }
        seen[nums[i]] = i;
    }
    return {};
}

#ifndef ALGO_TEST
int main() {
    auto answer = Solve({2, 7, 11, 15}, 9);
    std::cout << "[" << answer[0] << ", " << answer[1] << "]" << std::endl;
    return 0;
}
#endif
