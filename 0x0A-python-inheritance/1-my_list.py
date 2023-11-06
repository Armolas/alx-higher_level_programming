#!/usr/bin/python3
"""This module contains a class MyList which is a subclass of list"""


class MyList(list):
    """This class creates an instance of the class MyList"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
