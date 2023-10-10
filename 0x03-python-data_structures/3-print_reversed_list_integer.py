#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copy = my_list.copy()
    for i in range(len(my_list)):
        print("{:d}".format(copy.pop()))
