#!/usr/bin/python3
"""
module
"""


def is_integer_num(n):

    """
    checks if a number is a float or an int
    """
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return True


def add_integer(a, b=98):

    """
    adds integers
    """
    if not is_integer_num(a):
        raise TypeError("a must be an integer")
    if not is_integer_num(b):
        raise TypeError("b must be an integer")
    
    result = int(a) + int(b)
    return result

