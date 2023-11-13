#!/usr/bin/python3
"""This module contains the class rectangle"""


from models.base import Base
"""This module contains the base class"""


class Rectangle(Base):
    """This class creates an instance of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a rectangle class"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of the rectangle"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of the rectangle"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """returns the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the x of the rectangle"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """returns the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the y of the rectangle"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints a rectangle to stdout using '#'"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        strn = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + \
            "/" + str(self.__y) + " - " + str(self.__width) + \
            "/" + str(self.__height)
        return strn

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 4:
                self.__y = args[4]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 0:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['width'] = self.__width
        my_dict['height'] = self.__height
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        return my_dict
