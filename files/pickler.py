#!/usr/bin/env python3


# Import the pickle module.
import pickle


if __name__ == '__main__':
    # Python also has a built-in system to save arbitrary data structures to a file, called pickling.  The interface
    # is similar to the file interface.  The advantage is that Python knows how to turn data structures into files
    # and back again, so you don't have to interpret the data in the files yourself.  The downside is that the files
    # are not human-readable, so you can't check their contents without reading them into Python.  More details on
    # pickling are here: https://docs.python.org/3/library/pickle.html
    # Make sure you read the warning on this web page.  Unpickling a file that you did not pickle yourself is
    # dangerous, since there's a way to have this process run arbitrary Python code on your computer.  DO NOT
    # unpickle files if you don't know what's in them.

    # This is an arbitrary data structure, involving lists, tuples, and a dictionary.
    data = [1, 2, 'three', (4, 5, 6), {1: 'one', 2: 'two'}]
    print('Original:', data)

    # First, open a file to write to.  This needs to be opened as 'wb' since we're writing binary data to it.
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    # To read the data back in, it's a similar process.  Again, open if for binary data reading with 'rb'
    with open('data.pickle', 'rb') as f:
        new_data = pickle.load(f)

    print('Loaded:  ', new_data)
