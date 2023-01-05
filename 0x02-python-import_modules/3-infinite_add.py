#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for argument in argv[1:]:
        sum += int(argument)

    print(sum)


if __name__ == "__main__":
    main()
