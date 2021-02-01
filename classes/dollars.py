#!/usr/bin/env python3

# This is an example of using a class to hide the internal representation of data.  In this case, we're going to
# represent currency (US Dollars in this case) using the underlying amount of pennies as the internal representation.
# If we change the way we represent things internally, code that uses this class doesn't need to know about it, as
# long as we keep the interface to the class (the function calls) the same.


class Dollars:
    """
    A simple example of a class that represents US dollars.
    """
    def __init__(self, dollars=0, cents=0):
        """
        Constructor.
        :param dollars: The number of dollars.   Defaults to zero.
        :param cents: The number of cents.  Defaults to zero.
        """

        # Figure out the number of cents in the arguments that are passed in.  Note that, if a fractional number is
        # passed in either dollars or cents, then this might lose some of the money.  The class is designed to
        # represent physical money, with the smallest unit being one cent.  The constructor is where we enforce our
        # policy for converting to pennies.  This is one example of how to do it, but it's not the only one that's
        # possible.

        # self.cents is NOT the same as the input parameter cents - it's a variable defined in
        # Dollars that's named cents.
        self.cents = int(int(dollars * 100) + cents)

    def __repr__(self):
        """
        Representation of Dollars.
        :return: A string representation of the dollar amount.
        """

        # There's a fair amount going on here to get the representation right.  The first argument is an optional
        # negative sign.  This is filled in appropriately by the if clause that is the first argument to format().
        # Then there's a dollar sign, then the amount of whole dollars, a dot, and the number of cents left over.
        # The whole dollars will appear with commas, and the cents has two places, with a leading zero if needed.
        # To get the number of dollars, we take the absolute value of cents (which could be negative) and do integer
        # division.  To get the number of cents, we take the absolute number of cents modulo 100.  We need to use the
        # absolute values to make sure things come out right.

        # Doing it pedantically
        str_neg_sign = '-' if self.cents < 0 else ''
        str_dollar_amount = abs(self.cents) // 100  # Integer divide
        str_cents_amount = abs(self.cents) % 100
        str_glue_it_together = '{0}${1:,}.{2:02}'.format(str_neg_sign, str_dollar_amount, str_cents_amount)
        return str_glue_it_together
        # This is the same thing as above, just in one fell swoop
        # return '{0}${1:,}.{2:02}'.format('-' if self.cents < 0 else '', abs(self.cents) // 100, abs(self.cents) % 100)

    def __str__(self):
        """
        The string representation of Dollars.
        :return: a string
        """

        # This is just going to be the same as the representation.
        return self.__repr__()

    def __neg__(self):
        """
        Mathematical negative.
        :return: The negative of the dollar amount.
        """

        # This lets us have a negative number of dollars.  We're going to return an instance of Dollars, with the
        # number of cents set to the negative of the number in the instance on which this is called.
        return Dollars(cents=-self.cents)

    def __add__(self, other):
        """
        Mathematical addition.
        :param other: The right hand side of the addition.
        :return: The sum of the instance and other.
        """

        # We're going to use duck typing to make this work.  First, we know that self is an instance of Dollar, and
        # we're going to assume that other is too.  We return an instance of Dollars with an amount of cents that's
        # the sum of cents in both of the arguments.  If this works, then we're all set.  However, if other is not
        # an instance of Dollars, then Python will raise an AttributeError exception (technically, it will raise it if
        # other doesn't have a cents attribute).  In this case, we're going to try to make a Dollars instance from
        # other, and then recursively call the __add__ function.  If this works, we're all set.  If not, Python will
        # raise an exception, and we'll leave the user to deal with it.
        try:
            # Assume other is an instance of Dollars.
            #   The cents=self.cents sets the cents value directly - could have done
            #   Dollars(0, self.cents + other.cents)
            return Dollars(cents=self.cents + other.cents)
        except AttributeError:
            # AttributeError happens when you try to do foo.bar and bar is not a variable
            #  or methods on the class foo

            # If other is not an instance of Dollars, try to make one from it, and recursively call __add__.
            return self + Dollars(other)

    def __radd__(self, other):
        """
        Mathematical right addition.
        :param other: The left hand side of the addition.
        :return: The sum of the instance and other.
        """

        # Addition commutes, so we're just going to call __add__ to get the job done.
        return self + other

    def __sub__(self, other):
        """
        Mathematical subtraction.
        :param other: The right hand side of the subtraction.
        :return: The result of the subtraction.
        """

        # Duck typing again, just like __add__.
        try:
            return Dollars(cents=self.cents - other.cents)
        except AttributeError:
            return self - Dollars(other)

    def __rsub__(self, other):
        """
        Mathematical right subtraction.
        :param other: The left hand side of the subtraction.
        :return: The result of the subtraction.
        """

        # Duck typing one more time - see add above.
        try:
            return Dollars(cents=other.cents - self.cents)
        except AttributeError:
            return Dollars(other) - self

    def __mul__(self, other):
        """
        Mathematical multiplication.
        :param other: The multiplier.
        :return: The result of the multiplication.
        """

        # This one is different, since it only makes sense to multiply Dollars by a number, not by another Dollars
        # instance.  Simply return a Dollars instance that has the number of cents multiplied by the multiplier.
        return Dollars(cents=self.cents * other)

    def __rmul__(self, other):
        """
        Mathematical right multiplication.
        :param other: The multiplier.
        :return: The result of the multiplication.
        """

        # Multiplication commutes, so just use __mul__.
        return self * other

    def __truediv__(self, other):
        """
        Mathematical division.
        :param other: The divisor
        :return: The result of the division.
        """

        # Just like multiplication, it only makes sense to divide an instance of Dollars by a number.
        return Dollars(cents=self.cents / other)


if __name__ == '__main__':
    # What sort of testing would you do for the Dollars class?

    # Make an instance of the Dollars class
    d = Dollars(1, 23)  # dollars is set to 1, cents is set to 23
    print(d)

    # If you don't give two arguments, defaults to dollars = 10
    d_ten_dollars = Dollars(10)
    print(d_ten_dollars)

    # .. But you can explicitly set cents
    d_ten_cents = Dollars(cents=10)
    print(d_ten_cents)

    # Call the negative (__neg__) method on Dollars and store the result in d_neg
    d_neg = - d
    print(d_neg)

    # Calls __rmul__ on the Dollar class, then creates a Dollar from that and prints it
    d_times_three_v1 = 3 * d
    print(d_times_three_v1)

    # Calls __mul__ on the Dollar class, then creates a Dollar from that and prints it
    d_times_three_v2 = d * 3
    print(d_times_three_v2)

    # Since Dollars behaves like a numerical quantity (and, in particular, has __add__defined for this example), we
    # can use functions on it, just like it was a built-in numerical type.
    l = [Dollars(x) for x in range(5)]
    print(l)

    # Show just adding two Dollar amounts together
    l2_l4 = l[2] + l[4]
    # Show adding a number to a dollar
    l3 = l[0] + 2  # 2 will turn into $2. Note that PyCharm is flagging that it thinks the type int is wrong
    l4 = 3 + l[0]  # 3 will turn into $3

    # Because + is defined, we can sum the list (which just does a bunch of adds)
    print(sum(l))

    # If you want to, you can also use the raw forms of the functions, but it looks ugly.
    a = Dollars(1, 45)
    b = Dollars(cents=25)
    c = a.__add__(b)   # Exactly the same as c = a + b
    c_better = a + b
    print(a, b, c)
    print(a, b, c_better)
