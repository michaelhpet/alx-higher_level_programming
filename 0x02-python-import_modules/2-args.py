#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1
    title = 'argument' if argc == 1 else 'arguments'
    terminator = '.' if argc == 0 else ':'
    print(f"{argc:d} {(title + terminator):s}")
    if argc > 0:
        for index, argument in enumerate(argv):
            if index == 0:
                continue
            print(f"{index:d}: {argument:s}")


if __name__ == "__main__":
    main()
