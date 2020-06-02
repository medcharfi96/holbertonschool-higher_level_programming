#!/usr/bin/python3
"""
creation class and print
"""


class MyList(list):
    """description of the class"""
    def print_sorted(self):
        """ print the sorted list"""
        print(sorted(self))
