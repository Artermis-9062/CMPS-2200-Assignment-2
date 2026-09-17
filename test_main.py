from main import subquadratic_multiply
from main import BinaryNumber
from sqlite3 import Binary
from main import quadratic_multiply
from main import *

# Feel free to expand and add your own tests here.
# Doing so won't impact the gradescope autograder tests (gradescope uses
# its own copy of this file so any changes you make here won't affect it).

# 5 pts
def test_quadratic_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(6)) == 5*6
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(2)) == 8*2

# 5 pts
def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(3)) == 4*3
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(6)) == 3*6