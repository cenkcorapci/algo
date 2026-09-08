# Reverse Bits (LeetCode 190)

Reverse the bits of a 32-bit unsigned integer and return the result as an unsigned 32-bit value.

## Approach

Build the answer bit by bit over 32 steps: take the low bit of `n` with `n & 1`, shift the result left and OR that bit in, then shift `n` right. After 32 iterations the bit order is reversed.

Time `O(1)` (fixed 32 steps), space `O(1)`.

## Languages

`python`, `go`, `cpp`, `scala`, `rust`, `js` — each with `:run` and `:test`.

```bash
make test LANG=python QUESTION=reverse_bits
make run LANG=go QUESTION=reverse_bits
```
