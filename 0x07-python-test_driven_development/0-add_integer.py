#!/usr/bin/python3
"""This module contains a function that adds two numbers as integers"""


def add_integer(a, b=98):
    """ returns the addition of a and b"""
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    elif not a:
        raise TypeError('a must be an integer')
    elif b is None:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
