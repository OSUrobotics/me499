#!/usr/bin/env python3


# Import the csv (comma separated values) module
import csv


def write_my_csv(fname, data):
    """ Write the data out to a file
    :param fname a string for the file fname
    :param data - an iteratable list of iterable objects
    """
    with open(fname, 'w') as f:
        csv_file = csv.writer(f)
        for datum in data:
            # Write a row of data, represented by a tuple in this case, to the file.
            csv_file.writerow(datum)


def read_my_csv_pedantic(fname):
    """ Read the file back in again
    :param fname name of the file
    :returns a list of tuples
    """

    # First open the file - notice the 'r' which means read
    with open(fname, 'r') as f:
        # This is a class that knows how to read in lines of
        #  text from a file - it needs a pointer to the file
        csv_file = csv.reader(f)

        # Place to put the data
        new_data = []
        new_data_fancy = []

        # Read in a row at a time, parsing out the elements.  Line is a list.
        for row in csv_file:
            # line is a list of strings.  You have to interpret what they are yourself.  In this case, we know that
            # they're integers, so we use map to apply the int function to each element of the list, then cast this
            # to a tuple.  Finally, we append this tuple to a list.
            new_row = []
            for r in row:
                make_int = int(r)
                new_row.append(make_int)
            new_data.append(tuple(new_row))

            # Note that you can do this in one line using
            #  map, which applies int(r) to each element r in row
            new_data_fancy.append(tuple(map(int, row)))

        # new_data and new_data_fancy are the same thing
        return new_data


def read_my_csv_fancy(fname):
    """ Read the file back in again
    :param fname name of the file
    :returns a list of tuples
    """
    # This first part is the same as above - open up the file
    #  for reading and create a csv reader

    # First open the file - notice the 'r' which means read
    with open(fname, 'r') as f:
        # This is a class that knows how to read in lines of
        #  text from a file - it needs a pointer to the file
        csv_file = csv.reader(f)

        # This is a more Pythonic (and elegant) way to do this.
        new_data = [tuple(map(int, row)) for row in csv_file]
    return new_data


if __name__ == '__main__':
    # Python has built-in support for csv files.  This is a good format for saving data, since it means you can
    # use the data in other programs, or import data from other programs.  The interface is similar to the file
    # interface that you already know.  More details: https://docs.python.org/3/library/csv.html

    # Generate some data.  We're going to make a list of tuples, representing numbers and their squares.  We're going
    # to use a list comprehension for this.
    data_to_write = [(n, n * n) for n in range(10)]

    write_my_csv('Squares.csv', data_to_write)
    data_read_from_file1 = read_my_csv_pedantic('Squares.csv')
    data_read_from_file2 = read_my_csv_fancy('Squares.csv')

    print(data_read_from_file1)
    print(data_read_from_file2)
