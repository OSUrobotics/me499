#!/usr/bin/env python3


# We're going to use wall clock time
from time import time


class Timer:
    """
    Example timing class, using a context manager.
    """
    def __init__(self, name):
        """
        Constructor.
        :param name: A name to identify the timer
        """
        self.name = name

    def __enter__(self):
        """
        Context initialization.
        :return: self
        """

        # The timer starts when the context opens.
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context closure.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """

        # Record the end time.  This doesn't need to be an instance variable, since we're not going to keep it around.
        end_time = time()

        # Print out a statement to show how long the context block took to execute.
        print('{0}: {1} seconds'.format(self.name, end_time - self.start_time))


if __name__ == '__main__':
    # We're going to verify that sleep works as it should
    from time import sleep

    # Open the context manager.  We don't need the as clause, since we're not going to use it in this case.
    with Timer('sleep timer'):
        sleep(1)
