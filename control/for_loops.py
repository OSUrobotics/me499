#!/usr/bin/env python3


if __name__ == '__main__':
    # The for statement loops over any iterable.  This can be a list.
    #  e will take on 1, 3, then 'hello'
    my_list = [1, 3, 'hello']
    for e in my_list:
        print(e)

    # Or it can be a generator function, like range.
    print()
    for i in range(5):
        print(i)

    # You can get the index out using the enumerate function
    #  in this case, i gets the index, e gets the element
    print()
    for i, e in enumerate(my_list):
        print("Element {0} is at index {1}".format(e, i))

    # You can also "zip" two lists together and loop over *both* at the same time
    print()
    my_range = range(3)   # A generator function that produces 0, 1, 2
    for e, r in zip(my_list, my_range):
        print("List item {0} and range item {1}".format(e, r))

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
    d = {1: 'un', 2: 'deux', 3: 'trois'}
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
