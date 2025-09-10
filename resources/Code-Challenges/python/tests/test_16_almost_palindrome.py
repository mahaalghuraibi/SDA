import unittest
from PY_code_challenges import c16_almost_palindrome

if __name__ == "__main__":
    unittest.main()


class TestAlmostPalindrome(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Regular palindrome
    # "racecar" reads the same forwards and backwards
    # -----------------------------------------------------------------
    def test_regular_palindrome(self):
        s = "racecar"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 2: Almost palindrome (remove one character)
    # "abca" -> remove 'c' -> "aba"
    # -----------------------------------------------------------------
    def test_almost_palindrome_one_removal(self):
        s = "abca"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 3: Non-palindrome
    # "hello" cannot become a palindrome by removing just one character
    # -----------------------------------------------------------------
    def test_non_palindrome(self):
        s = "hello"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertFalse(result)

    # -----------------------------------------------------------------
    # Test 4: Palindrome with spaces and punctuation
    # "A man, a plan, a canal, Panama" -> should return True
    # -----------------------------------------------------------------
    def test_palindrome_with_punctuation(self):
        s = "A man, a plan, a canal, Panama"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 5: Empty string
    # An empty string is trivially a palindrome
    # -----------------------------------------------------------------
    def test_empty_string(self):
        s = ""
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 6: Single character
    # Single characters are palindromes
    # -----------------------------------------------------------------
    def test_single_character(self):
        s = "x"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)

    # -----------------------------------------------------------------
    # Test 7: Almost palindrome with spaces
    # "deifiedx" -> remove 'x' -> "deified"
    # -----------------------------------------------------------------
    def test_almost_palindrome_with_extra_char(self):
        s = "deifiedx"
        result = c16_almost_palindrome.almost_palindrome(s)
        self.assertTrue(result)
