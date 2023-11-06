#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """This class creates an instance of base geometry"""
    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width

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
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def __str__(self):
        """creates a prints function"""
        strn = ("[Rectangle] " + str(self.__width)
                + "/" + str(self.__height))
        return strn

    def area(self):
        """returns the area of rectangle"""
        return self.__height * self.__width


class Square(Rectangle):
    """creates an instance of a square"""
    def __init__(self, size):
        """initializes a square instance"""
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size
        super().__init__(size, size)

    def area(self):
        """returns the area of a square"""
        return self.__width * self.__height
