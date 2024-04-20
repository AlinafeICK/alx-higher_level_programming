#!/usr/bin/python3
""" A module of class Square based on 1-square.py."""


class Square:
    """A Square Class that defines a square
    with a private instance attribute: size
    """
    def __init__(self, size=0):
        """ Initialization method for the Square.
        Args:
            size (int): Size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Method to Get/Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
