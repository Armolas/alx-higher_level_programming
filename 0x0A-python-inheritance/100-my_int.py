#!/usr/bin/python3
"""This module creates a class MyInt"""


class MyInt(int):
    """this class is a subclass of the int class"""
    def __init__(self, value):
        self.value = value

    def __eq__(self, b):
        if isinstance(b, int):
            return self.value != b.real

    def __ne__(self, b):
        if isinstance(b, int):
            return self.value == b.real
