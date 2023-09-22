#!/usr/bin/python3
"""
A child class that inherits property from the parent class
the rectangle is a class with attributes related to a rectangle
and methods such as area, displaty and delete
"""

from models.base import Base


class Rectangle(Base):
    """
    	A rectangle with width and height and x y attributes and
	display, delete, update and area methods
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectagle class by initializing the base class first
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        returns the value of the private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of the private attribute width
        """
        self.check_integer_parameter(value, 'width')

        self.__width = value

    @property
    def height(self):
        """
        returns the value of the private class height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of the private attribute height
        """
        self.check_integer_parameter(value, 'height')

        self.__height = value

    @property
    def x(self):
        """
        returns the value of X
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets teh value of private attribute X
        """
        self.check_integer_parameter(value, 'x')

        self.__x = value

    @property
    def y(self):
        """
        returens the value of Y
        """
        return self.__y

    @y.setter
    def y(self, value:
        """
        sets teh value of private attribute Y
        """
        self.check_integer_parameter(value, 'y')

        self.__y = param

    def check_integer_parameter(self, value, value1):
        """
        checks if a number is an integer parameter
        """
        if type(value) is not int:
            raise TypeError(value1 + ' must be an integer')

        if value <= 0 and value1 in ('width', 'height'):
            raise ValueError(value1 + ' must be > 0')

        if value < 0 and value1 in ('x', 'y'):
            raise ValueError(value1 + ' must be >= 0')

    def area(self):
        """
        returns the area orf teh rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        displays the shape of the rectangle using # symbol
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        returns the string representation of the of the class
	"""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        updates the attributes values of width, height, x and y
        """
        argc = len(args)
        kwargc = len(kwargs)
        attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        sets all of the attributes to a dictionary
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

