#!/usr/bin/python3

"""class Square that defines a square by: (based on 0-square.py)"""

class Square:
    def __init__(self, size=0):
        """ Initializing a new square.
        
        Args:
            size(int): size of the square
            """
        self.__size = size
        if not isinstance(size, int):
            """size must be int else raise TypeError"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """size must be greater or equal to 0 else raise ValueError"""
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
        