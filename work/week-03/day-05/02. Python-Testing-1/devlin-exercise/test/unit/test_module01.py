# test/unit/test_module01.py
import unittest


class TestClass01(unittest.TestCase):
    def test_case_01(self):
        my_name_str = "Suresh Sigera "
        my_int = 1000
        self.assertTrue(isinstance(my_name_str, str))
        self.assertTrue(isinstance(my_int, int))

    def test_case_02(self):
        my_pi = 3.14
        self.assertFalse(isinstance(my_pi, int))

if __name__ == '__main__':
    unittest.main()
