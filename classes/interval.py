#!/ust/bin/emv python3


# This code shows how we can define our own types in Python, using classes. If we do this right, then we can just
# use these classes in other calculations, just as if they were built-in.


# Import the original math sqrt function and rename it
from math import sqrt as mathsqrt


# Define a sqrt that works with our Interval class
def sqrt(n):
    try:
        # If it's an Interval, then we're all set
        return Interval(mathsqrt(n.low), mathsqrt(n.high))
    except:
        # If it's not an interval, pass it off to the sqrt from the math module.
        return mathsqrt(n)


class Interval:
    """Implements interval arithmetic."""
    def __init__(self, a, b=None):
        # If there's just one parameter, set the second bound to be the same value.
        if b == None:
            b = a

        # Make sure we know the low and high bounds, and store them.
        self.low = min(a, b)
        self.high = max(a, b)

    def __repr__(self):
        """
        Representation of the interval.
        :return: String representation of the interval.
        """
        return '[{0}; {1}]'.format(self.low, self.high)

    def __str__(self):
        """
        String representation.
        :return: String representation of the interval.
        """
        return self.__repr__()

    def __contains__(self, n):
        """
        Inclusion operator.
        :param n: Value
        :return: True if the value lies within the interval, inclusive of boundaries.  False otherwise.
        """
        return self.low <= n <= self.high

    def __add__(self, other):
        """
        Addition.
        :param other: The value to add.
        :return: The sum of the arguments.
        """

        # This, and all of the other math operators use duck typing.
        try:
            return Interval(self.low + other.low, self.high + other.high)
        except:
            return Interval(self.low + other, self.high + other)

    def __radd__(self, other):
        """
        Right addition.
        :param other: The value to add.
        :return: The sum of the arguments.
        """

        # Addition commutes.
        return self + other

    def __sub__(self, other):
        """
        Subtraction.
        :param other: The value to subtract.
        :return: The resulting value.
        """
        try:
            return Interval(self.low - other.high, self.high - other.low)
        except:
            return Interval(self.low - other, self.high - other)

    def __rsub__(self, other):
        """
        Right subtraction.
        :param other: The value to subtract from.
        :return: The resulting value.
        """
        return -self + other

    def __mul__(self, other):
        """
        Multiplication.
        :param other: The multiplier.
        :return: The product.
        """
        try:
            return Interval(min(self.low * other.low, self.low * other.high,
                                self.high * other.low, self.high * other.high),
                                max(self.low * other.low, self.low * other.high,
                                self.high * other.low, self.high * other.high))
        except:
            return Interval(self.low * other, self.high * other)

    def __rmul__(self, other):
        """
        Right multiplication.
        :param other: The multiplier.
        :return: The product.
        """
        return self * other

    def __truediv__(self, other):
        """
        Division
        :param other: Divisor.
        :return: The resulting value.
        """

        # Division doesn't work if there's a zero in the denominator, so we're going to raise an exception.
        if other.__contains__(0):
            raise ValueError

        try:
            return self * Interval(1 / other.high, 1 / other.low)
        except AttributeError:
            return self / Interval(other)

    def __rtruediv__(self, other):
        # Division doesn't work if there's a zero in the denominator, so we're going to raise an exception.
        if self.__contains__(0):
            raise ValueError

        try:
            return other * Interval(1 / self.high, 1 / self.low)
        except AttributeError:
            return Interval(other) / self

    def __neg__(self):
        """
        Mathematical negation.
        :return: The negative of the interval.
        """
        return Interval(-self.low, -self.high)


if __name__ == '__main__':
    # What tests would you put in here?

    i = Interval(-2, 2)
    print(i / i)
