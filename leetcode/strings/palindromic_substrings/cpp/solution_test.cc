#include <cassert>
#include <string>

#include "solution.h"

int main() {
    // Tests for palindromic substrings
    {
        auto got = Solve("");
        assert(got == 0);
    }

    {
        // no palindromic substrings longer than 1
        auto got = Solve("abc");
        assert(got == 3); // a, b, c
    }

    {
        // all characters same
        auto got = Solve("aaa");
        // substrings: a, a, a, aa, aa, aaa => 6
        assert(got == 6);
    }

    {
        // mixed palindrome
        auto got = Solve("aba");
        // a, b, a, aba => 4
        assert(got == 4);
    }

    {
        // single char
        auto got = Solve("x");
        assert(got == 1);
    }

    return 0;
}

