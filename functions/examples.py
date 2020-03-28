#!/usr/bin/env python3


# Import the value of pi from the math module.
from math import pi

# Import a function to return the wall clock time and a function that sleeps for a given amount of time from the time
# module.
from time import time, sleep


def circle_area(radius):
    """
    A function that calculates the area of a circle.

    :param radius: The radius of the circle.
    :return: The area of the circle.
    """

    # Just compute the area in the return statement, rather than making a separate variable to hold it.
    return pi * radius * radius


# This function takes a function as the first argument, and the arguments for this function as the remaining arguments.
# This is a good example of when you should use *args and **kwds.  When you write the function, you don't know which
# arguments to f will be needed, so this mechanism allows you to make things very general.
def time_function(f, *args, **kwds):
    """
    A simpler timer that times the execution of a function, passed as a parameter.  the execution time is printed out,
    and the return value of the passed function is returned.

    :param f: The function to time.
    :param args: The arguments for the function.
    :param kwds: The keyword arguments for the function.
    :return: The return value of the function that was passed in.
    """

    # Record the start time
    start_time = time()

    # Run the function that was passed in, along with it's arguments
    retval = f(*args, **kwds)

    # Record the stop time
    end_time = time()

    # Print out the elapsed time.  Note that all functions have a variable associated with them, called __name__ that
    # contains the name of the function, as a string.
    print('{0}: {1} seconds'.format(f.__name__, end_time - start_time))

    # Return the value from the original function.
    return retval


if __name__ == '__main__':
    # This is a simple function call.
    print('Circle area of a circle with radius', 2, 'is', circle_area(2))

    # How long does this function take?
    time_function(circle_area, 2)

    # How long does it take for a function that sleeps for a second?
    time_function(sleep, 1)
