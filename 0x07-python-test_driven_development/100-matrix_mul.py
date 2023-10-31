#!/usr/bin/python3
"""This module contains a function that multiples \
a matrix"""


def matrix_mul(m_a, m_b):
    """This fuction multiples matrix m_a by m_b"""
    matrix = []
    for i in range(len(m_b[0])):
        row = []
        for j in range(len(m_a)):
            num = 0
            for k in range(len(m_b[0])):
                num += m_a[j][k] * m_b[k][i]
            row.append(num)
        matrix.append(row)
    return matrix
