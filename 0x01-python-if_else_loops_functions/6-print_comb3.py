#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            print("{:d}".format(i), end="")
            if i != 8:
                print("{:d}".format(j), end=", ")
            else:
                print("{:d}".format(j))
