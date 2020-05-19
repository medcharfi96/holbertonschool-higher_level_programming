#!/usr/bin/python3
"""
definir la class Square
"""


class Square:
    """la classe square"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return the area of the square"""
        return (pow(self.__size, 2))

    @property
    def size(self):
        """ the func get for size"""
        return self.__size	

    @size.setter
    def size(self, value):
        """ the function set of the size """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
