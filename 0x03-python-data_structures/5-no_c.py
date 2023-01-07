#!/usr/bin/python3
def no_c(my_string):
    if not isinstance(my_string, str):
        return None

    new_string = ""
    for character in my_string:
        if character in "cC":
            continue
        new_string += character

    return new_string
