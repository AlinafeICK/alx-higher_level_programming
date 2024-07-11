#!/usr/bin/python3
"""Function that returns True if the object is
an instance of a baseclass"""


def is_kind_of_class(obj, a_class):
    """Function that checks if the object
    is an instance of the specified class"""
    return isinstance(obj, a_class)
