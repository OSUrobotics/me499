#!/usr/bin/env python3


if __name__ == '__main__':
    # type() will tell you the type of an expression
    print(type(2))
    print(type(2.3))
    print(type(True or False))

    # You can easily move between types by casting.  In general, you should try to avoid doing this if you can.  It's
    # generally better to let Python figure it out on its own.
    print(int(3.2))   # Cast a float to an integer
    print(str(3.4))   # Cast a float to a string
    print(float(3))   # Cast an integer to a float.
    print(int('3'))   # Cast a string to an integer
