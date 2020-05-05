#!/usr/bin/env python3

# This is an example of the dangers of using code you just find from the Internet, in addition to showing how we can
# set up a class to do things for us behind the scenes.  In this case, we're going to make a fake physics package,
# and use it to do some nefarious stuff.

# This is the actual value of c, the speed of light
from scipy.constants import c as original_c


# This is a class that's going to behave like a constant, but will also do other things.
class FakeNumber:
    def __init__(self, n):
        self.n = n

    # When Python needs a float, we can pretend to be a float.
    def __float__(self):
        return self.n

    def __repr__(self):
        return str(self.n)

    def __str__(self):
        return self.__repr__()

    # If we're really trying to fake being a constant, then we'd have to define all of the mathematical operations.
    # Since we're just making a point here, we're only going to define left and right multiply.
    def __mul__(self, other):
        # In addition to doing the calculation correctly, we're also going to run some extra code.  In this case, it's
        # just going to print stuff out, but it could as easily try to find your passwords or social security number,
        # and email it to me.
        print("You're doing physics!  Stop it!")
        return self.n * other

    def __rmul__(self, other):
        return self * other


c = FakeNumber(original_c)


if __name__ == '__main__':
    n = FakeNumber(2)

    print(n * 2)
