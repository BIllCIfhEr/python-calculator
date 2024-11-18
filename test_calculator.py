import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 6), 11)
    def test_add2(self):
        self.assertEqual(self.calc.add(6, -9), -3)
    def test_add3(self):
        self.assertEqual(self.calc.add(-3, -8), -11)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(8, -7), 15)
    def test_subtract3(self):
        self.assertEqual(self.calc.subtract(-7, -9), 2)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(8, 3), 24)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(6, -3), -18)
    def test_multiply3(self):
        self.assertEqual(self.calc.multiply(-3, -10), 30)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 3), 3)
    def test_divide2(self):
         self.assertEqual(self.calc.divide(16, -8), -2)
    def test_divide3(self):
        self.assertEqual(self.calc.divide(-7, -7), 1)
    def test_divide4(self):
        self.assertEqual(self.calc.divide(81, 9), 9)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, -4), -2)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    def test_modulo3(self):
        self.assertEqual(self.calc.modulo(10, 6), 4)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()