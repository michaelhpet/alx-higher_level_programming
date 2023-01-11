#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0
        
    token = roman_string.upper()
    numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500
    }
    end = len(token) - 1
    result = 0

    for idx, char in enumerate(token):
        if idx < end and numerals[char] < numerals[token[idx + 1]]:
            result -= numerals[char]
        else:
            result += numerals[char]

    return result
