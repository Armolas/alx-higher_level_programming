#!/usr/bin/python3
"""This module contains the class Student"""


class Student:
    """creates an instance of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (isinstance(attrs, list) and all
                (isinstance(elm, str) for elm in attrs)):
            my_dict = {}
            for elm in attrs:
                if elm in self.__dict__:
                    my_dict[elm] = self.__dict__[elm]
            return my_dict
        return self.__dict__
