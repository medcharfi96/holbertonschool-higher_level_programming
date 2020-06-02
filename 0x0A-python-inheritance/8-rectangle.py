#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """class descr"""
    def area(self):
        """raise a exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ give the name and value """
        if type(name) is not str:
            raise TypeError("{:s} must be a string".format(name))
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """ fonction dinitialisation"""
        self.__height = self.integer_validator('height', height)
        self.__width = self.integer_validator('width', width)
        self.__height = height
        self.__width = width
