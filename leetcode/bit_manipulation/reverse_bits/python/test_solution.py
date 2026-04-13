import unittest

from solution import solve


class ReverseBitsTests(unittest.TestCase):
    def test_example(self) -> None:
        # Known example: 43261596 -> 964176192 after bit-reversal (32-bit)
        self.assertEqual(solve(43261596), 964176192)


if __name__ == "__main__":
    unittest.main()

