import unittest
from lab6.calculator import Calculator

class TestMultiplication(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(-1, -1), 1)
        self.assertEqual(self.calculator.multiplication(-1, 1), -1)
        self.assertEqual(self.calculator.multiplication(0, 5), 0)

if __name__ == '__main__':
    unittest.main()