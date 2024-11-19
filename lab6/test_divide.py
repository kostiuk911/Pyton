import unittest
from lab6.calculator import Calculator

class TestDivision(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_divide(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(-6, -3), 2)
        self.assertEqual(self.calculator.division(-6, 3), -2)
        self.assertEqual(self.calculator.division(0, 1), 0)

if __name__ == '__main__':
    unittest.main()