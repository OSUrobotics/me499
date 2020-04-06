#!/usr/bin/env python3
# ...this first line defines what version of Python you expect people to use

# An example of importing just a single item from the numpy package
# import numpy as np would import the entire package, which would then be
#   accessed by np.pi
from math import pi


class KitchenSink(int):
    # There is only *one* of this variable across all instances of kitchen_sink.
    # Changing this value will change it everywhere
    # In general, discouraged unless you have a really, really good reason (like a cache)
    my_local_float = 0.3

    def __init__(self, my_value_initialize=0):
        """ Initializer
        Gets called when an instance is created
        @param: my_value_initialize: what do you want to initialize self to"""

        # this initializes the class we're inheriting from (in this case, int)
        super(int, self).__init__()

        # Any variables that you expect a kitchen sink should be created (and initizlied)
        # in this method
        # Notice the use of self to indicate a class variable
        self.my_name = "default_name"
        self.save_my_value = my_value_initialize

    # Notice the two underscores - this indicates it's a member *all* classes should have (built-in)
    # This is the *representation* of the object - used when you're printing a container that contains
    #   the object
    def __repr__(self):
        """ How to turn my self into a string
        @return: string """
        # make a string out of my data
        return "My name is {0}, my value {1}".format(self.my_name, self.my_local_float)

    # Most of the time this will just call __repr__ - but if you wanted
    def __str__(self):
        """Cast me to a string
        @return: string """
        # Notice the use of self to get the class method
        return self.__repr__()

    # Something to try - try typing def _ and see what the list of options are. All of these are methods that
    # every class has - you can override their default behavior. You'll do this in the Complex lab assignment
    def __del__(self):
        """Generally don't override defaults - but... useful to show you that you can"""
        return False

    def _mine_and_mine_only(self):
        """The underscore indicates that this really shouldn't be called by any outside code - it's just
          an internal helper function"""
        self.my_name = self.my_name + "internal_only"
        return self.my_name

    def my_method(self, in_val):
        """ A method - add self to in_val and then return
        @param in_val - an array or a float/int type object"""

        # this code gracefully handles an int/float type (anything that can be
        # added to my_local_float) OR an array of such things
        try:
            return in_val + self.my_local_float  # this will generate a TypeEror if in_val is not something that can be added to a number
        except TypeError:
            # This is essentially a for loop with one line in it (add my_local_float to each value in the array)
            #   that returns another array
            # In matlab, you would just do new_array = old_array + my_local_float. Python 3 has wrapped up this
            #   functionality in the [] notation, which says create an array, and do so using the for loop
            return [self.my_local_float + v for v in in_val]

    def my_method_params(self, p1, p2=0.3, p3="hi"):
        """ An example of setting - and overriding - parameters. You have to give at least one parameter (p1)
        @param p1: You have to give this one
        @param p2: If you don't give this one, it will be set to 0.3
        @param p3: If you don't give this one, it will be set to the string hi. If you pass two parameters, this third
           one is the one that will be automatically set"""
        print("Passed: {0} {1} {2}".format(p1, p2, p3))

        return self.__repr__()


# An example of what NOT to do - this will create these two variables in *any* script that includes this one.
#   And print out this annoying message every time you import this file
# Put your test code in the __name__ method below
do_not_do_this = "An unintented global variable"
k1_test = KitchenSink(3)
# Note that we print the same variable twice by numbering
print("Do not do this {0} {1} {0}".format(do_not_do_this, k1_test))


# Test code for this class goes here. This says "if you're running this python
# script by itself - not importing it - then run this code"
# run this in the debugger (cntrl-right click, debug)
# The console is a tab next to the Debugger tab in the window below this one
if __name__ == '__main__':
    print("\nStart of test\n")
    # Make two of these, and set their names
    k1 = KitchenSink(4)
    k1.my_name = "k1"
    k2 = KitchenSink(5)
    k2.my_name = "k2"

    # these are essentially ints, so this works, and returns an int
    k3 = k1 + k2

    # put them all in a tuple (well, triple)
    # sort of like an array, but the expectaion is that you aren't going to change
    # my_ks_tuple
    my_ks_tuple = (k1, k2, k3)
    for k in my_ks_tuple:
        # uses __repr__ to print - note that k3 is an int, and this all still works
        print(k)

    # Effect of local variable in class
    print("k1 has {0} value".format(k1.my_local_float))
    print("Setting k2's")
    # Note the use of the class name, not an instance name...
    KitchenSink.my_local_float = pi
    print("k1 (and all others) now have {0}".format(k1.my_local_float))
    # THIS will create a local variable in k2 that shadows the class one
    k2.my_local_float = 4
    print("k1 still has {0}, k2 has local variable {1}, and class has {2}".format(k1.my_local_float,
                                                                                  k2.my_local_float,
                                                                                  KitchenSink.my_local_float))

    # But
    # Let's try fancy add of an array - use the debugger to see what happens
    val = 3
    val_ret = k1.my_method(val)

    array_val = [3, 1, 7]
    array_ret = k1.my_method(array_val)

    # Playing with parameters. This will set all 3 directly, in the given order
    p1_pass = "p1"
    p2_pass = "p2"
    p3_pass = "p3"
    # Note that you get a *warning* that the type for p2_pass doesn't match the type in the method, but it will still
    #   let you do it. You should pay close attention to these yellow high lights (and corresponding yellow bars on the
    #   right in the scroll bar) because it usually means you did something wrong.
    #  Put your cursor over the variable/in the yellow region/over the yellow bar on the right to see what the error is
    k1.my_method_params(p1_pass, p2_pass, p3_pass)

    # Python is not smart enough to tell you that you  put the parameters in the wrong order
    k1.my_method_params(p2_pass, 0.3, p3_pass)

    # You can leave out the second 2 parameters and they'll be set to the default values
    k1.my_method_params(p1_pass)

    # Or supply 2, and only the last one will be filled with the default
    k1.my_method_params(p1_pass, 0.3)

    # Or you can set them by name
    k1.my_method_params(p1=p1_pass, p2=0.3, p3=p3_pass)

    # In this case, you don't actually have to fill them in in order, but it's still a good idea...
    k1.my_method_params(p2=0.3, p1=p1_pass, p3=p3_pass)

    # You can use this to "skip over" the default parameters, and only set the one or two that you want to override
    # to new values. Very handy for methods in numpy/scipy, where there's typically 10-15 additional parameters
    # you can (optionally) set, but usually you want the defaults
    k1.my_method_params(p1_pass, p3 = p3_pass)

    # Notice the yellow-colored parenthesis. This mn indication that you forgot a required parameter (p1 unfilled)
    k1.my_method_params()

    # And here you see that you added an extra parameter, and it's giving you a warning for that
    # Note: This will cause a run-time error
    k1.my_method_params(p1_pass, p2_pass, p3_pass, 0.3)
