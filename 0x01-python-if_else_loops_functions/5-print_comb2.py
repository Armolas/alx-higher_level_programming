#!/usr/bin/python3
sep = ", "
for num in range(100):
    if num != 99:
        print("{:02d}".format(num), end=sep)
    else:
        print("{:02d}".format(num))
