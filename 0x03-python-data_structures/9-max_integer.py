#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_int = my_list[0]
    for i_nt in my_list:
        if i_nt > max_int:
            max_int = i_nt
    return max_int
