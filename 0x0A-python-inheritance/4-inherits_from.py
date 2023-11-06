#!/usr/bin/python3
"""This module checks if an object is a subclass"""


def inherits_from(obj, a_class):
    """checks if obj is a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
