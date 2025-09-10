import unittest
from PY_code_challenges import c06_letter_count

if __name__ == "__main__":
    unittest.main()


class Test_Letter_Count(unittest.TestCase):
    # -----------------------------------------------------------------
    # Test 1: Phrase with spaces, repeating vowels, and consonants
    # "hello and goodbye"
    # Expect dictionary showing how many times each letter/space appears.
    # -----------------------------------------------------------------
    def test_letter_count_one(self):
        result = c06_letter_count.letter_count("hello and goodbye")
        self.assertEqual(result, { " ": 2, "h": 1, "e": 2, "l": 2, "o": 3, "a": 1, "n": 1, "d": 2, "g": 1, "y": 1, "b": 1 })

    # -----------------------------------------------------------------
    # Test 2: Sentence with 4 spaces and repeating "e"
    # "i hope you are well"
    # Verifies multiple spaces and multiple different vowels.
    # -----------------------------------------------------------------
    def test_letter_count_two(self):
        result = c06_letter_count.letter_count("i hope you are well")
        self.assertEqual(result, { " ": 4, "i": 1, "h": 1, "o": 2, "p": 1, "e": 3, "y": 1, "u": 1, "a": 1, "r": 1, "l": 2, "w": 1 })

    # -----------------------------------------------------------------
    # Test 3: Single word, no spaces
    # "excited"
    # Verifies the function handles compact input correctly.
    # -----------------------------------------------------------------
    def test_letter_count_three(self):
        result = c06_letter_count.letter_count("excited")
        self.assertEqual(result, { "e": 2, "x": 1, "c": 1, "i": 1, "t": 1, "d": 1 })

    # -----------------------------------------------------------------
    # Test 4: Phrase with spaces, repeated 'e', and some consonants
    # "leave me alone"
    # Verifies counting of multiple words and repeated letters.
    # -----------------------------------------------------------------
    def test_letter_count_four(self):
        result = c06_letter_count.letter_count("leave me alone")
        self.assertEqual(result, { " ": 2, "l": 2, "e": 4, "a": 2, "v": 1, "m": 1, "o": 1, "n": 1 })
