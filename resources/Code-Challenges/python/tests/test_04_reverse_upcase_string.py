import unittest
from PY_code_challenges import c04_reverse_upcase_string

if __name__ == "__main__":
    unittest.main()


class TestReverseString(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Simple lowercase input
    # "hello" reversed and uppercased should be "OLLEH".
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_01(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("hello")
        self.assertEqual(result, "OLLEH")

    # -----------------------------------------------------------------
    # Test 2: Input with underscore
    # "reverse_me" reversed and uppercased should be "EM_ESREVER".
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_02(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("reverse_me")
        self.assertEqual(result, "EM_ESREVER")

    # -----------------------------------------------------------------
    # Test 3: Multi-word input with space
    # "software engineer" reversed and uppercased should be "REENIGNE ERAWTFOS".
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_03(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("software engineer")
        self.assertEqual(result, "REENIGNE ERAWTFOS")

    # -----------------------------------------------------------------
    # Test 4: Empty string
    # An empty string should just return an empty string.
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_empty(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("")
        self.assertEqual(result, "")

    # -----------------------------------------------------------------
    # Test 5: Already uppercase input
    # "HELLO" reversed should still be "OLLEH".
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_already_uppercase(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("HELLO")
        self.assertEqual(result, "OLLEH")

    # -----------------------------------------------------------------
    # Test 6: Input with punctuation and numbers
    # "Python 3.9!" reversed and uppercased should be "!9.3 NOHTYP".
    # -----------------------------------------------------------------
    def test_reverse_upcase_string_punctuation(self):
        result = c04_reverse_upcase_string.reverse_upcase_string("Python 3.9!")
        self.assertEqual(result, "!9.3 NOHTYP")
