#!/usr/bin/env python3


def even(n):
    """
    A function that determines if a number is even.

    :param n: The number
    :return: True if the number is even, False otherwise.
    """

    # If the remainder after dividing by two is zero, then the number is odd.
    return n % 2 == 0


if __name__ == '__main__':
    # Test by generating a set of even numbers
    print('even():')
    for i in range(-10, 11, 2):
        if not even(i):
            print('  failed for', i)

        # An even number plus one is an odd number.
        if even(i + 1):
            print('  failed for', i + 1)
    print('  tests complete')

    # Generate a list of numbers, then filter out the even numbers.
    numbers = list(range(-10, 10))
    print('Numbers:', numbers)
    print('even():', list(filter(even, numbers)))

    # We can also do this with an anonymous function.  This sort of thing, where you need a simple calculation that
    # needs to be phrased as a function, is the most common use of lambda functions.
    print('Anonymous:', list(filter(lambda x: x % 2 == 0, numbers)))
