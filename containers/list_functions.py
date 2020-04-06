#!/usr/bin/env python3


def odd(n):
    """
    Checks whether a number is odd.
    :param n: Number.
    :return: True if n is odd, False otherwise.
    """
    return n % 2 == 1


def do_something(l):
    """
    A function the illustrates how a function can alter the contents of a list passed into it.  This is a side-effect,
    and is often a bad idea.
    :param l:
    :return:
    """
    l[0] = 'Hello, World!'


if __name__ == '__main__':
    # Build a list of numbers from -9 to 9
    a = list(range(-9, 10))
    print(a)

    # You can make a list of the absolute values of a with a list comprehension
    b = [abs(x) for x in a]
    print(b)

    # You can also do it with the map function.  This takes a function and an iterable (a list, in this case) as
    # arguments, and returns the result of applying the function to each iterable element in turn.  map is an iterator,
    # so we have to cast it to a list.
    b = list(map(abs, a))
    print(b)

    # You can extract the odd elements using a list comprehension
    b = [x for x in a if x % 2]
    print(b)

    # You can also do it with the filter function.  Like map, this takes a function and an interable, and returns the
    # elements for which the function evaluates positive.  Again, you have to cast to a list to make this work. You
    # can do this with an actual function, like this
    b = list(filter(odd, a))
    print(b)

    # Or, you can use an anonymous function instead.
    b = list(filter(lambda x: x % 2 == 1, a))
    print(b)

    # Passing a list to a function allows the function to modify the elements of the list, because of the way that
    # Python deals with lists and other data structures.
    a = list(range(5))
    print('Before:', a)
    do_something(a)
    print('After:', a)