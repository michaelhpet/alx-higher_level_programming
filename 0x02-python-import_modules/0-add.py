#!/usr/bin/python3
from add_0 import add


def main():
    a = 1
    b = 2
    sum = add(a, b)
    print("{0:d} + {1:d} = {2:d}".format(a, b, sum))


if __name__ == "__main__":
    main()
