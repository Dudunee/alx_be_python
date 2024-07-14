import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleCalculator()
        result = calc.add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        calc = SimpleCalculator()
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        calc = SimpleCalculator()
        result = calc.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        calc = SimpleCalculator()
        
        # Test normal division
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            calc.divide(8, 0)

if __name__ == "__main__":
    unittest.main()


