import unittest
from PY_code_challenges import c20_compress_string

if __name__ == "__main__":
    unittest.main()


class TestCompressString(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Standard compression
    # Consecutive repeated characters should be compressed
    # -----------------------------------------------------------------
    def test_standard_compression(self):
        input_str = "aaabbc"
        expected = "a3b2c"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 2: No repeated characters
    # String should remain unchanged
    # -----------------------------------------------------------------
    def test_no_repeats(self):
        input_str = "abcd"
        expected = "abcd"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 3: Mix of letters and symbols
    # Ensure digits and symbols are preserved and compressed correctly
    # -----------------------------------------------------------------
    def test_letters_and_symbols(self):
        input_str = "!!@@@###$$$"
        expected = "!2@3#3$3"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 4: Empty string
    # Should return empty string
    # -----------------------------------------------------------------
    def test_empty_string(self):
        input_str = ""
        expected = ""
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 5: Single-character string
    # Should remain unchanged
    # -----------------------------------------------------------------
    def test_single_character(self):
        input_str = "x"
        expected = "x"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 6: Longer mixed string
    # Multiple groups of repeated characters
    # -----------------------------------------------------------------
    def test_longer_mixed_string(self):
        input_str = "wwwwaaadexxxxx"
        expected = "w4a3dex5"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)

    # -----------------------------------------------------------------
    # Test 7: Case sensitivity
    # 'a' and 'A' should be treated differently
    # -----------------------------------------------------------------
    def test_case_sensitivity(self):
        input_str = "aaAAa"
        expected = "a2A2a"
        result = c20_compress_string.compress_string(input_str)
        self.assertEqual(result, expected)
