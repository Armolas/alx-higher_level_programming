#!/usr/bin/python3
def no_c(my_string):
    new = []
    for let in my_string:
        if let == "c" or let == "C":
            continue
        new.append(let)
    new_str = "".join(new)
    return new_str
