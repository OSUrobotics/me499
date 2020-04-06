#!/usr/bin/env python3


from math import cos


def abs_of_steel(n):
    """
    Function to illustrate the use of duck typing for make an abs function that works on iterables and scalars.
    :param n: List or scalar
    :return: The absolute value of the iterable or scalar.
    """

    try:
        # Assume that abs will work, and try to run it.
        return abs(n)
    except TypeError:
        # If it doesn't work, catch the exception, and try to apply map to it.
        return list(map(abs, n))


def better_abs_of_steel(n):
    """
    Function to illustrate the use of duck typing for make an abs function that works on iterables and scalars.
    :param n: List or scalar
    :return: The absolute value of the iterable or scalar.
    """

    try:
        # Assume that abs will work, and try to run it.
        return abs(n)
    except TypeError:
        # If it doesn't work, catch the exception, and try to apply map to it.
        return list(map(better_abs_of_steel, n))


def steel(f, n):
    """
    This is a generalizable wrapper to robustify arbitrary functions.
    :param f: The function to robustify.
    :param n: A parameter to the function.
    :return: The return from the function, after applying it to every element in the parameter.
    """

    try:
        return f(n)
    except TypeError:
        return list(map(lambda x: steel(f, x), n))


# Since steel takes two arguments, we can wrap it in an anomymous function that only takes one.  This makes it easier
# to robustify multiple functions.
abs_of_steel2 = lambda x: steel(abs, x)
cos_of_steel = lambda x: steel(cos, x)


if __name__ == '__main__':
    # Works for both lists and scalars
    print(abs_of_steel([1, -2, 3]))
    print(abs_of_steel(-5))

    # Doesn't work for embedded lists
    #print(abs_of_steel([1, 2, [3, 4, 5]]))

    # But, the better version can work on these embedded lists
    print(better_abs_of_steel([1, 2, [3, 4, 5]]))

    print(abs_of_steel2(1))
    print(abs_of_steel2([-1, 2, -3]))
    print(abs_of_steel2([1, 2, [-3, -4, -5]]))
