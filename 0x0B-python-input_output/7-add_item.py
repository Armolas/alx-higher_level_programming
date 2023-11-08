#!/usr/bin/python3
"""This is a script that load, add and save item"""


if __name__ == "__main__":
    import sys
    """This is the sys module"""


    import os
    """This is the os module"""


    load = __import__('6-load_from_json_file').load_from_json_file
    """This module loads an object from a json file"""


    save = __import__('5-save_to_json_file').save_to_json_file
    """This module saves an object to a json file"""


    no_of_args = len(sys.argv)
    if os.path.exists("add_item.json"):
        my_list = load('add_item.json')
    else:
        my_list = []
    for i in range(1, no_of_args):
        my_list.append(sys.argv[i])
    save(my_list, "add_item.json")
