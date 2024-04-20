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
        """Set the size of the square.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
    def my_print(self):
        """Method that prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
