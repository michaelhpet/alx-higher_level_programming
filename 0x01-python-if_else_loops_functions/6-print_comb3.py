#!/usr/bin/python3
for digit_one in range(10):
    for digit_two in range(10):
        if digit_two > digit_one:
            if digit_one < 8 and digit_two < 10:
                print(f"{digit_one:d}{digit_two:d}", end=", ")
            else:
                print(f"{digit_one:d}{digit_two:d}")
