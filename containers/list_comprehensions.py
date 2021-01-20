#!/usr/bin/env python3


from random import random


if __name__ == '__main__':
    # Instead of enumerating all of the items in a list, you can use a for loop to build one.  Start with an empty
    # list.
    a = []

    # This will build a list of the first 10 even numbers.
    for i in range(10):
        a.append(i * 2)
    print(a)

    # There's a more compact syntax for this, called a list comprehension.
    a = [2 * i for i in range(10)]
    print(a)

    # Here's a list of 5 random numbers, using the random() function
    a = [random() for _ in range(5)]
    print(a)

    # Same code as below but with if and for written out
    a = []
    for i in range(10):
        if i % 2 == 0:
            a.append(i)

    # You can put conditions on the list elements.  This builds a list of even numbers.
    a = [i for i in range(10) if i % 2 == 0]
    print(a)
