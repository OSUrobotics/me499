#!/usr/bin/env python3


# You can import all of numpy/scipy or just a subset. Here we import all of numpy (requiring all
# calls to numpy to be tagged by np) and just one method from scipy.
# If you just need one or two methods, just import those methods (otherwise you have to import a LOT of stuff)
# If you're using a lot of the functionality of numpy, then import all of the methods
# Note that scipy has a lot of sub packages (optimze, Fourier transforms, etc) and you can import just a method
#  from one package (as shown below) or import the entire sub package
import numpy as np
from scipy.optimize import fmin


def my_func(t):
    x = np.sin(t) * np.cos(2*t)
    return x


if __name__ == '__main__':
    # Make an n-dimensional array filled with zeros
    my_zero_nd_array = np.zeros([2, 3])  # A 2 x 3 matrix

    # Make an nd array from a list
    my_array = [t * np.pi / 3.0 for t in range(0, 100)]
    my_nd_array = np.array(my_array)

    # You can also put this in a single statement
    my_nd_array_2 = np.array([t * np.pi / 3.0 for t in range(100)])

    # Element-wise operations work for nd arrays
    my_nd_array_res = my_nd_array * 3.0 + 3.0

    # Boolean operations return arrays
    my_array_check = abs(my_nd_array_res) < 7
    print(my_array_check)

    # Make a list from an ndarray
    my_list = list(my_nd_array_res)

    # linspace and arange
    my_t_array = np.linspace(0, 2 * np.pi, 100)
    my_t_array_2 = np.arange(0, 2 * np.pi, 0.01)

    # numpy operations can apply to entire arrays.  Notice that this sin() is different from the one
    # you would import from the math module.
    my_s_array = np.sin(2.0 * my_t_array)

    # Matrix operations - notice the @ instead of *
    my_matrix = np.identity(4)
    my_vector = np.ones([4, 1])
    my_vector_mult = my_matrix @ my_vector  # This is a matrix multiply

    # An example of calling fmin
    x_min = fmin(np.sin, np.pi / 3.0)  # Sin function, start at pi/3
    print("Minimum value of sin: {0}".format(x_min))

    x_min = fmin(my_func, np.pi / 3.0)  # Modified sin function
    print("Minimum value of my func: {0}".format(x_min))
