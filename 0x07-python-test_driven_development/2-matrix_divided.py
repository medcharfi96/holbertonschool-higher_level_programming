#!/usr/bin/python3
"""
divides a matrix with an integers
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix
    """
    nouveau_mtx = []
    erreur = "matrix must be a matrix (list of lists) of integers/floats"
    erreur2 = "matrix must be a matrix (list of list of integers/float)"
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError()
    if len(matrix) is 0:
        raise TypeError(erreur)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(erreur)
        size_compare = len(matrix[0])
        if len(row) != size_compare:
            raise TypeError('Each row of the matrix must have the same size')
        ADDrow = []
        for j in row:
            if not isinstance(j, (int, float)):
                raise TypeError(erreur2)
            ADDrow.append(round((j / div), 2))
        nouveau_mtx.append(ADDrow)
    return nouveau_mtx
