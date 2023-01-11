#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        if a_dictionary.get(key) is not None:
            del a_dictionary[key]
        return a_dictionary
    except Exception:
        return None
