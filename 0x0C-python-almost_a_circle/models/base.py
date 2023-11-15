#!/usr/bin/python3
"""This module contains the base class"""


import turtle
import json
"""This imports the json module"""


class Base:
    """This class creates an instace of base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """eturns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        with open(filename, mode='w', encoding="utf-8") as file:
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if str(cls.__name__) == "Rectangle":
            ins = cls(2, 2)
        else:
            ins = cls(2)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        list_dict = cls.from_json_string(json_string)
        instances = []
        for _dict in list_dict:
            ins = cls.create(**_dict)
            instances.append(ins)
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.csv"
        dict_list = []
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        with open(filename, mode='w', encoding="utf-8") as file:
            file.write(cls.to_json_string(dict_list))

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        list_dict = cls.from_json_string(json_string)
        instances = []
        for _dict in list_dict:
            ins = cls.create(**_dict)
            instances.append(ins)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        for rect in list_rectangles:
            turtle.color("red", "blue")
            turtle.goto(rect.x, rect.y)
            turtle.begin_fill()
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.end_fill()
            turtle.penup()
        for sqr in list_squares:
            turtle.color("green", "yellow")
            turtle.goto(sqr.x, sqr.y)
            turtle.begin_fill()
            turtle.pendown()
            turtle.forward(sqr.width)
            turtle.left(90)
            turtle.forward(sqr.width)
            turtle.left(90)
            turtle.forward(sqr.width)
            turtle.left(90)
            turtle.forward(sqr.width)
            turtle.end_fill()
            turtle.penup()
        turtle.done()
