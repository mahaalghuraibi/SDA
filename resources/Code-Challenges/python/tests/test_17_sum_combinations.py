import unittest
from PY_code_challenges import c17_sum_combinations

if __name__ == "__main__":
    unittest.main()


class TestSumCombinations(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Single number matches target
    # Only one combination exists
    # -----------------------------------------------------------------
    def test_single_number(self):
        numbers = [2, 3, 7]
        target = 7
        expected = [[7]]
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 2: Multiple combinations possible
    # Example: 2+3+3 and 3+5 both sum to 8
    # -----------------------------------------------------------------
    def test_multiple_combinations(self):
        numbers = [2, 3, 3, 5]
        target = 8
        # Depending on implementation, duplicates may or may not be allowed
        expected = [[3,5], [2,3,3]]
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(sorted(result), sorted(expected))

    # -----------------------------------------------------------------
    # Test 3: Multiple numbers sum to target, order irrelevant
    # -----------------------------------------------------------------
    def test_order_irrelevant(self):
        numbers = [2, 4, 6]
        target = 6
        expected = [[6], [2,4]]
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(sorted(result), sorted(expected))

    # -----------------------------------------------------------------
    # Test 4: No possible combination
    # Should return an empty list
    # -----------------------------------------------------------------
    def test_no_solution(self):
        numbers = [5, 10, 12]
        target = 7
        expected = []
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 5: Empty input list
    # Should return an empty list
    # -----------------------------------------------------------------
    def test_empty_list(self):
        numbers = []
        target = 5
        expected = []
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 6: Repeated numbers in input list
    # Make sure duplicates in input are handled correctly
    # -----------------------------------------------------------------
    def test_repeated_numbers(self):
        numbers = [2, 3, 2, 3]
        target = 5
        expected = [[2,3], [2,3]]  # may appear twice if allowed, otherwise deduplicate
        result = c17_sum_combinations.sum_combinations(numbers, target)
        self.assertEqual(sorted(result), sorted(expected))
