#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        values = a_dictionary.values()
        score = max(values)
        for key, value in a_dictionary.items():
            if value == score:
                return key
        else:
            return None
    except Exception:
        return None
