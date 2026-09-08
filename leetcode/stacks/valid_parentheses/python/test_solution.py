import unittest

from solution import solve


class ValidParenthesesTests(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(solve("()"))
        self.assertTrue(solve("()[]{}"))
        self.assertFalse(solve("(]"))
        self.assertFalse(solve("([)]"))
        self.assertFalse(solve("("))


if __name__ == "__main__":
    unittest.main()
