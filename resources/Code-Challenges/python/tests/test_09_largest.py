import unittest
from PY_code_challenges import c09_largest

if __name__ == "__main__":
    unittest.main()


class TestLargest(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Small list of positive numbers
    # Checks basic functionality with a simple list.
    # Example: [1, 2, 3, 4, 0] -> largest is 4
    # -----------------------------------------------------------------
    def test_largest_simple(self):
        result = c09_largest.largest([1, 2, 3, 4, 0])
        self.assertEqual(result, 4)

    # -----------------------------------------------------------------
    # Test 2: Larger numbers
    # Tests with a list that has larger numbers to ensure correct max selection.
    # Example: [10, 4, 2, 231, 91, 54] -> largest is 231
    # -----------------------------------------------------------------
    def test_largest_larger_numbers(self):
        result = c09_largest.largest([10, 4, 2, 231, 91, 54])
        self.assertEqual(result, 231)

    # -----------------------------------------------------------------
    # Test 3: Negative numbers and zero
    # Verifies function works with negative numbers.
    # Example: [-5, -1, -10, 0] -> largest is 0
    # -----------------------------------------------------------------
    def test_largest_negative_numbers(self):
        result = c09_largest.largest([-5, -1, -10, 0])
        self.assertEqual(result, 0)

    # -----------------------------------------------------------------
    # Test 4: Single element list
    # The largest of a single-element list should be that element itself.
    # -----------------------------------------------------------------
    def test_largest_single_element(self):
        result = c09_largest.largest([42])
        self.assertEqual(result, 42)

    # -----------------------------------------------------------------
    # Test 5: All same numbers
    # Ensures function returns the correct value when all elements are equal.
    # Example: [7, 7, 7] -> largest is 7
    # -----------------------------------------------------------------
    def test_largest_all_equal(self):
        result = c09_largest.largest([7, 7, 7])
        self.assertEqual(result, 7)
