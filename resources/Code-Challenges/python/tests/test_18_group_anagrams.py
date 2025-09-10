import unittest
from PY_code_challenges import c18_group_anagrams

if __name__ == "__main__":
    unittest.main()


class TestGroupAnagrams(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Standard example
    # Multiple groups of anagrams
    # -----------------------------------------------------------------
    def test_standard_example(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_groups = [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]
        result = c18_group_anagrams.group_anagrams(words)
        # Sort inner lists and outer list for comparison
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected_groups])
        self.assertEqual(sorted_result, sorted_expected)

    # -----------------------------------------------------------------
    # Test 2: Single word input
    # Should return a list containing a single group with that word
    # -----------------------------------------------------------------
    def test_single_word(self):
        words = ["hello"]
        expected_groups = [["hello"]]
        result = c18_group_anagrams.group_anagrams(words)
        self.assertEqual(result, expected_groups)

    # -----------------------------------------------------------------
    # Test 3: Empty list input
    # Should return an empty list
    # -----------------------------------------------------------------
    def test_empty_list(self):
        words = []
        expected_groups = []
        result = c18_group_anagrams.group_anagrams(words)
        self.assertEqual(result, expected_groups)

    # -----------------------------------------------------------------
    # Test 4: Duplicate words
    # ["bat", "tab", "bat"] -> "bat" and "tab" are anagrams, duplicates allowed
    # -----------------------------------------------------------------
    def test_duplicates(self):
        words = ["bat", "tab", "bat"]
        expected_groups = [["bat", "tab", "bat"]]
        sorted_result = sorted([sorted(group) for group in c18_group_anagrams.group_anagrams(words)])
        sorted_expected = sorted([sorted(group) for group in expected_groups])
        self.assertEqual(sorted_result, sorted_expected)

    # -----------------------------------------------------------------
    # Test 5: All words the same
    # ["cat", "cat", "cat"] -> single group with all words
    # -----------------------------------------------------------------
    def test_all_same_words(self):
        words = ["cat", "cat", "cat"]
        expected_groups = [["cat", "cat", "cat"]]
        result = c18_group_anagrams.group_anagrams(words)
        self.assertEqual(result, expected_groups)

    # -----------------------------------------------------------------
    # Test 6: Words with no anagrams
    # Each word should be its own group
    # -----------------------------------------------------------------
    def test_no_anagrams(self):
        words = ["one", "two", "three"]
        expected_groups = [["one"], ["two"], ["three"]]
        sorted_result = sorted([sorted(group) for group in c18_group_anagrams.group_anagrams(words)])
        sorted_expected = sorted([sorted(group) for group in expected_groups])
        self.assertEqual(sorted_result, sorted_expected)
