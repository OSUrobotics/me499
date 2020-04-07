#!/usr/bin/env python3


from collections import OrderedDict


if __name__ == '__main__':
    # Ordering is not guaranteed for sets and dictionaries.  If you need to guarantee ordering, then use an OrderedDict.
    # The interface is the same as their non-ordered versions.  There is no ordered set.
    d = OrderedDict()
    d[1] = 'one'
    print(d)

    # You can sort containers using the sorted function.  This returns a list.
    a = {3, 2, 1}
    print(type(a), a)
    b = sorted(a)
    print(type(b), b)

    # If you start with a list, you can also sort it in place, using sort.
    a = [3, 2, 4, 1, 4]
    print(a)
    a.sort()
    print(a)
