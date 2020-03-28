#!/usr/bin/env python3


from math import pi


# This is a better implementation of the circle_area function, that makes sure the radius you pass in makes sense.  For
# the purposes of this function, a valid radius is non-negative.
def circle_area(radius):
    """
    Calculate the area of a circle

    :param radius: The circle radius.
    :return: The circle area.
    """

    # If the radius is negative, then raise a ValueError.  This will cause the program calling this function to stop,
    # and will force the person writing it to fix the problem.
    if radius < 0:
        raise ValueError

    # If we get to here, the arguments are valid, and we can just calculate and return the area.
    return pi * radius * radius


if __name__ == '__main__':
    # Valid inputs work as before.
    for r in range(5):
        print('{0}: {1}'.format(r, circle_area(r)))

    # Invalid arguments do not.  Comment out the error checking in the function definition to see what happens if we
    # don't check the arguments.
    try:
        print('-1:', circle_area(-1))
    except ValueError:
        print('Caught an exception!')

    # This will also fail if we don't pass in a number.  We don't explicitly test for this in the function because
    # this case is already handled by Python (in this case by raising a TypeError).  In general, you should only handle
    # problems that would otherwise not stop the program.  For negative radius values, the calculation in the function
    # is valid, and will return a number.  It's not a number that makes geometric sense, but it won't stop the program,
    # and might cause subtle bugs later in in the program.  Explicitly testing and raising an exception avoids this
    # potential problem.
    circle_area('this will not work')
