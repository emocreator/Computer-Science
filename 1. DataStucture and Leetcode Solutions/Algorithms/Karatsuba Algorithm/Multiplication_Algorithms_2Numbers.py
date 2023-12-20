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
import math 

class KaratsubaMultiply:

    @staticmethod
    def karatsuba(x, y):
        # Validate inputs are integers
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Inputs must be integers")
        
        # Base case    
        if x < 10 or y < 10:
            return x*y  
        
        # Maximum recursion depth 
        if KaratsubaMultiply.max_depth_reached(KaratsubaMultiply.rdepth): 
            return x * y
        
        # Calculate size 
        n = max(len(str(x)),len(str(y))) 
        KaratsubaMultiply.rdepth += 1
        
        # Split numbers  
        nby2 = n // 2
        a, b = KaratsubaMultiply.split_number(x, nby2)
        c, d = KaratsubaMultiply.split_number(y, nby2)
        
        # Recursive calls 
        ac = KaratsubaMultiply.karatsuba(a,c)  
        bd = KaratsubaMultiply.karatsuba(b,d)
        ad_plus_bc = KaratsubaMultiply.karatsuba(a+b, c+d) - ac - bd
        
        # Combine results
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd    
        
        KaratsubaMultiply.rdepth -= 1
        
        return prod

    @staticmethod
    def split_number(x, n):    
        # Splits x into two halves 
        return x // 10**n, x % 10**n
    
    @staticmethod 
    def int_to_str(x):
        # Convert int to string to manipulate digits
        return str(x)
    
    @staticmethod 
    def str_to_int(x):
       # Convert string back to int
       return int(x)
       
    @staticmethod
    def max_depth_reached(d):
         # Detect recursion depth limit 
         return d >= 1000  
         
    # Static var to track recursion depth
    rdepth = 0
        
if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592  
    y = 2718281828459045235360287471352662497757247093699959574966967627

    print(KaratsubaMultiply.karatsuba(x,y))
