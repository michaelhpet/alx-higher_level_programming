#!/usr/bin/python3
for index in range(25, -1, -1):
    ascii_code = index + 65 if (index % 2) == 0 else index + 97
    print("{0:s}".format(chr(ascii_code)), end="")
