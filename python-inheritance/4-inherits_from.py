#!/usr/bin/python3
""" Return Only sub class of a class """


def inherits_from(obj, a_class):
    """
    Return true if the object is an instance of a class
    """
    if (issubclass(type(obj), a_class) and (type(obj) is not a_class)):
        return True
    else:
        return False
