import unittest

from solution import solve


class MergeTwoSortedListsTests(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(solve([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])
        self.assertEqual(solve([], [0]), [0])
        self.assertEqual(solve([1, 2, 3], []), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
