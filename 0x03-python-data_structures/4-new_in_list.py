#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not isinstance(my_list):
        return None
        
    my_list_len = len(my_list)
    if idx < 0 or idx > my_list_len - 1:
        return my_list[:]

    new_list = []
    for i in range(my_list_len):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])

    return new_list
