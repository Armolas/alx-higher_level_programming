#!/usr/bin/python3
"""This module contains the class Square"""


from models.rectangle import Rectangle
"""This module contains the Rectangle Class"""


from models.base import Base
"""This module contains the Base class"""


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        strn = "[Square] (" + str(self.id) + ") " + str(self.x) + \
            "/" + str(self.y) + " - " + str(self.width)
        return strn

    @property
    def size(self):
        """returns the width of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the size of the square"""
        if not isinstance(size, int):
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 3:
                self.y = args[3]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 1:
                self.height = args[1]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 0:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.width
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
