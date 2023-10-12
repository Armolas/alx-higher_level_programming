#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = reduce(lambda x, y: x + y, list(set(my_list)))
    return add
