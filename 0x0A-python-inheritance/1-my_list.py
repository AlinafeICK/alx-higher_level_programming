#!/usr/bin/python3
""" a Class Myclass that inherits from list """


class MyList(list):
    """ a Class Myclass that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
