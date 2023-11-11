#!/usr/bin/python3
"""This module contains a function that creates a pascal triangle"""


def pascal_triangle(n):
    """This function creates a pascal triangle"""
    row = [[]]
    for i in range(1, n + 1):
        col = []
        for j in range(i):
            if j == 0 or j == i - 1:
                col.append(1)
            else:
                num = row[i - 1][j - 1] + row[i - 1][j]
                col.append(num)
        row.append(col)
    del row[0]
    return row
