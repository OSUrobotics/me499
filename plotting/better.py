#!/usr/bin/env python3


# Import the basic plotting package
import matplotlib.pyplot as plt

# Get some things from numpy.  The numpy sin function allows us to apply sin to an array of numbers all at once,
# rather than one at a time.  Don't worry much about this for now, since we'll talk about it more when we cover
# numpy in more detail.
from numpy import arange, sin, pi

if __name__ == '__main__':
    # A better use of plot is to give it both the x and the y values, so that the x-axis scale is correct.
    x = arange(0, 2 * pi, 0.01)
    y = sin(x)
    plt.plot(x, y)

    # We can put a title on the graph, and label the axes
    plt.title('A sine curve')
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # You can also save this to a file.  Matplotlib will figure out the right file type based on the filename
    # extension.
    plt.savefig('sine.png')

    # We'll only see the graph when you run show().  The program will stop here, until you kill the plot window.
    plt.show()