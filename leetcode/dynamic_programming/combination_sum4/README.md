# Combination Sum IV (LeetCode 377)

Given distinct positive integers `nums` and a target, return how many ordered combinations of those numbers sum to `target` (order matters; reuse is allowed).

## Approach

Dynamic programming: `dp[t]` = number of ways to form sum `t`. Set `dp[0] = 1`. For each sum `i` from 1 to `target`, add `dp[i - num]` for every `num` that fits. Because the outer loop is over the sum and the inner over numbers, different orders count as distinct.

Time `O(target * |nums|)`, space `O(target)`.

## Languages

`python`, `go`, `cpp`, `scala`, `rust`, `js` — each with `:run` and `:test`.

```bash
make test LANG=python QUESTION=combination_sum4
make run LANG=rust QUESTION=combination_sum4
```
