"""
Karatsuba Multiplication Algorithm:

The Karatsuba algorithm is a fast multiplication algorithm that multiplies two numbers in a more efficient manner
than the standard long multiplication method. It achieves this by recursively breaking down the multiplication 
process into smaller subproblems and combining the results using a formula that reduces the number of 
multiplication operations needed.

Steps:
1. Split the given numbers into two halves at the middle.
2. Recursively compute the products of these halves.
3. Combine the results using Karatsuba's formula.

Steps(Mathematically):
let x and y be an n-digit string of numbers with base B
we can rewrite any positive interger m less than n

x= x1B^(m)+x0
y= y1B^(m)+y0

where x*y= z2B^(2m)+z1B^(m)+z0

where
z2=x1y1
z1=x1y0+x0y1
z0=x0y0

where
z3= (x1+x0)(y0+y1)
z1= z3-z2-z0

The algorithm reduces the number of recursive calls by exploiting properties of multiplication and uses 
addition and subtraction to compute the final result.

Reference: https://en.wikipedia.org/wiki/Karatsuba_algorithm, https://youtu.be/JCbZayFr9RE?list=PLEGCF-WLh2RLHqXx6-GZr_w7LgqKDXxN_
"""

class _Multiply():
    def __init__(self, _number1=None, _number2=None):
        self.number1 = _number1
        self.number2 = _number2
        
    def _size_base10(self, _num):
        if _num == 0:
            return 1  # Special case for zero
        size = 0
        while _num != 0:
            size += 1
            _num //= 10  # Integer division by 10 to remove the least significant digit
        return size
    
    def _split_at(self, _num, _length):
        _mid = _length//2
        if _length % 2 == 0:  # If the number has an even number of digits
            first_part = _num // (10 ** _mid)
            second_part = _num % (10 ** _mid)
        else:  # If the number has an odd number of digits
            first_part = _num // (10 ** (_mid + 1))
            second_part = _num % (10 ** _mid)
        return first_part, second_part
        
    def _Karatsuba_Method(self, _number1, _number2): #Algorithm with O(n^log_{2}3) by Karatsuba
        if _number1 < 10 or _number2 < 10:
            return _number1 * _number2

        # Calculates the size of the numbers.
        _size_num1 = self._size_base10(_number1)
        _size_num2 = self._size_base10(_number2)
        m = max(_size_num1, _size_num2)
        m2 = m // 2
        high1, low1 = self._split_at(_number1, m)
        high2, low2 = self._split_at(_number2, m)

        z0 = self._Karatsuba_Method(low1, low2)
        z1 = self._Karatsuba_Method((low1 + high1), (low2 + high2))
        z2 = self._Karatsuba_Method(high1, high2)
        result = (z2 * 10**(m2 * 2)) + ((z1 - z2 - z0) * 10**m2) + z0
        return result

multiply = _Multiply()
k = multiply._Karatsuba_Method(1234, 5678)
print(k)
