#!/usr/bin/python3
"""This module contains a class Rectangle"""


class Rectangle:
    """This class creates an instance of a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle instance using '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for j in range(self.width):
                rect += '#'
            if i < self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """returns the representation of rectangle instance"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """deletes a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
