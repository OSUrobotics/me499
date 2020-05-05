#!/usr/bin/env python3


from interval import Interval


if __name__ == '__main__':
    # Set up the variables as floats
    m = 10
    v = 20

    # Do a simple kinetic energy calculation
    k_e = 0.5 * m * v * v
    print('Kinetic Energy', k_e)

    # Set up the variables as intervals, representing uncertainty.
    m = Interval(9.9, 10.1)
    v = Interval(19.5, 20.5)

    # Do the same simple kinetic energy calculation, which just works with the new type.
    k_e = 0.5 * m * v * v
    print('Kinetic Energy', k_e)