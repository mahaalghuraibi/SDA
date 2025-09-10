import unittest
from PY_code_challenges import c05_multiply_by

if __name__ == "__main__":
    unittest.main()


class TestMultiplyBy(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Empty list input
    # Multiplying an empty list should always return an empty list.
    # -----------------------------------------------------------------
    def test_multiply_by_empty_list(self):
        result = c05_multiply_by.multiply_by([], 5)
        self.assertEqual(result, [])

    # -----------------------------------------------------------------
    # Test 2: Single element in the list
    # Multiplying a one-item list should just return that element * factor.
    # -----------------------------------------------------------------
    def test_multiply_by_single_element(self):
        result = c05_multiply_by.multiply_by([2], 10)
        self.assertEqual(result, [20])

    # -----------------------------------------------------------------
    # Test 3: Multiple elements in the list
    # Each number in the list should be multiplied individually.
    # -----------------------------------------------------------------
    def test_multiply_by_multiple_elements(self):
        result = c05_multiply_by.multiply_by([1, 2, 3], 2)
        self.assertEqual(result, [2, 4, 6])

    # -----------------------------------------------------------------
    # Test 4: Negative numbers and factors
    # Function should correctly handle both positive and negative values.
    # -----------------------------------------------------------------
    def test_multiply_by_negative(self):
        result = c05_multiply_by.multiply_by([3, -1, 4], -2)
        self.assertEqual(result, [-6, 2, -8])

    # -----------------------------------------------------------------
    # Test 5: Factor of zero
    # Any number multiplied by zero should return zero.
    # -----------------------------------------------------------------
    def test_multiply_by_zero(self):
        result = c05_multiply_by.multiply_by([5, 10, 15], 0)
        self.assertEqual(result, [0, 0, 0])

    # -----------------------------------------------------------------
    # Test 6: Factor of one
    # Multiplying by 1 should return the list unchanged.
    # -----------------------------------------------------------------
    def test_multiply_by_one(self):
        result = c05_multiply_by.multiply_by([7, 8, 9], 1)
        self.assertEqual(result, [7, 8, 9])

    # -----------------------------------------------------------------
    # Test 7: Large numbers
    # Ensures the function handles large integer multiplication properly.
    # -----------------------------------------------------------------
    def test_multiply_by_large_numbers(self):
        result = c05_multiply_by.multiply_by([1000000, 2000000], 1000)
        self.assertEqual(result, [1000000000, 2000000000])
