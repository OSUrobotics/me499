#!/usr/bin/env python3


from time import time


def time_in(iterable, n):
    """
    Time the use of in in an iterable.
    :param iterable: The iterable to search in.
    :param n: The element to search for.
    :return: True if n is in iterable, False otherwise.
    """
    start_time = time()
    retval = n in iterable
    end_time = time()
    print('{0} seconds'.format(end_time - start_time))
    return retval


if __name__ == '__main__':
    # Build a list of the numbers from 0 to 999999
    a = list(range(1000000))

    # We can ask if a number is in this list with the in keyword
    if 123 in a:
        print('123 is in')
    else:
        print('123 is not in')

    # The time it takes to do this depends on where we find the number.  In this example, the time taken depends on the
    # position of the number in the list.
    print('List:\n  0: ', end='')
    time_in(a, 0)
    print('  500000: ', end='')
    time_in(a, 500000)
    print('  -1: ', end='')
    time_in(a, -1)

    # Sets are different, since they have an O(1) lookup.  This means that the time taken doesn't depend on what you're
    # searching for, and that it's also quicker than a list in most cases.
    s = set(a)
    print('Set:\n  0: ', end='')
    time_in(s, 0)
    print('  500000: ', end='')
    time_in(s, 500000)
    print('  -1: ', end='')
    time_in(s, -1)