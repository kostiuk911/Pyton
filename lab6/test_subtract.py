import unittest
from lab6.calculator import Calculator

class TestSubtraction(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(-1, -1), 0)
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

if __name__ == '__main__':
    unittest.main()