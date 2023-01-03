#!/usr/bin/python3
for digit_one in range(10):
    for digit_two in range(10):
        if digit_two > digit_one:
            if digit_one < 8 and digit_two < 10:
                print("{0:d}{1:d}".format(digit_one, digit_two), end=", ")
            else:
                print("{0:d}{1:d}".format(digit_one, digit_two))
