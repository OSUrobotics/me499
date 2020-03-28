#!/usr/bin/env python3


# This is an example of a simple function.  This doesn't take any arguments, and always returns the value 2.  This is
# not a very useful function, but it does show the general syntax.  Note the comment with triple quotes as the first
# line of the function body.  This is the docstring, which is used by Python to document what it does.  You can find
# out a lot more about docstrings here: https://www.python.org/dev/peps/pep-0257/
# There's no single format for docstrings, but one of the conventions is to add the parameters and the return values
# prepended with a colon (:).  This allows documentation for the function to be automatically generated (using Sphinx,
# in this case, https://www.sphinx-doc.org/en/master/)
def foo():
    """
    This function takes no arguments, and always returns the value 2.

    :return 2
    """
    return 2


# This function takes a single argument and returns double that value.
def double(n):
    """
    Returns double the value of the argument
    :param n: Number to be doubled
    :return: Double the value of the input, n
    """
    return n * 2


# Functions don't need to return anything.  In this case, the function actually returns None, which is special value.
# This function just prints out its argument using the built-in print function.  Again, this is not a very useful
# function, since it just wraps around print, and doesn't do anything else.
def print_wrapper(s):
    print(s)


if __name__ == '__main__':
    # This prints out information about the function, from the docstring.
    help(foo)

    # The double function works on numbers.  Note that we can pass multiple arguments to the built-in print function.
    print('Doubling:', 2, double(2))

    # Python doesn't care about types.  That means the double function will work for anything that can have the *
    # operator applied to it.  What happens, depends on what the operator does.  For example, for strings, * returns
    # multiple copies of the string.
    print('Doubling strings:', 'hello', double('hello'))
