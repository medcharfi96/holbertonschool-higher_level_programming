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

    def area(self):
        """calculate the area"""
        bass = self.__height * self.__width
        return (bass)

    def __str__(self):
        """ rectangle description """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """add descr"""
    def __init__(self, size):
        """ the square class"""
        self.__size = self.integer_validator('size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ fonc cal area"""
        bass = self.__size * self.__size
        return (bass)
