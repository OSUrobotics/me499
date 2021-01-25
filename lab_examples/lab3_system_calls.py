#!/usr/bin/env python3

# This is the library that lets you do system (terminal) calls
#   eg get arguments off of the command line, manipulate directories
#   and files, etc.
import sys
from os.path import basename

# To run this script, pick "terminal" in the bottom of PyCharm (instead of Run
# or Python Console)
# Try: python lab_examples/lab3_systems_calls.py
#    This starts python, tells it to run the script lab_examples/lab3_systems_calls.py
#       You have to use the path name from the current directory
#       which is me499
# Now try adding arguments
if __name__ == '__main__':
    # Need two file names, which means 3 arguments in the list.  If we don't get this, then print out a usage
    # Message and return a 1 to the operating system.
    #  argv[0] is always the program name
    #  eg python input1 input2
    if len(sys.argv) < 2:
        # basename is a useful way to get final filename in a path
        print('Usage: {0} input1 input2 etc'.format(basename(sys.argv[0])))
        # This ends the program
        exit(1)

    print("Got {0} arguments to command {1}".format(len(sys.argv) - 1,basename(sys.argv[0])))
    for my_input in sys.argv[1:]:
        print("Got: argument {0}".format(my_input))

    print()
