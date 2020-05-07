#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrice = []
    for count in matrix:
        new_matrice.append(list(map(lambda ro: ro ** 2, count)))
    return (new_matrice)
