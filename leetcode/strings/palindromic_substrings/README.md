# Palindromic Substrings (LeetCode 647)

Given a string `s`, return the number of palindromic substrings in it. A substring is contiguous; single characters count as palindromes.

## Approach

Expand around centers: for each index, count odd-length palindromes centered at that index and even-length ones centered between `i` and `i + 1`. Each expansion that stays a palindrome adds one to the answer.

Time `O(n²)`, space `O(1)`.

## Languages

Currently `cpp` (Bazel) and a `rust` Cargo sketch.

```bash
bazel test //leetcode/strings/palindromic_substrings/cpp:test
bazel run //leetcode/strings/palindromic_substrings/cpp:run
```
