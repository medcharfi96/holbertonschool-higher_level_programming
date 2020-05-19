#!/usr/bin/python3
"""
definir la class Square
"""


class Square:
    """la classe square"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
