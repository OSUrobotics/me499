#!/usr/bin/env python3


if __name__ == '__main__':
    # A much better way of dealing with files is to use the with construct.  This will automatically close the file
    # when you're done with it, so you don't have to worry about remembering to do it.  You shoudl always use this
    # approach.  This example writes numbers and their squares to a file.
    with open('second_example_file', 'w') as f:
        for i in range(10):
            f.write('{0} {1}\n'.format(i, i * i))

    # Now, we can read in the numbers again.  They are read in as strings, so we need to convert them to integers if
    # we're going to use them.
    with open('second_example_file', 'r') as f:
        # For each line in the file
        for line in f:
            # Take the line, and split it into a list, based on spaces.  Then, use map to apply the int() function to
            # each of the elements of this list, turning it from a string to an integer.  Then, assign n and squared
            # to be the first two elements of this list of integers.  This is a very Pythonic way to do this.  There
            # are others, which might be clearer to read
            (n, squared) = map(int, line.split())

            # We're just going to print these out for now, along with their types.
            print('{} ({}) -> {} ({})'.format(n, type(n), squared, type(squared)))

    # Even better than this is to wrap the with block in a try-except block, in case there's a file error.  There are
    # a number of exceptions that open can raise and, to be safe, you should have an exception handler for each of
    # them.
    try:
        with open('this_file_does_not_exist', 'r') as f:
            # We're not going to do anything in this example, since we're just showing the exception behavior
            pass
    except FileNotFoundError:
        print('Could not find the file!')