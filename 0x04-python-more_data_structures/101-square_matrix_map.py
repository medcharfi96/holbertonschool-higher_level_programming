#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda elem: list(map(lambda row: row**2, elem)), matrix))
