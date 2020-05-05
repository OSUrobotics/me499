#!/usr/bin/env python3


# This shows how classes can be used to encapsulte information about objects, and operations on that information.


from math import pi


class Circle:
    """
    A 2d circle.
    """

    def __init__(self, radius):
        """
        Constructor.
        :param radius: The circle radius.
        """
        # We're not going to allow a negative radius.
        if radius < 0:
            raise ValueError('Circle: Radius must be non-negative')

        self.radius = radius

    def __str__(self):
        return 'Circle({0})'.format(self.radius)

    def area(self):
        """
        Circle radius.
        :return: The radius of the circle.
        """
        return pi * self.radius ** 2

    def diameter(self):
        """
        Circle diameter.
        :return: The circle diameter.
        """
        return 2 * self.radius

    def circumference(self):
        """
        The circumference of the circle.
        :return: The circle circumference.
        """
        return 2 * pi * self.radius

    def perimeter(self):
        """
        The perimeter (circumference) of the circle.
        :return: The circle perimeter.
        """
        return self.circumference()


class Rectangle:
    """A 2d rectangle"""
    def __init__(self, length, width):
        # We're not going to allow negative lengths.
        if length < 0 or width < 0:
            raise ValueError('Rectangle: Length and width must be non-negative.')

        self.length = length
        self.width = width

    def __str__(self):
        return 'Rectangle({0}, {1})'.format(self.length, self.width)

    def area(self):
        """
        Rectangle area.
        :return: The rectangle area.
        """
        return self.width * self.length

    def perimeter(self):
        """
        Rectangle perimeter.
        :return: The perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)


if __name__ == '__main__':
    c = Circle(10)
    d = Rectangle(10, 30)

    # Since the circle and the rectangle have functions in common, we can treat them the same in this for loop.
    shapes = [c, d]
    for s in shapes:
        print('{0}: area is {1}'.format(s, s.area()))
