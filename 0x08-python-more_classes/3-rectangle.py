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

    def area(self):
        """
        returns area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Return the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
