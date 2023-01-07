#!/usr/bin/python3
def multiple_returns(sentence):
    if not isinstance(sentence, str):
        return None

    if len(sentence) == 0:
        return (0, None)

    return (len(sentence), sentence[0])
