from scipy.optimize import fmin
from functools import partial


# A generic function that we want to find the minimum of
def my_func(x):
    """A quadratic function
    :param x the input x value
    :returns f(x)"""
    return (x-2)**2 - 3


# A fancier quadratic-y type function (but in 2D)
def elliptic_paraboloid(x, y, x0, y0, a, b):
    """ x,y -> f(x) in the shape of a 'bowl'
    :param x - x value in the plane
    :param y - y value in the plane
    :param x0 - amount to shift the bottom of the bowl by in x
    :param y0 - amount to shift the bottom of the bowl by in y
    :param a - scale the bowl's side in x
    :param b - scale the bowl's side in y
    :returns - f(x,y) the bowl's height over the point x,y
    """
    return (x-x0)**2 / a**2 + (y-y0)**2 / b**2


if __name__ == '__main__':
    # Use fmin to find the minimum of my_func
    # The _ says ignore that returned value
    # Note that x_at_min is a list - in this case, a list of dimension 1
    #    The full_output=True prints out the optimization result to the console
    x_at_min, f_at_x_min, _, _, _ = fmin(my_func, 0.2, maxfun=100, full_output=True)
    print("Minimum of f is {0}, happens at x={1}".format(f_at_x_min, x_at_min[0]))
    print("Checking fmin result {0} against func eval {1}".format(f_at_x_min, my_func(x_at_min[0])))

    # This does the same thing
    #   See https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html
    #   for what the remaining values are
    f_min_ret_vals = fmin(my_func, 0.2, maxfun=100, full_output=True)
    x_at_min_2 = f_min_ret_vals[0][0]
    fx_at_min_2 = f_min_ret_vals[1]
    print("Minimum of f is {0}, happens at x={1}".format(fx_at_min_2, x_at_min_2))

    # Now going to do the 2 dimensional version of a parabaloid
    # Because the function definition has all these extra parameters that
    #  control the shape of the function (x0, etc), we have do what's called
    #  "binding" the variables to values, in this case x0 = 3, y0 = 2, a = 4, b=16
    # partial is a functools method to do this, which has the advantage over a lambda
    #  function of creating a python function that is more "efficient" because it
    #  "freezes" the constant parameters
    # partial takes the function elliptic_paraboloid and "binds" all of the named
    #   parameter arguments
    my_paraboloid = partial(elliptic_paraboloid, x0=3, y0=2, a=4, b=16)
    print("My parabaloid at 3,4: {0}, check {1}".format(my_paraboloid(3, 4), elliptic_paraboloid(3, 4, 3, 2, 4, 16)))

    # Almost done - fmin takes a function that takes in one argument (a list of dimension d)
    #  and outputs one number. Our my_paraboloid function currently takes in x,y, not [x,y].
    # Lambda functions fix that: In this case, it says make a new (temporary, unnamed function)
    #  that takes in one parameter (array) and calls my_paraboloid with array[0] and array[1]
    result = fmin(lambda array: my_paraboloid(array[0], array[1]), [0, 0], maxfun=200, full_output=True)
    print(result)
    print("Function minimum is {0}, found at {1}".format(result[1], result[0]))

    # You shouldn't really do this, because lambda functions are suppose to be unnamed,
    #  but this will show you what the lambda did
    my_func_2D = lambda array: my_paraboloid(array[0], array[1])
    # Notice that my_func_2D takes a list of two numbers, my_parabaloid takes 2 numbers
    print("Call my_parabaloid with 3, 4: {0} {1}".format(my_func_2D([3, 4]), my_paraboloid(3, 4)))
