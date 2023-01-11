#!/usr/bin/python3
def number_keys(a_dictionary):
    try:
        return len(a_dictionary.keys())
    except Exception:
        return None
