#!/usr/bin/env python3


def yes():
    """
    Simple function that returns True
    :return: True
    """

    print('  yes()')
    return True


def no():
    """
    Simple function that returns False
    :return: False
    """

    print('  no()')
    return False


def get_value():
    """
    Function that just returns a number.
    :return: 4
    """

    return 4


if __name__ == '__main__':
    # Boolean variables can take one of two values: True or False
    a = True
    b = False

    # Booleans are often used as expressions to control program flow:: if and while loops, for example.
    if a:
        print('a is True')
    else:
        print('a is False')

    # You can chain together booleans with the logical operators: or, and
    if a or b:
        print('one of a, b is True')
    else:
        print('a and b are both False')

    if a and b:
        print('a and b are both True')
    else:
        print('at least one of a, b is False')

    # Python uses short-circuit evaluation.  This means that it only evaluates as much of an expression as it has to
    # in order to determine the truth of the expression.  For and, it stops on the first False.  For or, it can stop
    # on the first True.
    print('Should only print one yes')
    if yes() or yes():
        pass

    print('should only print one no')
    if no() and yes():
        pass

    print('should print yes, yes, no')
    if yes() and yes() and no() and yes():
        pass

    # Python can interpret numbers as booleans.  Zero is False, and everything else is True.  Beware relying on floating
    # point numbers being exactly zero.
    i = 5
    while i:
        print(i)
        i -= 1

    # Compound booleans return the last thing they evaluated.  This can be subtle
    print('Different returns from compounds:')
    print(' ', True and False)
    print(' ', True and 0)
    print(' ', 1 and 2 and 3)
    print(' ', 1 and False or 3)
    print(' ', 1 and False and 3)

    # The way that this is often run is to use a boolean to determine whether or not to run a function.  This results
    # in the same behavior as:
    # if run_function:
    #     results = get_value()
    # else:
    #     results = None

    run_function = None   # None also evaluates to False.  Try changing this to True
    results = run_function and get_value()
    print(results)
