#!/usr/bin/python3
def magic_string():
    magic_string.__calls = getattr(magic_string, '__calls', 0) + 1
    return "BestSchool, " * (magic_string.__calls - 1) + "BestSchool"
