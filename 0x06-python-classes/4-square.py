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
        """
        initialise class with size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        gets the size of a square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        set the size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns area
        """
        return self.__size ** 2
