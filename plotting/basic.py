#!/usr/bin/env python3


# Import the basic plotting package
import matplotlib.pyplot as plt

# Get some things from numpy.  The numpy sin function allows us to apply sin to an array of numbers all at once,
# rather than one at a time.  Don't worry much about this for now, since we'll talk about it more when we cover
# numpy in more detail.
from numpy import arange, sin, pi

if __name__ == '__main__':
    # This shows the basic plotting functionality.  plot() can take an iterable, and will plot the values in it.
    # It will assume that the x-values are 0, 1, 2, and so on.  In this example, we're plotting a sine function
    # from 0 to 2 * pi, in increments of 0.01.
    plt.plot(sin(arange(0, 2 * pi, 0.01)))

    # We'll only see the graph when you run show().  The program will stop here, until you kill the plot window.
    plt.show()
