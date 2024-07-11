#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""


def area(self):
    """Not implemented"""
    raise Exception("area() is not implemented")


def integer_validator(self, name, value):
    """validates value"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
