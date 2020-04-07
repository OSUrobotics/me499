#!/usr/bin/env python3


from random import randint
from collections import Counter


def roll():
    """
    Simulate the roll of two 6-sided dice.
    :return: The sum of the two dice.
    """
    return randint(1, 6) + randint(1, 6)


if __name__ == '__main__':
    # Generate a list of 1,000,000 rolls
    values = [roll() for _ in range(1000000)]

    # How many of each value?  Store this in a dictionary.
    count = {}
    for v in values:
        try:
            # Try to increment the value in the dictionary.
            count[v] += 1
        except KeyError:
            # We get a KeyError if the value isn't in the dictionary.  This means that it's the first time we've seen
            # this key, so the count is 1.
            count[v] = 1

    # Print out the counts, ordering by the keys:
    print('Hand Coded:')
    for k in sorted(count.keys()):
        print('  {0:2}: {1}'.format(k, count[k]))

    # Since this is a very common use case, there's a built in version of a dictionary to do this.  The constructor
    # does all the work for you.
    c = Counter(values)
    print('Counter:')
    for k in sorted(c.keys()):
        print('  {0:2}: {1}'.format(k, count[k]))

    # Any element that hasn't been seem has a count of zero, rather than raising a KeyError, like a standard dictionary
    # would.
    print('\n100:', c[100])
