#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    try:
        to_del = []
        for key, value_ in a_dictionary.items():
            if value_ == value:
                to_del.append(key)
        for key in to_del:
            del a_dictionary[key]
        return a_dictionary
    except Exception:
        return None
