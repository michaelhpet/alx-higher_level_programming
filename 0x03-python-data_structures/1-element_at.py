#!/usr/bin/python3
def element_at(my_list, idx):
    my_list_len = len(my_list)

    if idx < 0 or idx > my_list_len - 1:
        return None
    for i in range(my_list_len):
        if i == idx:
            return my_list[i]
