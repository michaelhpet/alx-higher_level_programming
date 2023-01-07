#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for character in my_string:
        if character in "cC":
            continue
        new_string += character

    return new_string
