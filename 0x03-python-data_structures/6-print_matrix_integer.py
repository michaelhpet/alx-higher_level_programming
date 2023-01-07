#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, element in enumerate(row):
            end = "\n" if index == len(row) - 1 else " "
            print("{:d}".format(element), end=end)
