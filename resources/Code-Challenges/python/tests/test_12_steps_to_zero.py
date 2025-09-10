import unittest
from PY_code_challenges import c12_steps_to_zero

if __name__ == "__main__":
    unittest.main()


class TestStepsToZero(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Example from prompt
    # Input: 14
    # Step breakdown: 14 → 7 → 6 → 3 → 2 → 1 → 0
    # Total steps = 6
    # -----------------------------------------------------------------
    def test_steps_example(self):
        result = c12_steps_to_zero.steps_to_zero(14)
        self.assertEqual(result, 6)

    # -----------------------------------------------------------------
    # Test 2: Single odd number
    # Input: 1
    # Steps: 1 → 0
    # Total steps = 1
    # -----------------------------------------------------------------
    def test_steps_single_odd(self):
        result = c12_steps_to_zero.steps_to_zero(1)
        self.assertEqual(result, 1)

    # -----------------------------------------------------------------
    # Test 3: Single even number
    # Input: 8
    # Steps: 8 → 4 → 2 → 1 → 0
    # Total steps = 4
    # -----------------------------------------------------------------
    def test_steps_single_even(self):
        result = c12_steps_to_zero.steps_to_zero(8)
        self.assertEqual(result, 4)

    # -----------------------------------------------------------------
    # Test 4: Zero as input
    # Edge case: 0 is already zero, so steps = 0
    # -----------------------------------------------------------------
    def test_steps_zero(self):
        result = c12_steps_to_zero.steps_to_zero(0)
        self.assertEqual(result, 0)

    # -----------------------------------------------------------------
    # Test 5: Larger number
    # Input: 25
    # Steps: 25 → 24 → 12 → 6 → 3 → 2 → 1 → 0
    # Total steps = 7
    # -----------------------------------------------------------------
    def test_steps_larger_number(self):
        result = c12_steps_to_zero.steps_to_zero(25)
        self.assertEqual(result, 7)

    # -----------------------------------------------------------------
    # Test 6: Power of two
    # Input: 16
    # Steps: 16 → 8 → 4 → 2 → 1 → 0
    # Total steps = 5
    # -----------------------------------------------------------------
    def test_steps_power_of_two(self):
        result = c12_steps_to_zero.steps_to_zero(16)
        self.assertEqual(result, 5)
