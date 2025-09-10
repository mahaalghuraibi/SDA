import unittest
from PY_code_challenges import c02_sum_to

if __name__ == "__main__":
    unittest.main()


class TestSumTo(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Small number
    # The sum of numbers from 1 to 6 is 21 (1+2+3+4+5+6).
    # -----------------------------------------------------------------
    def test_sum_to_small(self):
        result = c02_sum_to.sum_to(6)
        self.assertEqual(result, 21)

    # -----------------------------------------------------------------
    # Test 2: Larger number
    # The sum of numbers from 1 to 10 is 55.
    # -----------------------------------------------------------------
    def test_sum_to_large(self):
        result = c02_sum_to.sum_to(10)
        self.assertEqual(result, 55)

    # -----------------------------------------------------------------
    # Test 3: Edge case n = 1
    # The sum from 1 to 1 is just 1.
    # -----------------------------------------------------------------
    def test_sum_to_one(self):
        result = c02_sum_to.sum_to(1)
        self.assertEqual(result, 1)

    # -----------------------------------------------------------------
    # Test 4: Edge case n = 0
    # The sum from 1 to 0 should return 0 (nothing to add).
    # -----------------------------------------------------------------
    def test_sum_to_zero(self):
        result = c02_sum_to.sum_to(0)
        self.assertEqual(result, 0)

    # -----------------------------------------------------------------
    # Test 5: Edge case negative number
    # By definition in this challenge, negative inputs should return 0
    # because you cannot sum from 1 to a negative number.
    # -----------------------------------------------------------------
    def test_sum_to_negative(self):
        result = c02_sum_to.sum_to(-5)
        self.assertEqual(result, 0)

    # -----------------------------------------------------------------
    # Test 6: Large input
    # The sum from 1 to 100 should be 5050 (classic formula check).
    # -----------------------------------------------------------------
    def test_sum_to_100(self):
        result = c02_sum_to.sum_to(100)
        self.assertEqual(result, 5050)
