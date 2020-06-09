#!/usr/bin/python3
"""
claass rectangle
"""


from models.base import Base


class Rectangle(Base):
    """class description"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialisation"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
