#!/usr/bin/python3
"""This module contains a class called Square"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
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
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """returns the position of a square object"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of a square object"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints out the square object using #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                if i != self.__size:
                    print("#", end="")
                else:
                    print("#")
            print()
