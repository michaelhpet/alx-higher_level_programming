#!/usr/bin/env python3
def uppercase(str):
    uppercase_string = ""

    for character in str:
        ascii_code = ord(character)

        if ascii_code > 96 and ascii_code < 123:
            ascii_code -= 32

        uppercase_string += chr(ascii_code)

    print("{0:s}".format(uppercase_string))
