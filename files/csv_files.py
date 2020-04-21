#!/usr/bin/env python3


# Import the csv (comma separated values) module
import csv


if __name__ == '__main__':
    # Python has built-in support for csv files.  This is a good format for saving data, since it means you can
    # use the data in other programs, or import data from other programs.  The interface is similar to the file
    # interface that you already know.  More details: https://docs.python.org/3/library/csv.html

    # Generate some data.  We're going to make a list of tuples, representing numbers and their squares.  We're going
    # to use a list comprehension for this.
    data = [(n, n *n) for n in range(10)]

    # Write these data to a csv file
    with open('squares.csv', 'w') as f:
        csv_file = csv.writer(f)
        for datum in data:
            # Write a row of data, represented by a tuple in this case, to the file.
            csv_file.writerow(datum)

    # Read in the data from the file
    with open('squares.csv', 'r') as f:
        csv_file = csv.reader(f)
        new_data = []

        #Read in a row at a time, parsing out the elements.  Line is a list.
        for row in csv_file:
            # line is a list of strings.  You have to interpret what they are yourself.  In this case, we know that
            # they're integers, so we use map to apply the int function to each element of the list, then cast this
            # to a tuple.  Finally, we append this tuple to a list.
            new_row = []
            for r in row:
                make_int = int(r)
                new_row.append(make_int)
            new_data.append(tuple(new_row))
            new_data.append(tuple(map(int, row)))

        # This is a more Pythonic (and elegant) way to do this.  Comment out the for loop and code block, and
        # uncomment this line to see it in action.
        #new_data = [tuple(map(int, row)) for row in csv_file]

        print(new_data)
