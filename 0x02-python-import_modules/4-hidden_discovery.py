#!/usr/bin/python3
if __name__ == "__name__":
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name.startswith("__"):
            continue
        else:
            print("{}".format(name))
