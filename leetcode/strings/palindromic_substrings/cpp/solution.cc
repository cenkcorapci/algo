// Standard library headers: do not allocate memory themselves; they
// make types and functions available to the compiler. No program
// memory is created by these lines at runtime.
#include <iostream> // provides std::cout (no storage allocated here)
#include <string>   // provides std::string (class type)
#include <vector>   // provides std::vector (class template)

#include "solution.h" // includes the declaration of Solve; no runtime allocation

// Define the function that computes number of palindromic substrings.
// When this function is called, a new stack frame is created for its
// local variables and parameters. Any objects with automatic storage
// duration live on that stack frame (or manage heap internally).
int Solve(const std::string& s) {
    // 's' is a const reference parameter: it does NOT copy the
    // string contents. The caller's std::string is not duplicated.

    int n = static_cast<int>(s.size());
    // 'n' is an int stored on the stack in this function's frame.
    // s.size() typically reads s's internal size member (no heap alloc).

    if (n == 0) return 0; // early return; nothing allocated

    int res = 0; // result counter stored on the stack

    // The lambda below captures local variables by reference ([&]).
    // The lambda object itself is a small callable stored on the stack
    // (its closure object), and it holds references (not copies) to
    // local variables like 'res' and 's' — those are not reallocated.
    // Because the lambda is used only within the lifetime of this
    // function, referencing stack locals is safe.
    auto expand = [&](int l, int r) {
        // 'l' and 'r' are function parameters for the lambda — they
        // are allocated on the lambda's invocation stack frame when
        // the lambda is called (not stored persistently).
        while (l >= 0 && r < n && s[l] == s[r]) {
            // Accessing s[l] and s[r] reads characters from the
            // caller-owned std::string buffer. That buffer is not
            // copied because 's' is a reference.
            ++res; // increments the stack-stored counter
            --l; ++r; // simple integer arithmetic on the stack
        }
        // When the lambda returns, its parameters l,r are destroyed
        // (no heap deallocation is necessary since these are ints).
    };

    // Loop variable 'i' is a stack integer. The loop does not allocate
    // heap memory; it repeatedly calls the lambda which updates 'res'.
    for (int i = 0; i < n; ++i) {
        expand(i, i);     // odd-length centers: passes copies of ints
        expand(i, i + 1); // even-length centers
    }

    // 'res' is returned by value. Returning an int copies a small
    // value into the caller's context (typically via a register).
    return res;
}

#ifndef ALGO_TEST
// This main is only compiled when ALGO_TEST is not defined. When built
// as part of a library/test (where ALGO_TEST is defined), this block
// is excluded so there is no duplicate 'main' symbol.
int main() {
    // Temporary std::string is created from the string literal "abc";
    // the temporary is stored in automatic storage and manages its own
    // small internal buffer (SSO or heap depending on implementation).
    std::cout << Solve("abc") << std::endl;
    // std::cout is a global object (static storage), its internal
    // buffers manage I/O; printing here does not create persistent heap
    // allocations in our code.
    return 0; // program exit; stack is unwound and local objects destroyed
}
#endif
