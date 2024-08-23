#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #
   """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
