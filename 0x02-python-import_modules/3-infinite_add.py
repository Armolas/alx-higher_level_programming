#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    no = len(argv) - 1
    for i in range(1, no + 1):
        total += int(argv[i])
    print("{:d}".format(total))
