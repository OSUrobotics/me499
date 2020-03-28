#!/usr/bin/env python3

# This is the traditional first program that you write in a new language.  All it does when you run it is print
# Hello, World!  Notice the comment line above this one.  This tells the computer that the stuff in this file is a
# Python program, and specifically a Python 3 program.  While you don't need this when you're using an IDE like
# Pycharm, it is needed if you run this program outside of the IDE, from the command line for example.  All Python
# scripts should have this line.

# This if statement checks to see if the file is being invoked as a program, or if it's being included by some other
# file using the import statement.  If it's being run as a program, then the expression in the if statement evaluates
# to True, and the stuff in the indented block below it runs.  All Python scripts should have this line.
if __name__ == '__main__':
    # This block is indented one level, since it's in the scope of the if statement.  If you don't indent things
    # correctly, this is a syntax error and your code will not run.

    # Print is a built-in function in Python.  It prints the arguments that you give it out to the screen.  In this
    # case, we're just printing a string of text.  Python will add a newline after whatever you're printing.
    print('Hello, World!')
