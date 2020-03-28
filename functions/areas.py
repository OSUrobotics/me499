#!/usr/bin/env python3


# Import the value of pi from the math library
from math import pi


def rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    :param length: The length of the rectangle.
    :param width: The width of the rectangle.
    :return: The area of the rectangle.
    """

    return length * width


def circle_area(radius):
    """
    Calculates the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """

    return pi * radius * radius


if __name__ == '__main__':
    # It's common practice to put tests in this block, for files that define functions you're going to use elsewhere.
    # This allows you to run your tests by invoking the file as a program.  When the functions are imported by another
    # file, however, the tests are not run.

    # We're going to define some function inputs for which we know the outputs.  In this case, we're going to put these
    # in a dictionary, where the keys are a tuple of the length and the wide of the rectangle, and the value is the
    # expected area.
    rectangle_area_tests = {(1, 2): 2, (1, 1): 1, (3, 2): 6}

    # Iterate through the test cases, checking each one.  The variable assignment in the for loop is a little tricky,
    # but all it's doing is unpacking the information in the key-value pairs.
    for (l, w), a in rectangle_area_tests.items():
        result = rectangle_area(l, w)

        # If we don't get what we expect, then print out the relevant information.  Since we only have integer test
        # values, we will get integer results, so we can compare these with !=.
        if result != a:
            print('Failed test for length', l, 'and width', w, '\n  expected', a, 'but got', result)

    # It's good practice to print out when we're done with the tests since, if we don't, then not running the tests
    # (because out testing code is wrong) will produce the same results as running it and passing all of the tests.
    print('Rectangle tests completed')

    # This is the same testing procedure of the circle.
    circle_area_tests = {0: 0, 1: pi, 2: 4 * pi}
    for r, a in circle_area_tests.items():
        result = circle_area(r)

        # Since the return values are floating point numbers, we should not be using != to compare them.  Instead,
        # we should check if they're close to each other.  This code looks to see if the absolute value of the
        # difference of the numbers (the distance between them) is above some small number.  This will allow small
        # differences, due to the floating point representation, to pass the test.
        if abs(a - result) > 1e-10:
            print('Failed test for radius', r, '\n  expected', a, 'but got', result)
    print('Circle tests completed')
