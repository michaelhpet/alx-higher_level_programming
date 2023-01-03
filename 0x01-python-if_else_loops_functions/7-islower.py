def islower(c):
    ascii_code = ord(c)
    if ascii_code > 96 and ascii_code < 123:
        return True
    else:
        return False
