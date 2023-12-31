#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """This class creates an instance of base geometry"""
    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """this method validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """This class creates an instance of Rectangle which is a \
subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Initializes a rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
