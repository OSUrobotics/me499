#!/usr/bin/env python3


# Import the basic plotting package
#   plt has all of the plotting commands - all of your plotting will begin with ply.[blah]
#   To have this behave more like MatLab, do
# import matplotlib.pyplot
#    in which case the plt scoping isn't needed
import matplotlib.pyplot as plt

# Get some things from numpy.  The numpy sin function allows us to apply sin to an array of numbers all at once,
# rather than one at a time.  Don't worry much about this for now, since we'll talk about it more when we cover
# numpy in more detail.
from numpy import arange, sin, pi

if __name__ == '__main__':
    # This shows the basic plotting functionality.  plot() can take an iterable, and will plot the values in it.
    # It will assume that the x-values are 0, 1, 2, and so on.  In this example, we're plotting a sine function
    # from 0 to 2 * pi, in increments of 0.01. The x-axis, however, (since you didn't specify it) will go from
    # 0 to the number of points (around 500). See better.py to specify both x and y
    plt.plot(sin(arange(0, 2 * pi, 0.01)))

    # Note that functionality differs depending on if you're running in the debugger and what operating system you're
    # using. In debug/interactive mode, the window may show up when you do the plot command. In non-interactive
    # mode it won't show up until you do show
    # We'll only see the graph when you run show().  The program will stop here, until you kill the plot window.
    #   If you want the window to stay up when you step over this line in the debugger, use this instead:
    # plt.show(block=True)
    plt.show()
