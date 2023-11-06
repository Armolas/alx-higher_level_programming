#!/usr/bin/python3
"""This module contains a function which checks the instance of \
an object"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
