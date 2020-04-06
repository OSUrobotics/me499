#!/usr/bin/env python3


if __name__ == '__main__':
    # Python can represent integers.  Here are a couple of ways to create an integer variable.  Notice the truncation,
    # rather than rounding, in the assignment of d.
    a = 5
    b = int()
    c = int(4)
    d = int(3.84)
    print(a, b, c, d)

    # Integers have the usual math operations.  Note that division will return a float, but others will preserve the
    # integer type.  The type() function can tell you the type of a variable.  You should try to avoid using this
    # function in your code.
    print('\ndivision')
    a = 10
    b = 10 / 5
    print(b, type(b))

    # We can force integer division with //.  Note that this will truncate results.
    print('\nInteger division')
    a = 10
    b = 10 // 5
    print(b, type(b))

    a = 10
    b = 10 // 3
    print(b, type(b))

    # We can also calculate the remainder
    n = 10
    m = 3
    div = n // m
    rem = n % m
    print('\n{0} = {1} * {2} + {3}'.format(n, div, m, rem))
