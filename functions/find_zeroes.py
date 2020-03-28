#!/usr/bin/env python3


# Here's an example of a useful use of recursion.  The idea is to find the zero-crossing of a function over a given
# interval.  The base is is if there's a zero-crossing in the interval, and the interval is small enough.  If not,
# divide the interval into two, and throw away the half the doesn't include the zero-crossing, and run the function
# again on the remaining half.  You could do this without recursion, but this is a natual way to think about the
# problem.
def find_zeroes(f, a, b, epsilon=1e-10):
    """
    Find the zero-crossing of the function f in the interval [a, b].  The function assumes that there is a single
    zero-crossing in the interval.

    :param f: The function.
    :param a: The lower bound of the interval.
    :param b: The upper bound of the interval.
    :param epsilon: The stopping tolerance.  When the interval is less that this, the function will return.  Defaults
                    to 1e-10.
    :return: The zero-crossing of f or None if there is no zero-crossing in the interval.
    """

    # Guard against someone getting the ordering of a and b wrong.
    low = min(a, b)
    high = max(a, b)
    middle = (low + high) / 2

    # Evaluate the functions, and store the results.  We're doing this to reduce the number of function evaluations
    # that we need, in case the function is expensive to evaluate.
    f_low = f(low)
    f_high = f(high)
    f_middle = f(middle)

    # If there's no zero-crossing in the interval, then we're done.  We can test this by looking at the sign of the
    # function evaluations at the bounds.  If they're different, then there's a zero-crossing.  An easy way to check
    # this is to multiply them together.  If they signs are different, then their product is negative.  If there's no
    # zero-crossing, return None.
    if f_low * f_high > 0:
        return None

    # If the interval is narrow enough, return the mid-point of it.  This is the base case of the recursion.
    if abs(high - low) < epsilon:
        return middle

    # If we haven't hit the base case, then we have to recursively call the function.  Pick the half of the interval
    # that contains the zero crossing, and call the function on that.  We can do this by looking at the sign of the
    # function evaluated at the mid-point.  If it's different from the function evaluated at the lower bound, then we
    # should keep the bottom half.
    if f_low * f_middle > 0:
        return find_zeroes(f, middle, high, epsilon)
    else:
        return find_zeroes(f, a, middle, epsilon)


# This is essentially the same as the first implementation, but it does the recursive step explicityly in a while loop.
# This means that the function never calls itself.  Notice how the function is more complicated, since you have to
# manage values and bounds for yourself, rather than having Python and the function call mechanism do it for you.
# However, this is a more efficient way to do things, since you don't have the function call overhead.
def find_zeroes_2(f, a, b, epsilon=1e-10):
    """
    A formulation of the recursive version of find_zeroes that does not do explicit recursion on the stack.

    :param f: The function.
    :param a: The lower bound of the interval.
    :param b: The upper bound of the interval.
    :param epsilon: The stopping tolerance.  When the interval is less that this, the function will return.  Defaults
                    to 1e-10.
    :return: The zero-crossing of f or None if there is no zero-crossing in the interval.
    """

    # Get the bounds, as before
    low = min(a, b)
    high = max(a, b)
    middle = (a + b) / 2

    # Get the function evaluations, as before
    f_low = f(low)
    f_middle = f(middle)
    f_high = f(high)

    while abs(high - low) > epsilon:
        # If there's no zero-crossing in the interval, then we're done.
        if f_low * f_high > 0:
            return None

        if f_low * f_middle > 0:
            low = middle
            f_low = f_middle
        else:
            high = middle
            f_high = f_middle

        middle = (low + high) / 2
        f_middle = f(middle)

    return middle


if __name__ == '__main__':
    # Each test case is a tuple: function, zero, low bound, high bound).  We're only going to test the positive cases
    # here, but you should really test some negative cases, too.
    test_cases = (
        (lambda x: x, 0, -10, 10),
        (lambda x: x + 2, -2, -10, 10),
        (lambda x: x * x - 4, 2, 0, 10),
    )

    print('Running tests:')
    for tester in [find_zeroes, find_zeroes_2]:
        print('  ' + tester.__name__ + ':')
        for (f, zero, a, b) in test_cases:
            result = tester(f, a, b)
            if abs(result - zero) > 1e-10:
                print('    failed test for {0}: expected {1} but got {2}'.format(f.__name__, zero, result))
        print('    tests completed')

    # How long do these implementations take?
    from examples import time_function
    functions = [find_zeroes, find_zeroes_2]
    for f in functions:
        time_function(f, lambda x: x, -100, 100, 1e-30)
