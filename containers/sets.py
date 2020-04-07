#!/usr/bin/env python3


if __name__ == '__main__':
    # Sets are like dictionaries with no values.  They behave just like mathematical sets.
    # https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    a = set()
    b = {1, 2, 3, 2, 1}  # Notice that this gets rid of duplicates.
    print(a, b)

    # You can use sets in a for loop
    a = {1, 2, 3}
    for x in a:
        print(x, end=' ')
    print()

    # You can add to sets and remove from them.
    a = {1, 2, 3}
    print(a)
    a.add('number')
    print(a)
    a.remove(2)
    print(a)

    # Sets have efficient intersections, unions, and differences
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a, b)
    print('Intersection:', a.intersection(b))
    print('Union:', a.union(b))
    print('Difference:', a.difference(b), b.difference(a))
