import unittest
from lab6.calculator import Calculator

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -1), -2)
        self.assertEqual(self.calculator.addition(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()