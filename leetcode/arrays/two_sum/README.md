# Two Sum (LeetCode 1)

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Each input has exactly one solution; you may not use the same element twice.

## Approach

One pass with a hash map from value → index. For each index `i`, look up `target - nums[i]`; if present, return those indices, otherwise store `nums[i] → i`.

Time `O(n)`, space `O(n)`.

## Languages

`python`, `go`, `cpp`, `scala`, `rust`, `js` — each with `:run` and `:test`.

```bash
make test LANG=python QUESTION=two_sum
make run LANG=go QUESTION=two_sum
```
