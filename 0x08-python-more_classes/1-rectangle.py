#!/usr/bin/python3

"""
module 0
"""


class Rectangle:
    """
    empty rectangle class
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        width getter
        """

        return self.__width
    @width.setter
    def width(self, width):
        """
        width setter
        """
        
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = width


    @property
    def height(self):
        """
        height getter
        """

        return self.__height
    @height.setter
    def height(self, height):
        """
        height setter
        """

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
