#!/usr/bin/env python3


if __name__ == '__main__':
    # Lists are a basic data structure in Python.  Here are a couple of ways to create them.
    a = []
    b = [1, 2, 3]
    c = list()
    print(a, b, c)

    # You access a list by using subscripts.  The first element is element 0.  Negative indexes count from the end of
    # the list.
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])  # Print the first element of the list
    print(a[1])  # Print the second element of the list
    print(a[-1]) # Print the last element of the list
    print(a[-2]) # Print the second to last element of the list

    # Assignment works as you would expect.
    a[2] = 'X'
    print(a)

    # You can also extract segments of lists using the slice mechanism.
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[1:3])  # Start at element 1, stop before you get to element 3.
    print(a[1:2])  # A single element, as a list.
    print(a[:-1])  # Everything but the last element.
    print(a[1:])   # Everything except the first element.

    # You can also assign to these ranges.
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = ['X', 'Y']  # Replace two elements with new values
    print(a)

    # In general, the syntax a[start:stop] = element or list means
    #  take the elements start:stop out and replace them with what's on
    #  the right hand side. If it's an element, this just puts the one
    #  element in
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = 'Z'  # Replace two elements with a single element.
    print(a)

    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = ['Z']  # The same effect as the previous example
    print(a)

    # If it's a list, then it inserts the list into that spot
    #   i.e., a[1] will be X, a[2] will be Y, a[3] will be Z,
    #   and all the elements from the original a[3] on will be
    #   shifted to the right
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = ['X', 'Y', 'Z']  # Replace two elements with a single element.
    print(a)

    # List elements can have mixed types.  List elements can be other lists.
    a = [1, 2, 'a', 'b', [5, 6, 7], 10]
    print(a[-2])  # Second last element is itself a list

    # You can make a list from a range just by casting to the list type.
    r = range(10)
    a = list(r)
    print(a)

    # If you have a list and you want to extend
    # a current list by that list
    #   a = ['a', 'b']
    #   b = ['c', 'd']
    #   ab = ['a', 'b', 'c', 'd']
    # Then use ab = a.extend(b) or ab = a + b
    a_list_append = []
    a_list_concatenate = []
    a_list_extend = []
    for i in range(0, 10):
        l = [j for j in range(0, i)]
        a_list_append.append(l)
        # The following are identical: + calls extend
        a_list_concatenate = a_list_concatenate + l
        a_list_extend.extend(l)
    print(a_list_append)
    print(a_list_concatenate)
    print(a_list_extend)

