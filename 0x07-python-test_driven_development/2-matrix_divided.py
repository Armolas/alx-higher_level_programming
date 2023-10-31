#!/usr/bin/python3
"""This module contains a function that \
divides a matrix by a particular number"""


def matrix_divided(matrix, div):
    """This fuction divides matrix by div"""
    new_matrix = []
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not div:
        raise TypeError('div must be a number')
    if not matrix:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if matrix is None:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    mat_len = len(matrix[0])
    for i in range(len(matrix)):
        if mat_len != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the \
same size')
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[i])))
    return new_matrix
