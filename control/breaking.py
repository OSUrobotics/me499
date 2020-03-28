#!/usr/bin/env python3


def break_while():
    """
    A function illustrating the use of break in a while loop.  Type 'quit' to quit.

    :return: None
    """

    while True:
        i = input('Type something: ')

        if i == 'quit':
            break

        print('You typed:', i)


def continue_while(numbers):
    """
    A function illustrating the use of continue in a for loop.  This one prints out the even numbers in an iterable.
    There are better ways of doing this, but we're using continue to illustrate its use.

    :return:
    """

    for n in numbers:
        if n % 2:
            continue

        print(n)


def else_while(n, numbers):
    """
    A function illustrating the use of else with a loop.  This function will determine if n is in the iterable
    numbers.

    :param n: The thing to search for.
    :param numbers: An iterable to search over.
    :return: True if the thing is in the iterable, false otherwise.
    """

    # Loop over the numbers
    for e in numbers:
        # If we've found it, break out of the loop.
        if e == n:
            break
    else:
        # The else clause runs if we exited the loop normally (ie, didn't break)
        return False

    # Otherwise, if we execute break, then we get to here.
    return True


if __name__ == '__main__':
    break_while()
    continue_while(range(10))
    print(else_while(3, [1, 4, 2, 5, 2]))
