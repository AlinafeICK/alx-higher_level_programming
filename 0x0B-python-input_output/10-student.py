#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class
        Args:
          first_name (str): The first name of the student
          last_name (str): The last name of the student
          age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance
        if attrs is a list of strings, only attribute names contained
        in this list are returned
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        else:
            return self.__dict__
