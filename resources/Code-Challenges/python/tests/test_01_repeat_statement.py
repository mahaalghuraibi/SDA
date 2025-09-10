import unittest
from PY_code_challenges import c01_repeat_statement

if __name__ == "__main__":
    unittest.main()


class TestRepeatStatement(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Repeat once
    # Repeating "Hello" 1 time should return exactly "Hello".
    # -----------------------------------------------------------------
    def test_repeat_once(self):
        result = c01_repeat_statement.repeat_statement("Hello", 1)
        self.assertEqual(result, "Hello")

    # -----------------------------------------------------------------
    # Test 2: Repeat multiple times
    # Repeating "Hi" 3 times should return it on 3 separate lines.
    # -----------------------------------------------------------------
    def test_repeat_multiple_times(self):
        result = c01_repeat_statement.repeat_statement("Hi", 3)
        self.assertEqual(result, "Hi\nHi\nHi")

    # -----------------------------------------------------------------
    # Test 3: Empty string input
    # Repeating an empty string should just return empty lines.
    # -----------------------------------------------------------------
    def test_repeat_empty_string(self):
        result = c01_repeat_statement.repeat_statement("", 3)
        self.assertEqual(result, "\n\n")  # 3 empty lines → 2 newline separators

    # -----------------------------------------------------------------
    # Test 4: Repeat zero times
    # Repeating anything 0 times should return an empty string.
    # -----------------------------------------------------------------
    def test_repeat_zero_times(self):
        result = c01_repeat_statement.repeat_statement("Hello", 0)
        self.assertEqual(result, "")

    # -----------------------------------------------------------------
    # Test 5: Longer statement
    # Works with multi-word statements.
    # -----------------------------------------------------------------
    def test_repeat_long_statement(self):
        result = c01_repeat_statement.repeat_statement("Hello there", 2)
        self.assertEqual(result, "Hello there\nHello there")
