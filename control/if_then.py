#!/usr/bin/env python3


def big(n):
    """
    Prints a message if the argument is big, to illustrate a simple if statement.

    :param n: The number.
    :return: None
    """

    # We're going to pretend that 100 is a big number, for the purposes of this function.
    if n > 100:
        print('This is a big number ({0})'.format(n))


def big_or_small(n):
    """
    Prints a message about the size of a number, to illustrate a simple if-else statement.

    :param n: The number.
    :return: None
    """

    if n > 100:
        print('This is a big number ({0})'.format(n))
    else:
        print('This is a small number ({0})'.format(n))


def numbers(n):
    """
    A function to illustrate if-elif-else statements.

    :param n: A number.
    :return: A string representation of the number.

    """
    if n == 0:
        return 'zero'
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    else:
        return 'unknown number'


if __name__ == '__main__':
    big(1)
    big(1000)

    big_or_small(1)
    big_or_small(1000)

    print(numbers(1))
