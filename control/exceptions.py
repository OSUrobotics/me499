#!/usr/bin/env python3


def exceptor():
    """
    This function just raises an exception.

    :return: None
    """

    # Raise an exception with the raise statement.  Try raising different exceptions, to see what the effects on the
    # try-except-else block in this file.  These three exceptions are all built-in exceptions in Python.  More
    # information is available here: https://docs.python.org/3/library/exceptions.html
    raise ValueError
    #raise IndexError
    #raise TypeError


if __name__ == '__main__':
    # This is the basic syntax of an exception handler.  If an exception is raised in the try block (or in any
    # function called from it, it is passed to the associated except blocks.
    try:
        print('Before function')
        #exceptor()
        print('After function')
    # This will catch all ValueErrors.  You should specify a specific exception here, usually one of the built in
    # ones.  If an exception is raised, and there's no corresponding except block, then the exception is passed to
    # the next higher enclosing block of code.  Eventually, if there's nothing that catches the exception, Python
    # will stop and report the exception.
    except ValueError:
        print('Caught a ValueError')
    # This will catch an IndexError
    except IndexError:
        print('Caught an IndexError')
    # If no exceptions are caught by the except block, the the else block will run.
    else:
        print('Did not catch an exception')

    print('After the try-except block')