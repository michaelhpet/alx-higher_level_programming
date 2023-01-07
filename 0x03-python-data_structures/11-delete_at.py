#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not isinstance(my_list, list):
        return None
    
    my_list_len = len(my_list)
    if idx < 0 or idx > (my_list_len - 1):
        return my_list

    for i, item in enumerate(my_list):
        if i == idx:
            del my_list[i]

    return my_list
