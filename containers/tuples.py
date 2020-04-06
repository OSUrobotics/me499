#!/usr/bin/env python3


if __name__ == '__main__':
    # Tuples are similar to lists, but are immutable.  That means you can't change their elements.
    a = ()
    b = (1,)      # This needs a comma after the single element.  If you leave the comma out, Python will treat the
                  # the parentheses as arithmetic, and assign the value of 1 to b.
    c = (2, 'x')
    d = tuple()
    print(a, b, c, d)

    # Getting to the elements of a tuple works just like a list.
    a = (5, 4, 3, 2, 1)
    print(a[2])

    # You can't assign to a tuple, though.  Uncomment the next line to see what happens.
    #a[2] = 'X'

    # You can't do tuple comprehensions (because these involve building things one element at a time), but you can
    # do a list comprehension and cast it to a tuple.  The if clause in this example, uses the fact that a zero
    # can be interpreted as a False to create a tuple of odd numbers.
    a = tuple([i for i in range(20) if i % 2])
    print(a)
