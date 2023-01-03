#!/usr/bin/python3
for ascii_code in range(97,123):
     if ascii_code not in [101, 113]:
        print(f"{chr(ascii_code):s}", end="")
