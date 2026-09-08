# Valid Parentheses (LeetCode 20)

Given a string `s` containing only `()[]{}`, return whether the brackets are valid: every close bracket matches the most recent unmatched open bracket of the same type, in the correct order.

## Approach

Scan left to right with a stack of opening brackets. Push opens; on a close, pop and require a matching open. Reject early on mismatch or empty stack; accept only if the stack is empty at the end.

Time `O(n)`, space `O(n)`.

## Languages

`python`, `go`, `cpp`, `scala`, `rust`, `js` — each with `:run` and `:test`.

```bash
make test LANG=python QUESTION=valid_parentheses
make run LANG=cpp QUESTION=valid_parentheses
```
