#!/usr/bin/python3

"""
1. My first square
    Contains an empty class that defines a square
"""


class Square:
    """
    base class
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
