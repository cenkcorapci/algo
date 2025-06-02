class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1
        return result
sol = Solution()
print(sol.reverseBits(110011) == 110011)
print(sol.reverseBits(111011) == 110111)



