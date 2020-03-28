#!/usr/bin/env python3


if __name__ == '__main__':
    # The for statement loops over any iterable.  This can be a list.
    for i in [1, 3, 'hello']:
        print(i)

    # Or it can be a generator function, like range.
    print()
    for i in range(5):
        print(i)

    # You can nest for loops
    print()
    for x in range(3):
        for y in range(3):
            print(x, y)

    # You can pull things apart in for loops over iterables of containers.
    print()
    for (a, b) in [(1, 2), (3, 4), ('five', 'six')]:
        print(a, b)

    # This also works over dictionaries, using items()
    print()
    d = {1:'un', 2:'deux', 3:'trois'}
    for (k, v) in d.items():
        print('{0} => {1}'.format(k, v))

    # Just using the dictionary in the for look (without items()) will iterate over the keys.
    print()
    for k in d:
        print(k)

    # You can also iterate over the values.  There's also a keys() function.
    print()
    for v in d.values():
        print(v)

    # Text strings are also iterables:
    print()
    for c in 'hello':
        print(c)