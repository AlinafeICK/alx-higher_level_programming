#!/usr/bin/python3
"""Function that returns True if the object is an
instance of a class inherited through the specified class"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an
    instance of a class inherited through the specified class"""
    return isinstance(obj, a_class) and (type(obj) != a_class)
