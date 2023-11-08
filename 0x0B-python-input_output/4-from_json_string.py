#!/usr/bin/python3
import json
"""This module contains the function fro_json_string"""


def from_json_string(my_str):
    """returns a json representation of a string"""
    return json.loads(my_str)
