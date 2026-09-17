"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
Name: Chuong Hoang Pham
"""
from typing import List
import time
import random
from tabulate import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# ------------------------------Binary Helper Function----------------------------------#

# Helper Function: Add Binary
def binary_add(x: str, y: str) -> str:

    x = x[::-1]
    y = y[::-1]
    result = []
    carry = 0
    i = 0

    while i < len(x) or i < len(y) or carry:
        total = carry
        if i < len(x):
            total += int(x[i])
        if i < len(y):
            total += int(y[i])
        
        result.append(str(total % 2))
        carry = total // 2
        i += 1

    return "".join(result[::-1])

# Helper Function: Subtract Binary
def binary_subtract(x: str, y: str) -> str:
    x = x[::-1]
    y = y[::-1]
    result = []
    borrow = 0
    i = 0

    while i < len(x) or i < len(y) or borrow:
        total = borrow
        if i < len(x):
            total += int(x[i])
        if i < len(y):
            total -= int(y[i])
        
        if total < 0:
            total += 2
            borrow = -1
        else:
            borrow = 0
        
        result.append(str(total))
        i += 1

    return "".join(result[::-1])


#-----------------------Quadratic Multiply-----------------------------------------#
def quadratic_multiply(x, y):
    ### TODO
    binary_str =  _quadratic_multiply(x.binary_vec, y.binary_vec, max(len(x.binary_vec), len(y.binary_vec)))
    return int(binary_str, 2)

# Helper function which do the multiplication recursively and return the result in string.
def _quadratic_multiply(x: List, y: List, n: int) -> str: 

    # Base case: 
    if (len(x) == 1 and len(y) == 1):
        return str(int(x[0]) * int(y[0]))
    # Check if 2 numbers have the same length?
    longest_length = max(len(x), len(y))
    
    if(longest_length % 2 != 0):
        longest_length += 1
    
    # padding with leading zero
    x = abs(len(x) - longest_length) * ['0'] + x
    y = abs(len(y) - longest_length) * ['0'] + y

    # Split x into half
    x_left = x[:longest_length//2]
    x_right = x[longest_length//2:]

    # Split y into half
    y_left = y[:longest_length//2]
    y_right = y[longest_length//2:]
    
    # Calculate left, right term recursively
    left_product = _quadratic_multiply(x_left, y_left, max(len(x_left), len(y_left)))
    right_product = _quadratic_multiply(x_right, y_right, max(len(x_right), len(y_right)))
    
    # Calculate the middle term
    first_mid_product = _quadratic_multiply(x_left, y_right, max(len(x_left), len(y_right)))
    second_mid_product = _quadratic_multiply(x_right, y_left, max(len(x_right), len(y_left)))
    mid_product = binary_add(first_mid_product, second_mid_product)

    # Add up all terms
    res = binary_add(left_product + '0'*longest_length, mid_product + '0'*(longest_length//2))
    res = binary_add(res, right_product)

    return res
    

#-----------------------Subquadratic_multiply-----------------------------------------#
def subquadratic_multiply(x, y):
    ### TODO

    binary_str = _subquadratic_multiply(x.binary_vec, y.binary_vec, max(len(x.binary_vec), len(y.binary_vec)))
    return int(binary_str, 2)
    ###

# Helper function: Calculate subquadratic_multiply recursively
def _subquadratic_multiply(x: List, y: List, n: int) -> str:
    
    # Base case: 
    if (len(x) == 1 and len(y) == 1):
        return str(int(x[0]) * int(y[0]))
    # Check if 2 numbers have the same length?
    longest_length = max(len(x), len(y))
    
    if(longest_length % 2 != 0):
        longest_length += 1
    
    # padding with leading zero
    x = abs(len(x) - longest_length) * ['0'] + x
    y = abs(len(y) - longest_length) * ['0'] + y

    # Split x into half
    x_left = x[:longest_length//2]
    x_right = x[longest_length//2:]

    # Split y into half
    y_left = y[:longest_length//2]
    y_right = y[longest_length//2:]
    
    # Calculate left, right term recursively
    left_product = _quadratic_multiply(x_left, y_left, max(len(x_left), len(y_left)))
    right_product = _quadratic_multiply(x_right, y_right, max(len(x_right), len(y_right)))

    # Calculate the mid term
    x_sum = list(binary_add(x_left, x_right)) # Must be list type
    y_sum = list(binary_add(y_left, y_right)) # Must be list type
    mid_product = _subquadratic_multiply(x_sum, y_sum, max(len(x_sum), len(y_sum)))

    # Subtract left and right product from the mid product
    mid_product = binary_subtract(mid_product, left_product)
    mid_product = binary_subtract(mid_product, right_product)
    
     # Add up all terms
    res = binary_add(left_product + '0'*longest_length, mid_product + '0'*(longest_length//2))
    res = binary_add(res, right_product)
    
    return res


#-----------------------Time & Compare Multiply-----------------------------------------#
def time_multiply(x, y, f):
    start = time.perf_counter()
    f(x, y)
    return (time.perf_counter() - start) * 1000
    
def compare_multiply():
    headers = ["Size (n)", "Quadratic (ms)", "Subquadratic (ms)"]
    sizes = [2, 4, 8, 16, 32, 64, 128, 256]
    data = []

    for i in sizes:
        A = BinaryNumber(random.getrandbits(i))
        B = BinaryNumber(random.getrandbits(i))
        
        quadratic_time = time_multiply(A, B, quadratic_multiply)
        subquadratic_time = time_multiply(A, B, subquadratic_multiply)
        data.append([i, quadratic_time, subquadratic_time])

    print(tabulate(data, headers=headers, tablefmt="github", floatfmt=".4f"))

compare_multiply()
