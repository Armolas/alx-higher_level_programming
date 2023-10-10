#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    no_of_args = len(argv) - 1
    if no_of_args == 0:
        print("0 arguments.")
    elif no_of_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{:d} arguments:".format(no_of_args))
        for i in range(1, no_of_args + 1):
            print("{}: {}".format(i, argv[i]))
            i += 1 
