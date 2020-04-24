#!/usr/bin/env python3


import matplotlib.pyplot as plt
from time import time


def time_lookup(d):
    """
    Time how long a loopup takes in a data structure.
    :param d: The data structure.
    :return: The elapsed time.
    """
    start_time = time()
    # -1 is guaranteed not to be there.  Force the check, but then do nothing.
    if -1 in d:
        pass
    end_time = time()

    # Return the elapsed time
    return end_time - start_time

if __name__ == '__main__':
    # Let's plot how long it takes to look up an entry that doesn't exist in a list and dictionary as the size
    # of the data structure increases increases

    # Pick some sizes to try
    sizes = [100 * x for x in range(100)]

    list_times = []
    set_times = []
    for s in sizes:
        # Make a list and set of the right size
        l = list(range(s))
        s = set(range(s))

        # Figure out the timing for
        list_times.append(time_lookup(l))
        set_times.append(time_lookup(s))

    # Plot the results.  This time we're going to store the first thing in the tuple that the plot function
    # returns.  This will let us build a legend for the plot.  Note the comma on the left hand side.  This
    # tells Python to unpack the sequence that plot returns, and assign the first thing in this sequence to
    # the variable.  Plot returns a sequence of line segements, and we only need the first of these.
    list_plot, = plt.plot(sizes, list_times)
    set_plot, = plt.plot(sizes, set_times)

    # Build a legend for the plot.  The first argument is a list of the handles for the lines that plot
    # returned, and the second is a list of text labels for the legend.
    plt.legend([list_plot, set_plot], ['list', 'set'])


    # Label the axes and set a title
    plt.title('Lookup times')
    plt.xlabel('elements in data structure')
    plt.ylabel('time (seconds)')

    # Display the plot
    plt.show()


