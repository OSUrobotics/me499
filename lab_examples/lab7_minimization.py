from scipy.optimize import fmin
from functools import partial

def my_func(x):
    return (x-2)**2 - 3

def elliptic_paraboloid(x, y, x0, y0, a, b):
    return (x-x0)**2 / a**2 + (y-y0)**2 / b**2

# Want x0 = 3, y0 = 2, a = 4, b=16
# my_paraboloid = lambda x,y: elliptic_paraboloid(x, y, x0=3, y0=2, a=4, b=16)
my_paraboloid = partial(elliptic_paraboloid, x0=3, y0=2, a=4, b=16)

result = fmin(lambda array: my_paraboloid(array[0], array[1]), [0, 0], maxfun=200, full_output=True)
print(result)