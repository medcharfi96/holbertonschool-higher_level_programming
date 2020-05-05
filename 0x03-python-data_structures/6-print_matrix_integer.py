#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lista in matrix:
        for j in range(0, len(lista)):
                if j + 1 != len(lista):
                    print("{:d}".format(lista[j]), end=" ")
                else:
                    print("{:d}".format(lista[j]), end="")
        print()
