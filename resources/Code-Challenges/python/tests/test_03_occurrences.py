import unittest
from PY_code_challenges import c03_occurrences

if __name__ == "__main__":
    unittest.main()

class TestOccurrences(unittest.TestCase):
    def test_occurrences_01(self):
        # Example: count single letter
        result = c03_occurrences.occurrences("fleep floop", "e")
        self.assertEqual(result, 2)

    def test_occurrences_02(self):
        # Example: count another letter
        result = c03_occurrences.occurrences("fleep floop", "p")
        self.assertEqual(result, 2)

    def test_occurrences_03(self):
        # Example: count substring
        result = c03_occurrences.occurrences("fleep floop", "ee")
        self.assertEqual(result, 1)

    def test_occurrences_04(self):
        # Example: substring not present
        result = c03_occurrences.occurrences("fleep floop", "fe")
        self.assertEqual(result, 0)

    def test_occurrences_05(self):
        # Edge case: empty substring
        result = c03_occurrences.occurrences("fleep floop", "")
        self.assertEqual(result, 0)

    def test_occurrences_06(self):
        # Edge case: empty string
        result = c03_occurrences.occurrences("", "a")
        self.assertEqual(result, 0)
