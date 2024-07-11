#!/usr/bin/python3
""" A function that True if the object
is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function that checks if the object
    is exactly an instance of the specified class"""
    return (type(obj) == a_class)
