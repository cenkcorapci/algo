#include <cassert>
#include <vector>

#include "solution.h"

int main() {
    {
        auto got = Solve({2, 7, 11, 15}, 9);
        assert((got == std::vector<int>{0, 1}));
    }
    {
        auto got = Solve({1, 2, 3}, 99);
        assert(got.empty());
    }
    return 0;
}
