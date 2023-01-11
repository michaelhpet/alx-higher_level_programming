#!/usr/bin/python3
def weight_average(my_list=[]):
    try:
        if len(my_list) == 0:
            return 0

        weights = sum(list(map(lambda x: x[1], my_list)))
        total = sum(list(map(lambda x: x[0] * x[1], my_list)))
        return total / weights
    except Exception:
        return None
