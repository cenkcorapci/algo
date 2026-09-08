#include <string>

#include "solution.h"

bool Solve(const std::string& s) {
    std::string open;
    open.reserve(s.size());

    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            open.push_back(c);
            continue;
        }
        if (open.empty()) {
            return false;
        }

        char top = open.back();
        open.pop_back();
        if ((c == ')' && top != '(') || (c == ']' && top != '[') || (c == '}' && top != '{')) {
            return false;
        }
    }

    return open.empty();
}

#ifndef ALGO_TEST
int main() {
    return Solve("()[]{}") ? 0 : 1;
}
#endif
