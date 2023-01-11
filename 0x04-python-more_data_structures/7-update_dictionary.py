#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    try:
        a_dictionary[key] = value
        return a_dictionary
    except Exception:
        return None
