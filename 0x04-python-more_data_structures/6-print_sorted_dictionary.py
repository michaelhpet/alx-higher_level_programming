#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    try:
        sorted_keys = sorted(a_dictionary)
        for key in sorted_keys:
            print(f"{key}: {a_dictionary[key]}")
    except Exception:
        return None
