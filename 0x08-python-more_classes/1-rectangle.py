#!/usr/bin/python3

"""
module 0
"""


class Rectangle:
    """
    empty rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be an integer")
        
        self.__width = width


    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be an integer")
        
        self.__height = height
