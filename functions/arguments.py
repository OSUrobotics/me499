#!/usr/bin/env python3


# Functions arguments can have default values.  If the caller does not give values for these arguments, the default
# values are used instead.  The arguments without defaults (a in this case) have to appear before those with defaults
# (b and c in this case).
def foo(a=0, b=0, c=0):
    """
    A simple function to show default argument values.

    :param a: The first argument.
    :param b: The second argument.
    :param c: The third argument.
    :return: None
    """
    print('foo():\n  a = {0}\n  b = {1}\n  c = {2}'.format(a, b, c))


# Functions can also take an unspecified number of arguments.  You can do this by putting a * before the argument name,
# which is typically called args (although you can call it anything you like).  The arguments are available as a tuple
# from inside the function.
def bar(*args):
    """
    A simple function to illustrate how functions can take arbitrary number of arguments.

    :param args: The arguments to the function.
    :return: None
    """
    print('bar():', args)


# Functions can also take an unspecified number of arbitrary keyword arguments.  YOu can do this by putting **before
# the argument name, which is kwds by convention.  These are available in the function as a dictionary, where the keys
# are the keyword names (as a string), and the values are the argument values.
def baz(**kwds):
    """
    A simple function to illustrate how functions can take an arbitrary number of keyword arguments.

    :param kwds: The arguments to the function.
    :return: None
    """
    print('baz():', kwds)


# You can combine all of these things together.  Non-defaulted arguments come first, then defaulted values, then
# arguments, then keyword arguments.
def everything(a, b, c=0, *args, **kwds):
    """
    A simple function to illustrate how different argument types can eb combined.

    :param a: A regular argument.
    :param b: A regular argument.
    :param c: A an argument with a default value.
    :param args: An arbitrary number of other arguments.
    :param kwds: An arbitrary number of keyword arguments.
    :return: None
    """
    print('everything():  a = {0}\n  b = {1}\n  c = {2}\n  args = {3}\n  kwds = {4}'.format(a, b, c, args, kwds))

    # You can get to the specific arguments as a tuple (as in the print statement) or using a for loop
    print('everything() args:')
    for a in args:
        print(' ', a)

    # If you're accessing them directly, you should put things in a try block, since you can't guarantee how many
    # arguments you'll have.  Since it's a tuple, problems will raise an IndexError.
    try:
        print('everything() first args:', args[0])
    except IndexError:
        print('everything() no args!')

    # For the keyword args, you can access them like a dictionary,  kwds['a'], or using a for loop
    print('everything() kwds:')
    for (k, v) in kwds.items():
        print('  {0} => {1}'.format(k, v))

    # As for args, put direct accesses in a try block that catches KeyErrors:
    try:
        print('everything() keyword foo:', kwds['foo'])
    except KeyError:
        print('everything() no keyword argument foo!')


if __name__ == '__main__':
    # The function foo can take between zero and three arguments.
    foo()
    foo(1)
    foo(1, 2)
    foo(1, 2, 3)

    # We can also specify which particular arguments we want to assign values to.  All of the other arguments get
    # their default values.
    foo(b=12)

    # bar() can take any number of arguments.
    bar()
    bar(1)
    bar(1, 2)
    bar(1, 2, 3)

    # baz() can take any number of keyword arguments
    baz()
    baz(a=1)
    baz(a=1, b=2)

    # Everything, all at once
    everything(1, 2)
    everything(1, 2, 3)
    everything(1, 2, 3, 4, 5, 6)
    everything(1, 2, 3, 4, 5, 6, x=1, y=2, z=2)
