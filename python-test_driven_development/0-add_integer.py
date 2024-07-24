#!/usr/bin/python3
""" write a function that adds 2 integers"""


def add_integer(a, b=98):
    """ display a message if there is an error otherwise add a + b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)