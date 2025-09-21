# write your tests here
import unittest
from src import lab  


class TestLab(unittest.TestCase):

    # 1. Vowel Counter
    def test_count_vowels(self):
        self.assertEqual(lab.count_vowels("azcbobobegghakl"), 5)
        self.assertEqual(lab.count_vowels("AEiou"), 5)  
        self.assertEqual(lab.count_vowels("xyz"), 0)

    # 2. Occurrences of 'bob'
    def test_count_bob_occurrences(self):
        self.assertEqual(lab.count_bob_occurrences("azcbobobegghakl"), 2)
        self.assertEqual(lab.count_bob_occurrences("bobob"), 2)
        self.assertEqual(lab.count_bob_occurrences("hello"), 0)

    # 3. String Reversal
    def test_reverse_string(self):
        self.assertEqual(lab.reverse_string("Programming in Python"), "nohtyP ni gnimmargorP")
        self.assertEqual(lab.reverse_string(""), "")

    # 4. Letter Case Counter
    def test_count_case(self):
        self.assertEqual(lab.count_case("Hello World"), (2, 9))  
        self.assertEqual(lab.count_case("aA bB"), (2, 3))

    # 5. Alphabetical Sorting of Words
    def test_sort_words(self):
        self.assertEqual(
            lab.sort_words("without, hello, bag, world"),
            "bag, hello, without, world"
        )
        self.assertEqual(
            lab.sort_words("  zed ,   alpha,  mike "),
            "alpha, mike, zed"
        )
        self.assertEqual(lab.sort_words("only"), "only")

    # 6. Palindrome Checker
    def test_is_palindrome(self):
        self.assertTrue(lab.is_palindrome("madam"))
        self.assertFalse(lab.is_palindrome("maha"))
        self.assertTrue(lab.is_palindrome("RaceCar"))  


if __name__ == "__main__":
    unittest.main()
