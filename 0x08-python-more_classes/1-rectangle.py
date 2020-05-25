#!/usr/bin/python3
"""
class Rectangle
"""


class Rectangle:
    """Define rectangle class
    Attributes:
        width: int
        height: int
    """
    def __init__(self, width=0, height=0):
        """constructeur parametré"""
        self.width = width
        self.height = height

    @proprety
    def width(self):
        """ the width get """
        return self.__width

    @widthsetter
    def width(self, value):
        """ the width set """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @proprety
    def height(self):
        """ the height get """
        return self.__height

    @heightsetter
    def height(self, value):
        """ the height set """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
