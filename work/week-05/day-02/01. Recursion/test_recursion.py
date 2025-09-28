import unittest
import recursion

class TestFunctions(unittest.TestCase):
    def test_length_of_string(self):
        self.assertEqual(recursion.length_of_string("hello"), 5)
        self.assertEqual(recursion.length_of_string(""), 0)
        self.assertEqual(recursion.length_of_string("a"), 1)
        self.assertEqual(recursion.length_of_string("test string"), 11)
    
    def test_sum_of_array(self):
        self.assertEqual(recursion.sum_of_array([1, 2, 3, 4, 5]), 15)
        self.assertEqual(recursion.sum_of_array([]), 0)
        self.assertEqual(recursion.sum_of_array([10, -10, 20]), 20)
        self.assertEqual(recursion.sum_of_array([5]), 5)

    def test_find_max(self):
        self.assertEqual(recursion.find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(recursion.find_max([-1, -5, -3, -9, -2]), -1)
        self.assertEqual(recursion.find_max([]), None)
    
    def test_fibonacci(self):
        self.assertEqual(recursion.fibonacci(0), 0)
        self.assertEqual(recursion.fibonacci(1), 1)
        self.assertEqual(recursion.fibonacci(5), 5)
        self.assertEqual(recursion.fibonacci(7), 13)
        self.assertEqual(recursion.fibonacci(-1), None)
    
    def test_coin_flips(self):
        self.assertEqual(recursion.coin_flips(1), ['T', 'H'])
        self.assertEqual(recursion.coin_flips(2), ['TT', 'TH', 'HT', 'HH'])
        self.assertEqual(recursion.coin_flips(3), ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH'])
        self.assertEqual(recursion.coin_flips(0), None)
    
    def test_letter_combinations(self):
        self.assertEqual(set(recursion.letter_combinations(['a', 'b', 'c'])), 
                         set(["a","b","c","ab","ac","ba","bc","ca","cb","abc","acb","bac","bca","cab","cba"]))
        self.assertEqual(recursion.letter_combinations([]), [])

    def test_flatten(self):
        self.assertEqual(recursion.flatten([]), [])
        self.assertEqual(recursion.flatten([1, 2, 3]), [1, 2, 3])
        self.assertEqual(recursion.flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(recursion.flatten([[1, [2, [3, [4, [5]]]]]]), [1, 2, 3, 4, 5])
        self.assertEqual(recursion.flatten([1, "a", [2, ["b", 3]]]), [1, "a", 2, "b", 3])
        self.assertEqual(recursion.flatten([[], [1, [], [2, []], 3], []]), [1, 2, 3])
        self.assertEqual(recursion.flatten([1, 2, 3, [4, 5, [6, 7, 8, [9, 10], 11, 12, 13], 14, 15], 16, 17, 18]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

if __name__ == '__main__':
    unittest.main()