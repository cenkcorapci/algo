import unittest

from solution import solve


class TwoSumTests(unittest.TestCase):
    def test_finds_pair(self) -> None:
        self.assertEqual(solve([2, 7, 11, 15], 9), [0, 1])

    def test_returns_empty_when_missing(self) -> None:
        self.assertEqual(solve([1, 2, 3], 99), [])


if __name__ == "__main__":
    unittest.main()

