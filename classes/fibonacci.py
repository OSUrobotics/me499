#!/usr/bin/env python3


# This is a module that allows us to run things just before a piece of code ends.
import atexit

# This module allows us to save data structures efficiently
import pickle

# This is a class the hides implementation.  In this case, it revisits the Fibonacci cacheing example we looked at
# earlier.  In this case, we're going to define a class that contains the cache, and acts like a function.  Note that
# this implementation is not thread-safe.

class Fibonacci:
    """
    A class that wraps up a cacheing Fibonacci number function.
    """

    # These are class variables.  There is only one copy of these, shared by all instances of the class.  This is a
    # good place to define things that are shared, like filenames and, in this case, the Fibonacci number cache.
    CACHE_PICKLE_FILE = 'fibfile.pickle'
    cache = None

    def __init__(self):
        """
        Constructor.
        """

        # If we don't already have a cache, try to load one.  Since this is shared by all instances, another instance
        # might have already created the cache, so it's best to check.
        if not Fibonacci.cache:
            try:
                # Try to open the pickle file and read it in to the cache.
                with open(Fibonacci.CACHE_PICKLE_FILE, 'rb') as f:
                    Fibonacci.cache = pickle.load(f)
            except FileNotFoundError:
                # If we can't open the saved cache file, then initialize the cache with the base values for the
                # Fibonacci function recursion.
                Fibonacci.cache = {0:0, 1: 1}

    def __call__(self, n):
        """
        Fibonacci function calculation.
        :param n: The Fibonacci number to calculate.
        :return: The Fibonacci number.
        """

        # This is just like the recursive cacheing version of the function from earlier in the term.
        try:
            # Try to find the number in the cache, and return it.
            return Fibonacci.cache[n]
        except KeyError:
            # If we can't find it in the cache, explicitly calculate it, store it in the cache, and then return it.
            value = self.__call__(n - 1) + self.__call__(n - 2)
            Fibonacci.cache[n] = value
            return value

    # The thing with the @ sign is a function decorator.  We'll get to this later in the term, but this one basically
    # tells Python that the function belongs to the class, not an instance of the class.  Notice that there's no
    # self variable in the argument list.  This means that it can't access the instance variables of any given
    # class instance, but it can get to the class variables.  We could write this as just a function, outside of the
    # class, but it logically belongs to the class, so we put it in as a static function.  Since we don't want people
    # to actually call this function, the name starts with a _.  This doesn't stop people from calling it, but it
    # acts as a sign that they shouldn't.
    @staticmethod
    def _save_cache():
        """
        Pickle the Fibonacci cache to a file.
        :return: None
        """

        # Open the pickle file and write out the cache.
        with open(Fibonacci.CACHE_PICKLE_FILE, 'wb') as f:
            pickle.dump(Fibonacci.cache, f)


# Make a single instance of the class that users will interact with.
fib = Fibonacci()

# This tells Python that, just before the program ends, it should call Fibonacci._save_cache().  This will write out
# the Fibonacci cache right at the end of the execution of your code.
atexit.register(Fibonacci._save_cache)

if __name__ == '__main__':
    # We can not use fib (the single instance of the class) just like is was a function.  All of the cacheing happens
    # behind the scenes.  To see this at work, delete the pickle file and then run the code.  Then run the code again,
    # and see how it's faster the second time, because the Fibonacci values are saved between runs.  Since we're
    # cacheing, the difference is small, but it's there.
    from time import time
    start_time = time()
    f = fib(35)
    stop_time = time()
    print('{0}: {1} seconds'.format(f, stop_time - start_time))

    # Because we've defined __call__(), we can use fib just like it was a function
    v = fib(20)
    print([fib(i) for i in range(10)])
