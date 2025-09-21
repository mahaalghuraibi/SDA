import unittest
from src import calculator

class TddInPythonExample(unittest.TestCase):

    def test_calculator_add_method_returns_correct_result(self):
        calc = calculator.Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)

if __name__ == '__main__':
    unittest.main()