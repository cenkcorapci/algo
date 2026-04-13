import unittest

from solution import solve


class CombinationSum4Tests(unittest.TestCase):
    def test_example(self) -> None:
        # Known example: nums=[1,2,3], target=4 -> 7 combinations
        self.assertEqual(solve([1, 2, 3], 4), 7)


if __name__ == "__main__":
    unittest.main()

