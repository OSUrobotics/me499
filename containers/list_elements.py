#!/usr/bin/env python3


if __name__ == '__main__':
    # Make a list of all the even numbers from -10 to 10
    a = [2 * i for i in range(-5, 6)]
    print(a)

    # You can print out these values with a for loop
    for e in a:
        print(e)

    # The loop variable is a copy of the element of the array.  This means that you can't modify it.
    print(a)
    for e in a:
        e = 1  # This only modifies the local copy.
    print(a)

    # If you want to change the elements, that you need to iterate over the indexes.
    print(a)
    for i in range(len(a)):
        a[i] = 1
    print(a)