#!/usr/bin/python3
"""Module solely for function text_indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after eacg characters: `.`, `?`, and `:`
    Args:
        text (str): text string to parse
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.strip()
    delimiters = ['.', '?', ':']
    for i, character in enumerate(text):
        if character in delimiters:
            print(character, end="")
            print('\n') # 2 new lines because print() adds another
            continue
        if character == ' ' and text[i - 1] in delimiters:
            continue
        print(character, end="")
