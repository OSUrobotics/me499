#!/usr/bin/env python3


if __name__ == '__main__':
    # Lists are a basic data structure in Python.  Here are a couple of ways to create them.
    a = []
    b = [1, 2, 3]
    c = list()
    print(a, b, c)

    # You access a list by using subscripts.  The first element is element 0.  Negative indexes count from the end of
    # the list.
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[-1])

    # Assignment works as you would expect.
    a[2] = 'X'
    print(a)

    # You can also extract segments of lists using the slice mechanism.
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[1:3])  # Start at element 1, stop before you get to element 3.
    print(a[1:2])  # A single element, as a list.
    print(a[:-1])  # Everything but the last element.
    print(a[1:])   # Everything except the first element.

    # You can also assign to these ranges.
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = ['X', 'Y']  # Replace two elements with new values
    print(a)

    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = 'Z'  # Replace two elements with a single element.
    print(a)

    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = ['Z']  # The same effect as the previous example
    print(a)

    # List elements can have mixed types.  List elements can be other lists.
    a = [1, 2, 'a', 'b', [5, 6, 7], 10]
    print(a[-2])  # Second last element is itself a list

    # You can make a list from a range just by casting to the list type.
    a = list(range(10))
    print(a)

