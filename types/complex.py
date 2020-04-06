#!/usr/bin/env python3

from cmath import sin


if __name__ == '__main__':
    # As of Python 3, complex numbers are built in to the language.  Here's how to assign them to variables.
    a = 3 + 4j
    b = 2j
    c = complex()
    d = complex(1)
    e = complex(1, 2)
    print(a, b, c, d, e)

    # The normal mathematical operations work as expected, but you have to include functions from cmath, rather than
    # math for things to work.
    print(sin(3 + 4j))