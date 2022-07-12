#!/usr/bin/python3
"""Defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherites from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): space around the width
            y(int): space around the height
            id(int): id of the rectangle
                        increases when another rectangle is added
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(
            id
        )

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints the area of the rectangle as `#`"""
        xyturple = (self.__x, self.__y)
        for l in range(xyturple[1]):
            print()
        for i in range(self.__height):
            for j in range(xyturple[0]):
                print(" ", end="")
            for k in range(self.__width):
                print("#", end="")
            print()
        return ("")

    def __str__(self):
        """returns str representation"""
        st = f"[{str(self.__class__.__name__)}] ({str(self.id)}) "
        st += f"{str(self.__x)}/{str(self.__y)} - "
        st += f"{str(self.__width)}/{str(self.__height)}"
        return st

    def update(self, *args, **kwargs):
        """assigns arguments to the attributes"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == 'id':
                        self.id = kwargs['id']
                    if key == 'width':
                        self.__width = kwargs['width']
                    if key == 'height':
                        self.__height = kwargs['height']
                    if key == 'x':
                        self.__x = kwargs['x']
                    if key == 'y':
                        self.__y = kwargs['y']
    
    def to_dictionary(self):
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.__width
        dic["height"] = self.__height
        dic["x"] = self.__x
        dic["y"] = self.__y
        return dic
