# Merge Two Sorted Lists (LeetCode 21)

Merge two sorted linked lists into one sorted list by splicing nodes from the inputs (reuse existing nodes).

## Approach

Use a dummy head and a tail pointer. While both lists remain, attach the smaller head to `tail` and advance that list. Attach any leftover suffix once one list is exhausted. Return `dummy.next`.

Time `O(n + m)`, space `O(1)` extra (beyond the output list structure).

## Languages

`python`, `go`, `cpp`, `scala`, `rust`, `js` — each with `:run` and `:test`.

```bash
make test LANG=cpp QUESTION=merge_two_sorted_lists
make run LANG=python QUESTION=merge_two_sorted_lists
```
