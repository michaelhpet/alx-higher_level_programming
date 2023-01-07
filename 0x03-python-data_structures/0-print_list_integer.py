#!/usr/bin/python3
def print_list_integer(my_list=[]):
    my_list_len = len(my_list)
    for i in range(my_list_len):
        print("{0:d}".format(my_list[i]))
