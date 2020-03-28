#!/usr/bin/env python3


if __name__ == '__main__':
    # Open a file.  The second argument means we're opening the file to write to it.
    f = open('example_file', 'w')

    # Write something to the file.  You have to explicitly add the end of lines.
    f.write('This is a string\n')
    f.write('So is this\n')

    # You can't guarantee that things are written to the file until you close it.
    f.close()

    # You open for reading like this
    f = open('example_file', 'r')

    # You can read with f.read(), f.readline(), or use the more convenient for loop approach.  The end of line
    # character is included in the string that gets assigned to the line variable.
    for line in f:
        print(line)

    # Close the file again
    f.close()
