#!/usr/bin/python3
""" creating student class """


class Student:
    """ Defining a class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and
                all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
