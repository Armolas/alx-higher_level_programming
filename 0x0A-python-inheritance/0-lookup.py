#!/usr/bin/python3
"""This module contains the lookup function which
returns a list of all the attributes of a class"""


def lookup(obj):
    """this function returns a list of all available attributes of obj"""
    return dir(obj)
