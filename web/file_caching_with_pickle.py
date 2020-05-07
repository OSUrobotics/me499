#!/usr/bin/env python3


import pickle
from random import randint
from os import path


def expensive_function_creates_data(n):
    """ A silly bit of code that makes random lists, sorts them, then stuffs them in a dictionary
        with the key being their smallest value """
    my_data = {}
    for _ in range(0, n):
        my_list = sorted([randint(0, 2 * n) for _ in range(0, n)])
        my_data[my_list[0]] = my_list
    return my_data


def get_expensive_data(n, name="data/save_data", b_recalc=False):
    """
    Check to see if file exists, and if so, read it in
    @param n: parameter for the expensive function
    @param name: File name to use (the base part of the name)
    @param b_recalc: Force recalculation, y/n
    """
    my_fname = "{0}_{1}.bin".format(name, n)
    # The two cases we want to recalculate
    if b_recalc or not path.exists(my_fname):
        my_data = expensive_function_creates_data(n)
        # Save it for next time - note that this is a binary file, not a text file, so use the b
        with open(my_fname, 'wb') as f:
            pickle.dump(my_data, f)

        # Return the data
        return my_data

    # Read it in, since it exists
    with open(my_fname,'rb') as f:
        my_data = pickle.load(f)
    return my_data


if __name__ == '__main__':
    n = 1500
    get_data = get_expensive_data(n, "data/save_data", False)

    # You'll notice
    print("First element {0}".format(', '.join([str(k) for k in get_data.keys()])))
