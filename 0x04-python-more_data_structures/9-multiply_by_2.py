#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    try:
        dict_items = list(a_dictionary.items())
        new_dict = dict(map(lambda x: (x[0], x[1] * 2), dict_items))
        return new_dict
    except Exception:
        return None
