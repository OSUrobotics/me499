#!/usr/bin/env python3
# ...this first line defines what version of Python you expect people to use

# Note that the editor may complain because these are single files we're importing,
# not modules.

# import kitchen_sink_class
#  And set the class name to KS
#  This executes the entire file, and then just makes a shortcut for you of KS
from kitchen_sink_class import KitchenSink as KS

# this imports everything - including those variables like do_not_do_this
#   .. but everything has to be accessed by kitchen_sink_class
import kitchen_sink_class


# Now define functions
# Notice there is no "self" here -  everything is passed in
def my_kitchen_sink_fc(p1, p2, p3=3.0, p4="default"):
    """This should (in a few words) define what the function is for.
    @param: p1 - define what p1 is, and what type/range/values is expected
    @param: p2 - same again
    @param: p3 - and again
    @param: p4 - and again - but this one will default to the string "default" if you don't pass anything
    @returns: What does this function return? Both type and what it is conceptually"""
    # Notice the :0.2f - this says format this as a number with 2 decimal places
    return "name {0} value {1:0.2f}".format(p4, p3 * (p1 + p2))


# You can return tuples, arrays, classes - almost anything. Comment out the different lines to see what they do
def ret_value_types():
    """
    Try one of these
    return ks(3): # Make a class instance and return it
    return (0, "foo", [3, 1, 5]) # A tuple with a number, string, and an array in it
    return [1.0, 0.2, 3.0] # An array
    """
    return 3.0  # a number


# You can call functions from functions
def meta_function(p1):
    return my_kitchen_sink_fc(p1, 0.3, 0.4)


# Different ways to instantiate variables and cast them
def make_variables():
    a_number = 3  # defaults to an integer
    a_float = 3.0  # the .0 says make this a float
    a_string = "3"  # the string 3, not a number
    a_boolean = True  # or False
    an_empty_array = []
    an_array = [3, 3.0, "str", 10]  # Notice that things in the array don't have to be the same type...
    an_array_of_arrays = [[1, 2], ["1", "2"], an_array]  # and you can put arrays inside of arrays
    an_array_from_for = [a * 2 for a in range(1, 5, 2)]  # An array created with a for loop - range returns an array [1, 3, 5]

    # A tuple is a lot like an array - except you can't change the elements after it's created (immutable)
    #  Use to signal to Python (and whomever's reading the code) that you don't expect/what this collection to change
    a_tuple = (1, "hello", [2, 1])

    # Sets - lists of objects that have no particular order
    a_set = {"a", "b", "c"}

    # Dictionaries - lists of objects that have the given keys k:value
    an_empty_dict = {}
    a_dict = {0: "a", 1: "b", 2: "c"}

    # you can also make functions and give them names, although in general you should do this in-place
    y_fc = lambda x: my_kitchen_sink_fc(x, 3, 4, "foo")

    val = y_fc(2)  # will call my_kitchen_sink_fc with 2, 3, 4, "foo"
    val_same = y_fc(lambda x: my_kitchen_sink_fc(x, 3, 4, "foo"))

    # A serious abuse of the tuple return functionality
    ret_val = (a_number, a_float, a_string, a_boolean, an_empty_array, an_array, an_array_of_arrays, an_array_from_for,
               a_tuple, a_set, an_empty_dict, a_dict, y_fc, val, val_same)
    return ret_val

# Getting and setting values in arrays
# Remember, arrays are indexed from 0
# Search term: "slicing"
def all_things_arrays():
    # empty array
    a = []
    # Loop over all integers in 0 to 100
    for i in range(0, 100):
        # if an even number (i mod 2 is zero)
        if i % 2 == 0:
            # add to the array
            a.append(i)
    # You can change array values
    a[0] = [10, 5]  # replace the first element of a with the array [10,5]

    # You can get parts of arrays (look up "slicing" arrays in Python)
    # Notice these are grayed out because you're not using them anywhere
    a_all_but_first = a[1:]
    a_all_but_end = a[0:-1]
    a_ever_other = a[0::2]
    a_reverse = a[::-1]
    a_first_two_elements = a[0:2]  # gets 0 and 1, but NOT 2

    # Number of elements in the array
    a_len = len(a)

    # Loop over an array, getting both an index (0,length of array) and value
    for i, v in enumerate(a):
        print("Index {0}, value {1}".format(i, v))

    # If you're just doing something simple to the array, you can use this syntax to do that operation
    # on the array and create a new array to put the result in, all in one fell swoop
    a_scale_by_two = [v * 2 for v in a]

    # Array caveats
    b = a          # b is not a "deep" copy of a - if you chanbe b, it will change a and vice-versa
    b = a.copy()   # this will make a complete copy of a. Generally, you won't need to do this...

    # Usually, if you're mucking with an array and you want to make a "copy" and do something with it, you'll either
    # use the b =  [v for v in a] syntax above, or something like:
    b = []  # empty array
    for v in a:
        # Whatever you want to do to array element - then append to b
        b.append(v * 3)


# Difference between arrays and tuples
def diff_tuple_array():
    an_array = [1, 2, 3]
    an_empty_array = []
    a_tuple = (1, 2, 3)

    # both of these work
    for v in an_array:
        print(v)
    for v in a_tuple:
        print(v)
    # and these
    l_a = len(an_array)
    l_t = len(a_tuple)

    # You can do this
    an_array[0] = 2

    # but not this - notice it's highlighted in yellow, which means PyCharm thinks you did something Bad
    #     put cursor over and read error (or put cursor over yellow bar on right)
    try:
        a_tuple[0] = 2
    except TypeError:
        print("Generates type error because you can't do that kind of assignment")
        print("error generated:  TypeError: 'tuple' object does not support item assignment")

    # This lets you return multiple objects from a function -
    #   foo = diff_tuple_array will assign foo the first element of the tuple
    #   f1, f2, f3 = diff_tuple_array will assign each of the tuple elements to the invididual arrays
    #   _, f2, _ = diff_tuple_array will "ditch" f1 and f3, and keep f2
    return a_tuple


# Getting and setting values in dictionaries
def all_things_dict():
    # Syntax is { key:value, key:value }
    a_dict = {"foo":3}
    an_empty_dict = {}

    # To get an element out - if the key isn't in the dictionary, you'll get a key error
    val_for_key_foo = a_dict["foo"]

    # This will generate a KeyError - because this item doesn't exist
    try:
        make_key_error = a_dict["bar"]
    except KeyError:
        print("error generated:  KeyError: 'bar'")

    # A common bit of code that uses try/except to either add or edit items in the dictionary
    keys_to_add_or_edit = ["foo", "bar", "hello"]
    vals_to_add_or_edit = [0.5, 0.1, 0.5]

    # Version one - just put the things into the array
    # Zip lets us put the two arrays together
    for k, v in zip(keys_to_add_or_edit, vals_to_add_or_edit):
        # just set the key to the given value
        # syntax is dict[key] = value
        # if the entry  doesn't exist, it will create it.
        a_dict[k] = v

    # Version two - you want to edit the value in the dictionary by adding value, and if the entry
    #  doesn't exist, set it to value. Useful for counting the number of times something ocurred
    a_count_dict = {"foo": 1}
    for k, v in zip(keys_to_add_or_edit, vals_to_add_or_edit):
        try:
            # just try incrementing the value by one
            # Will generate a key error if it doesn't exist
            # syntax is dict[key] = value
            a_count_dict[k] = a_count_dict[k] + v
        except KeyError: # be specific about which error type
            a_count_dict[k] = v

    # Some ways to iterate over the dictionary - note that the order is random (well, not completely) but DO NOT
    # assume that if you put the keys in with a specific order that they will come *out* the same way
    for k, v in a_dict.items():
        print("key {0}, value {1}".format(k, v))

    # Iterate over the keys
    for k in a_dict.keys():
        print("key {0}, value {1}".format(k, a_dict[k]))

    # Iterate over the values
    for v in a_dict.values():
        print("value {0}".format(v))

    # Iterate over the *sorted* keys. Assumes the keys can be sorted...
    #  sorted returns a sorted list
    for k in sorted(a_dict.keys()):
        v = a_dict[k]
        print("key {0}, value {1}".format(k, v))

    # Ask how many items in the dictionary
    len_array = len(a_dict)
    return len_array


def casting_between_values():
    a_float = 3.0
    an_int = 3

    # Can go this way
    a_float_cast = float(an_int)
    # ... but not this way
    try:
        an_int_cast = int(a_float)
    except ValueError:
        print("ValueError: invalid literal for int() with base 10: '2.3'")

    # will truncate to 3
    an_int_truncate = int(3.7)

    # Will turn this into "2.3"
    a_str_of_a_number = str(2.3)

    # This works, and returns 2
    a_number_of_a_str = int("2")

    # This doesn't
    try:
        a_number_of_a_str = int("2.3")
    except ValueError:
        print("error generated: ValueError: invalid literal for int() with base 10: '2.3'")

    # nor this - but only because 1e20 is too big for an int
    try:
        a_big_int = int("1e29")
    except ValueError:
        print("error generated: ValueError: invalid literal for int() with base 10: '1e20'")

    # but this does
    a_float_of_a_str = float("2.3")

    # These work
    an_int = int("3512")
    a_float = float("188.3")
    a_big_float = float("1e10")

    # This doesn't work
    try:
        a_number = int("one")
    except ValueError:
        print("generates error: ValueError: invalid literal for int() with base 10: 'one'")

    # Converting an array "in place"
    float_array = [3.5, 1.2, 5.0]
    a_array_int = [int(f) for f in float_array]
    return a_array_int


def math_operations():
    # This should look familiar - if an int and a float, calls __add(int, float)
    # ** is exponentiation
    # See numpy or math library for things like pi, cos, sqrt, etc
    add_numbers = ((3 + (5 * 3) - 7) / 2) ** 2

    # modulus/remainder - muxt be integers
    remainder = 6 % 2

    # Python 3 does the right thing and converts these both to floats so you get 0.6, not 0
    # Python 2 does NOT do the right thing
    a_float = 3 / 5

    # This probably shouldn't work, but it does
    foo = 6.3 % 2

    return remainder


def expressions_and_if_and_while():
    a = 3
    b = 7
    while a < b:
        a = a + 1

    if a < 5 < b:
        print("between")
    elif b < 5 < a:
        print("Between backwards")
    else:
        print("Neither true")

    if a < 3 and (b < 5 or b > 2) and not b == 3:
        print("compound if expression")

    # Make a boolean
    b_ret_bool = a < b
    if b_ret_bool is True:
        print("Notice the use of is, not equal")


def my_func(a):
    return 3 * a


def functions_to_functions(f, b):
    return f(b)


# Test code for this class goes here. This says "if you're running this python
# script by itself - not importing it - then run this code"
if __name__ == '__main__':
    print("Start of Main - the stuff before came from importing kitchen_sink_class")

    # This makes a kitchen sink - using the naming from the from x import y as z
    my_ks = KS(1)

    # Some useful commands
    print(type(my_ks))
    print(type(3))
    help(my_ks)
    all_commands_on_object = dir(my_ks)

    # This makes a kitchen sing - using the scoping from the import kitchen_sink_class
    my_ks2 = kitchen_sink_class.KitchenSink(2)

    # Note that the do_not_do_this variable exists because of the import - whether you want it to or not
    print("This should not exist, but does, because of the do not do variable: {0}".format(kitchen_sink_class.do_not_do_this))

    # Normally you'd put all your testing code for each of the given functions here
    # Here we'll just call each of these in turn (the ones that won't die when run)
    ret_value = ret_value_types()
    print("Return value {0}".format(ret_value))

    # Function calling a function with a lambda function
    ret_value = meta_function(3)
    print("Return value meta fc: {0}".format(ret_value))

    # All sorts of ways to make variables
    ret_value = make_variables()
    print("Return value make_variables: {0}".format(ret_value))

    # Array operations
    all_things_arrays()

    # Note that this will throw an exception (but will be caught)...
    diff_tuple_array()

    # Dictionary operations
    all_things_dict()

    # casting between types
    casting_between_values()

    # Basic math operations
    math_operations()

    # Basic expresions
    expressions_and_if_and_while()

    # passing a function to a function
    functions_to_functions(my_func, 3)
