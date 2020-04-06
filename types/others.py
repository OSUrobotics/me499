#!/usr/bin/env python3


from math import pi

import decimal
import fractions


if __name__ == '__main__':
    # There are other types in Python, and we'll show you how to create your own types later in the class.  Here are
    # a couple of examples:

    # Fixed and arbitrary precision floating point arithmetic: https://docs.python.org/3/library/decimal.html
    print('Decimals:')
    decimal.getcontext().prec = 3
    d = decimal.Decimal(1 / 3)
    print(1 / 3)
    print(d)

    # Fractions: https://docs.python.org/3/library/fractions.html
    print('\nFractions:')
    f = fractions.Fraction(1, 3)
    g = fractions.Fraction(12, 17)
    print(f)
    print(f * g)

