#!/usr/bin/python3
"""pick find functon """


def find_peak(list_of_integers):
    """ last task"""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return (list_of_integers)
    for i in range(0, len(list_of_integers)-1):
        if list_of_integers[i] >= list_of_integers[i+1]:
            x = list_of_integers[i]
    return (x)
