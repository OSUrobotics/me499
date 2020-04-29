#!/usr/bin/env python3

def triple(a=None, b=None, c=None):
    """
    A simple function that takes three arguments, which default to None.
    :param a: First argument.
    :param b: Second argument.
    :param c: Third argument.
    :return: None
    """
    print('triple():')
    print('  a: ', a)
    print('  b: ', b)
    print('  c: ', c)


def print_point(x, y):
    print('Point is ({0}, {1})'.format(x, y))


if __name__ == '__main__':
    # This is a traditional function call.
    triple(1, 2, 3)

    # If we have an iterable, like a list, then we can unpack this into the function arguments using the
    # * operator.  Look at the different effects of these two calls.
    l = [4, 5, 6]
    triple(l)
    triple(*l)

    # Unpacking consumes the whole list, so beware of the number of arguments.  Uncomment these two lines
    # to see if fail because there are too many arguments
    #l = [1, 2, 3, 4, 5, 6]
    #triple(*l)

    # This often used to use functions that expect a set of individual arguments with data structures that
    # that combine these together.  Think about a point, represented as a tuple (x, y).  There are two ways
    # to pass this to the print_point() function.  The first is explicitly unpack the point:
    point = (1, 2)
    print_point(point[0], point[1])

    # But, it's a bit more compact and readable to use the star operator.  These two ways of doing it are
    # exactly the same, but this second one is a little more compact, and you're less likely to type it
    # wrong.
    print_point(*point)