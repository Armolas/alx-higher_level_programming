#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
        last = number % 10
    else:
        last = number % 10
    print("{:d}".format(last), end="")
    return last
