#include <cassert>

#include "solution.h"

int main() {
    assert(Solve("()"));
    assert(Solve("()[]{}"));
    assert(!Solve("(]"));
    assert(!Solve("([)]"));
    assert(!Solve("("));
    return 0;
}
