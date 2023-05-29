import unittest

class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        result = 2 + 3
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = 2 * 3
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
