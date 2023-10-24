#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0):
        """
        This initializes the class

        Arguments:
            size: size of the square
        """
        if (size != int(size)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
