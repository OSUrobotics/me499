#!/usr/bin/env python3


import matplotlib.pyplot as plt
from numpy import arange

if __name__ == '__main__':
    x = arange(0, 10, 1)

    # We can change the color and the type of the line.  You do with the string argument in the call below.
    # The r means red, and the -- means dashed line.  There are a number of these, and there are some examples
    # in this file.  There are full details of the options in the matplotlib documentation at:
    # https://matplotlib.org  There's also a great tutorial at:
    # https://matplotlib.org/tutorials/introductory/pyplot.html
    plt.plot(x, x, 'r--')
    plt.plot(x, x**2, 'bs')
    plt.plot(x, x**3, 'g^')

    # Display it on the screen
    plt.show()
