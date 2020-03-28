#!/usr/bin/env python3


def factorial_i(number):
    """
    Calculates the factorial of a number, using an iterative process.

    :param number: The number.
    :return: n!
    """

    # Check to make sure the argument is valid.
    if number < 0:
        raise ValueError

    # Go from 1 to n, multiplying up the numbers.
    total = 1
    for i in range(1, number + 1):
        total *= i

    return total


def factorial_r(number):
    """
    Calculates the factorial of a number, using a recursive process.

    :param number: The number.
    :return: n!
    """

    # Check to make sure the argument is valid.
    if number < 0:
        raise ValueError

    # This is the recursive part of the function.
    if number == 0:
        # If the argument is 0, then we simply return the value of 0!, which is 1.
        return 1
    else:
        # Otherwise, return n multiplied by the (n - 1)!
        return number * factorial_r(number - 1)


if __name__ == '__main__':
    # Import the built-in Python function for factorial, so that we can test our implementations against it.  By
    # importing in the testing block, we make sure we don't import it unless we're running the tests.
    from math import factorial

    # Set up a list of the functions we want to test.  Note that these are the functions, not the values from function
    # calls.  This will let us iterate through the functions, and use the same testing code for each of them.  It will
    # also let us add other functions easily.
    functions = [factorial_i, factorial_r]

    # Iterate through the functions we want to test.
    for f in functions:
        # Print the name of the function
        print('{0}:'.format(f.__name__))

        # For this example, we're only going to run through the values from 0 to 9.  In a more realistic test, you
        # would want to test all for the cases that you expected to see or, at least, a representative subset of them.
        for n in range(10):
            # This is the value from the built-in Python function, which we will assume is correct.
            expected = factorial(n)

            # This is our result.
            result = f(n)

            # Since we're dealing with integers, then we can directly compare them.
            if expected != result:
                print(' failed for {0}: expected {1} but got {2}'.format(n, expected, result))

        # We also need to check our error checking.
        try:
            # This should raise an exception.  If it doesn't, then Python will run the next line, telling us that
            # something went wrong.
            f(-1)
            print(' failed to throw an exception for -1')
        except ValueError:
            # If an exception was thrown, then we just silently ignore it, since this is the expected behavior.
            pass

        # Let us know that all of the tests are complete.
        print(' tests completed')

    # How long do these three versions take?  Let's have a look.  We'll use the timing function we wrote earlier,
    # importing it here.  Since we haven't set this up as a Python module, you'll see an error marker in PyCharm, but
    # you can ignore this for now.  The take-away from this is that the built-in function, factorial, is faster than
    # anything we've written.  This is going to be generally true, so you should always prefer built-in Python
    # functions over the ones your write yourself.
    from examples import time_function

    print('\nTiming tests:')
    time_function(factorial, 100)
    for f in functions:
        time_function(f, 100)
