import unittest

from solution import solve


class TemplateTests(unittest.TestCase):
    def test_trim_input(self) -> None:
        self.assertEqual(solve("  abc  \n"), "abc")


if __name__ == "__main__":
    unittest.main()

