#!/usr/bin/env python3


from math import pi, sin, frexp


if __name__ == '__main__':
    # Python represents real numbers using a representation called floating point.  Variables are generally called
    # "floats".  Here are a couple of ways of assigning floats to variables.
    a = 3.14
    b = float()
    c = float(1.23)
    print(a, b, c)

    # There are an uncountably infinite number of real numbers, but Python can only represent a subset of them.  This
    # means you can't rely on floats to exactly represent the number you want to represent.  To make matters worse,
    # some of the numbers we use, like pi, are only approximations and have no exact value.  This means you should
    # always treat floating point numbers as approximations.
    print('sin(pi) should be 0, but Python returns', sin(pi))

    # Don't directly compare values of floats.
    if sin(pi) == 0:
        print('Correct result')
    else:
        print('Incorrect result')

    # Rather, check to see if the values are close.
    if abs(sin(pi)) < 1e-10:
        print('Correct approximation')
    else:
        print('Incorrect approximation')

    # The underlying representation of floats is an exponent-mantissa representation.  Python will tell you the
    # exponent and mantissa for any given float, and you can verify that this works as expected.  You don't need to
    # know this, but it's an example of hiding things away inside of a class.  More information is available here:
    # https://docs.python.org/3/tutorial/floatingpoint.html
    (m,e) = frexp(pi)
    print(m, e)
    print('This should be {0}: {1}'.format(pi, m * 2 **e))

