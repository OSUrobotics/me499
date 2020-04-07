#!/usr/bin/env python3


if __name__ == '__main__':
    # Dictionaries store pairs of things, a key and a value.  Keys have to be unique, but you can have replicated
    # values.  Here are a few ways to create dictionaries.
    # https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    a = {}
    b = {1: 2}  # The key is 1, the value is 2
    c = {2: 'two', 'word': 'stuff'}  # 2 elements, 1st key is 2, value is 'two', 2nd key is 'word', value is 'stuff'
    d = dict()
    print(a, b, c, d)

    # You access the elements of the dictionary like this
    a = {'one': 1, 'two': 2, 'couple': 2}
    print(a['one'])

    # You can add a new element like this
    print(a)
    a['three'] = 3
    print(a)

    # And delete like this
    del a['one']
    print(a)

    # If the element already exists, then assignment changes the value
    print(a)
    a['one'] = 123
    print(a)

    # You can construct dictionaries with dictionary comprehensions.  These work just like list comprehensions.  This
    # example will build a dictionary of numbers and their squares.
    a = {x: x * x for x in range(10)}
    print(a)

    # Here's another example, also showing the use of the zip function.  This is not how you would do this for real,
    # but it's a good example of how you can build dictionaries from lists.
    a = list(range(10))
    b = [x * x for x in a]
    c = {k: v for (k, v) in zip(a, b)}
    print(c)

    # You can use dictionaries with for loops like this:
    a = {x: x * x for x in range(10)}
    for (k, v) in a.items():
        print('{0} -> {1}'.format(k, v))

    # You can also iterate over the keys or the values.  If you just iterate over the dictionary, then you get the keys.
    a = {'one': 1, 'two': 2, 'couple': 2}
    print('just dictionary: ', end='')
    for x in a:
        print(x, end=' ')
    print('\nkeys(): ', end='')
    for x in a.keys():
        print(x, end=' ')
    print('\nvalues(): ', end='')
    for x in a.values():
        print(x, end=' ')
    print()
