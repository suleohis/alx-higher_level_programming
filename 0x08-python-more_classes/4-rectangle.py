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

    def area(self):
        """
        area of  a rectangle

        return area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter of a rectangle

        return perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        print a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
