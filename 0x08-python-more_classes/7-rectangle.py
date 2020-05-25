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
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructeur parametré"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """ the width get """
        return self.__width

    @width.setter
    def width(self, value):
        """ the width set """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the height get """
        return self.__height

    @height.setter
    def height(self, value):
        """ the height set """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate the area of rect"""
        x = self.width * self.height
        return x

    def perimeter(self):
        """ calculer le perimaitre"""
        x = (self.width + self.height) * 2
        return x

    def __repr__(self):
        """affichage 2 """
        return("Rectangle({}, {:d})".format(self.__width, self.__height))

    def __str__(self):
        """  print the rectangle using # """
        mat = []
        sym = str(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(0, self.__height):
                mat.append(sym * self.width)
                if i != self.height - 1:
                    mat.append("\n")
        return("".join(mat))

    def __del__(self):
        """ deconstructeur par defaut"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
