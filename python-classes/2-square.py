#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class Square with a private instance attribute size"""

    def __init__(self, size=0):
        """Initialize a new Square with a specified size

        Args:
            size (int, optional): The size of the Square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
