#include <cstdint>
#include <iostream>

#include "solution.h"

uint32_t Solve(uint32_t n) {
    uint32_t result = 0;
    for (int i = 0; i < 32; ++i) {
        result = (result << 1) | (n & 1U);
        n >>= 1;
    }
    return result;
}

#ifndef ALGO_TEST
int main() {
    std::cout << Solve(43261596U) << std::endl;
    return 0;
}
#endif
