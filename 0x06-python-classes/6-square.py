#!/usr/bin/python3
"""
definir la class Square
"""


class Square:
    """la classe square"""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ the func get for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ the function set of the position """
        message = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(message)
        elif len(value) != 2:
            raise TypeError(message)
        elif type(value[0]) is not int and value[0] < 0:
            raise TypeError(message)
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError(message)
        else:
            self.__position = value

    def area(self):
        """ return the area of the square"""
        return (pow(self.__size, 2))

    def my_print(self):
        """ print the square  with the add position """
        if self.size is not 0:
            for a in range(0, self.position[1]):
                print()
            for a in range(0, self.size):
                for b in range(0, self.position[0]):
                    print(' ', end='')
                for c in range(0, self.size):
                    print('#', end='')
                print()
        else:
            print()
