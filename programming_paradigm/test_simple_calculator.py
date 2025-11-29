import unittest
from simple_calculator import SimpleCalculator

class TestSimplecalculator(unittest.TestCase):
    def setUp(self):
        self.calc= SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(1,2), 3)
        self.assertEqual(self.calc.add(-1,2), 1)
        self.assertEqual(self.calc.add(1,0), 1)
        self.assertEqual(self.calc.add(7,2), 9)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1,2), -1)
        self.assertEqual(self.calc.subtract(5,2), 3)
        self.assertEqual(self.calc.subtract(1,0), 1)
        self.assertEqual(self.calc.subtract(7,2), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # --- Division Tests ---
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        # Test dividing zero by a number
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == "__main__":
    unittest.main()