#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix =[]
    for x in matrix:
        squared_matrix.append(list(map(lambda x: x**2, x)))
    return (squared_matrix)
