import unittest
from src import add

class TestAdd(unittest.TestCase):

    def test_add_positive_num(self):
        self.assertEqual(add.addition(1,5), 6)

    def test_add_negative_num(self):
        self.assertEqual(add.addition(-5,-4), -9)

if __name__ == '__main__':
    unittest.main()