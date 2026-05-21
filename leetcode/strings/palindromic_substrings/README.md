Palindromic Substrings (LeetCode)
================================

This directory contains a C++ template for the LeetCode problem "Palindromic Substrings".

## Description

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.



```bash
bazel run //leetcode/strings/palindromic_substrings/cpp:run
```

Run tests:

```bash
bazel test //leetcode/strings/palindromic_substrings/cpp:test
```

This is a template only; implement the algorithm in `solution.cc` and extend tests in `solution_test.cc`.

