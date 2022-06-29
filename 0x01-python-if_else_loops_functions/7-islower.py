#!/usr/bin/python3
def islower(c):
    ascii_n = ord(c)
    if ascii_n >= 97 and ascii_n <= 122:
        return True
    return False