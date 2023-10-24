#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0):
        """ Initializes a square instance

        Args:
            size: size of the square
            """
        if (size != int(size)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of the square object"""
        return self.__size * self.__size

    @property
    def size(self):
        """ returns the size attribute of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of a square object size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints out the square object using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                if i != self.__size:
                    print("#", end="")
                else:
                    print("#")
            print()
