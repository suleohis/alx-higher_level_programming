#!/usr/bin/python3
"""creates class Square."""


class Rectangle:
    """ Square class defined
        Attributes:
            width (int): width of rectangle
            height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        """initializes
        Args:
            size (int): size
            postion(tuple): postion
        Returns:
            None
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter of width
        Return:
            Width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter of width
        Args:
            value (int): width
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter of height
        Return:
           height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter of height
        Args:
            value (int): height
        Raises
            TypeError: if size is not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
