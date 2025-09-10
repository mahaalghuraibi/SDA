import unittest
from PY_code_challenges import c10_last_two

if __name__ == "__main__":
    unittest.main()


class TestLastTwo(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Standard list with more than two items
    # Checks that the function correctly returns the last two items.
    # Example: ["banana", "peanut butter", "jelly", "bread", "pizza"] -> ["bread", "pizza"]
    # -----------------------------------------------------------------
    def test_last_two_standard(self):
        foods = ["banana", "peanut butter", "jelly", "bread", "pizza"]
        result = c10_last_two.last_two(foods)
        self.assertEqual(result, ["bread", "pizza"])

    # -----------------------------------------------------------------
    # Test 2: List with exactly two items
    # Should return both items without error.
    # Example: ["apple", "orange"] -> ["apple", "orange"]
    # -----------------------------------------------------------------
    def test_last_two_two_items(self):
        foods = ["apple", "orange"]
        result = c10_last_two.last_two(foods)
        self.assertEqual(result, ["apple", "orange"])

    # -----------------------------------------------------------------
    # Test 3: List with a single item
    # Should return a list containing just that one item.
    # Example: ["tomatoes"] -> ["tomatoes"]
    # -----------------------------------------------------------------
    def test_last_two_single_item(self):
        foods = ["tomatoes"]
        result = c10_last_two.last_two(foods)
        self.assertEqual(result, ["tomatoes"])

    # -----------------------------------------------------------------
    # Test 4: Empty list
    # Should return an empty list if no foods are provided.
    # -----------------------------------------------------------------
    def test_last_two_empty_list(self):
        foods = []
        result = c10_last_two.last_two(foods)
        self.assertEqual(result, [])

    # -----------------------------------------------------------------
    # Test 5: List with multiple identical items
    # Should still correctly return the last two items, even if they are the same.
    # Example: ["bread", "bread", "bread"] -> ["bread", "bread"]
    # -----------------------------------------------------------------
    def test_last_two_identical_items(self):
        foods = ["bread", "bread", "bread"]
        result = c10_last_two.last_two(foods)
        self.assertEqual(result, ["bread", "bread"])
