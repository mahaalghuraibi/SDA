import unittest
from PY_code_challenges import c08_sort_a_string

if __name__ == "__main__":
    unittest.main()

class TestSortAString(unittest.TestCase):
    def test_sort_a_string_01(self):
        # Edge case: empty string should stay empty
        result = c08_sort_a_string.sort_a_string("")
        self.assertEqual(result, "")

    def test_sort_a_string_02(self):
        # Simple case: already sorted string
        result = c08_sort_a_string.sort_a_string("abc")
        self.assertEqual(result, "abc")

    def test_sort_a_string_03(self):
        # Reverse order input
        result = c08_sort_a_string.sort_a_string("cba")
        self.assertEqual(result, "abc")

    def test_sort_a_string_04(self):
        # Mixed letters
        result = c08_sort_a_string.sort_a_string("hello")
        self.assertEqual(result, "ehllo")

    def test_sort_a_string_05(self):
        # Long complex case
        result = c08_sort_a_string.sort_a_string("supercalifragilisticexpialidocious")
        self.assertEqual(result, "aaacccdeefgiiiiiiillloopprrssstuux")