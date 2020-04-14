#!/usr/bin/env python3


def odd_numbers_list(start, stop):
    """
    Generate all the odd numbers in a given range.

    :param start: The start of the range.
    :param stop: The end of the range.
    :return: A list of odd numbers.
    """

    # Build a list with a list comprehension.  This only includes elements in the list if they are odd, because of
    # the if statement in the comprehension.
    return [i for i in range(start, stop + 1) if i % 2 == 1]


def odd_numbers_generator(start, stop):
    """
    A generator function that returns all of the odd numbers in a given range.

    :param start: The start of the range.
    :param stop: The end of the range.
    :return: The odd numbers in the range.
    """

    # Find the first odd number.  If the starting number is even, the first odd number is that number plus one.
    if start % 2 == 0:
        i = start + 1
    else:
        i = start

    # Loop until we get to the end point.
    while i <= stop:
        # Yield the current number.
        yield i

        # The next odd number is two more than the last one.
        i += 2


def add_up_numbers_1():
    """
    Function that adds up some odd numbers, to illustrate the time needed for a list-based implementation.

    :return: The sum of the numbers.
    """

    total = 0
    for i in odd_numbers_list(-10000000, 10000000):
        total += i
    return total


def add_up_numbers_2():
    """
    Function that adds up some odd numbers, to illustrate the time needed for a yield-based implementation.

    :return: The sum of the numbers.
    """

    total = 0
    for i in odd_numbers_generator(-10000000, 10000000):
        total += i
    return total


if __name__ == '__main__':
    # These tests are very minimal.  If you were using these functions for real, you would probably want to do more
    # complete testing
    print('Doing tests:')
    # Note that you have to cast range(-5, 6, 2) to a list because it is a generator itself
    if odd_numbers_list(-5, 5) != list(range(-5, 6, 2)):
        print('  odd_numbers_1: Test failed')
    # odd_numbers_2 is also a generator, so you need to cast both to a list in order to compare them
    if list(odd_numbers_generator(-5, 5)) != list(range(-5, 6, 2)):
        print('  odd_numbers_2: Test failed')
    print('  tests complete')

    # We can use the results of the first function in a for loop
    for n in odd_numbers_list(-5, 5):
        print(n)

    # We can also use the results of the second function in the same way.  The difference is that odd_numbers_2
    # never assembles the whole list.  This really matters if we're iterating over a large number of items.
    for n in odd_numbers_generator(-5, 5):
        print(n)

    # You can see the difference in how long this takes for large ranges.  Building the list takes time (and space)
    # and this slows down the first version of the function.  Since the second version never builds the whole list,
    # then it can be faster (and also uses less memory).
    from examples import time_function
    time_function(add_up_numbers_1)
    time_function(add_up_numbers_2)
