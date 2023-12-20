# Import the _Multiply class from the file containing the implementation
from Multiplication_Algorithms_2Numbers import KaratsubaMultiply
import unittest


class TestKaratsubaMultiply(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(KaratsubaMultiply.karatsuba(12, 13), 12*13)
        self.assertEqual(KaratsubaMultiply.karatsuba(25, 35), 25*35)

    def test_large_numbers(self):
        x = 3141592653589793238462643383279
        y = 271828182845904523536028747135       
        expected = x * y  
        result = KaratsubaMultiply.karatsuba(x, y)
        self.assertEqual(expected, result)

    def test_invalid_input(self):
        self.assertRaises(ValueError, KaratsubaMultiply.karatsuba, 10.5, 12)
        self.assertRaises(ValueError, KaratsubaMultiply.karatsuba, '10', 12)

    def test_max_depth(self):
        # Pick two large numbers that require max depth + 1
        x = 2**1000  
        y = 2**1000  
        self.assertEqual(KaratsubaMultiply.karatsuba(x, y), x * y)

if __name__ == '__main__':
    unittest.main()
