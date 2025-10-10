import unittest
import sys
import os

# Add the parent directory to the sys.path to allow imports from math_lib
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_lib.factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_of_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_of_non_integer(self):
        with self.assertRaises(ValueError):
            factorial(1.5)
        with self.assertRaises(ValueError):
            factorial("a")

if __name__ == '__main__':
    unittest.main()