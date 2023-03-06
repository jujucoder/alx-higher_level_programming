#!/usr/bin/python3

"""
1. My first square
    Contains an empty class that defines a square
"""


class Square:
    """
    base class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialise class with size
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        returns position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        sets position
        """
        if  len(position) != 2 or not \
                all(isinstance(x, int) and x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        returns area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square using #
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for i in range(0, self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print()
