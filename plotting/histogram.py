#!/usr/bin/env python3


import matplotlib.pyplot as plt

from random import randint
from collections import Counter
from numpy import arange


if __name__ == '__main__':
    # How many dice to simulate, and how many rolls
    N = 2
    ROLLS = 1000000

    # Simulate rolling N 6-sided dice 1,000,000 times, recording the sum for each roll.
    count = Counter()
    for _ in range(ROLLS):
        count[sum(randint(1, 6) for _ in range(N))] += 1

    # Turn these counts into probabilities by dividing by the total number of rolls
    for k in count.keys():
        count[k] /= ROLLS

    # Make a sorted list of values and counts.  We're going to use a list comprehension, and sort by the
    # keys in the Counter (which is really a dictionary), and build a list of tuples, which are the sum
    # and the count
    data = [(key, count[key]) for key in sorted(count.keys())]

    # We can pull this into two lists, one for the number, and one for the counts, using the zip command.
    # The use of the star operator is a bit subtle.  data has the form [(k1, v1), (k2, v2), ...], and the
    # use of *data causes Python to unpack this, and present it to zip like: zip((k1, v1), (k2, v2), ...),
    # ie with a number of arguments.  zip() will take these and assemble these into an iterator over tuples,
    # where the first tuple is (k1, k2, ...) and the second is (v1, v2, ..).  Using the star operator on this
    # presents it to plot as two arguments, which bar interprets as x and y.  This is pretty confusing the
    # first time you see it, but it's a standard idiom in Python, and one you might end up using yourself.
    plt.bar(*zip(*data))

    # Set the title and axes labels
    plt.title('Probabilities of the sum of {0} 6-sided dice.\n({1} rolls)'.format(N, ROLLS))
    plt.xlabel('Sum of {0} dice.'.format(N))
    plt.ylabel('Probability')

    # Show the plot
    plt.show()
