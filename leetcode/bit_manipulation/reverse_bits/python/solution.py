class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1
        return result


def solve(n: int) -> int:
    """Wrapper that runs the existing Solution implementation.

    Args:
        n: 32-bit unsigned integer to reverse bits of.

    Returns:
        Integer with bits reversed.
    """
    return Solution().reverseBits(n)


if __name__ == "__main__":
    # Example input from the LeetCode problem description
    print(solve(43261596))

