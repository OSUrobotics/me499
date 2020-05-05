#!/usr/bin/env python3

# You've seen the use of context managers with file I/O.  You can write your own managers for classes.  We're going to
# use a fictional database access example to show how it works.  Typically, to use a database, you first need to open
# a connection to it, just like a file.  When you're done, you have to close the connection, and make sure everything
# you did has been committed to the database, again like a file.  The context manager helps you do this automatically,
# so that you don't need to worry about remembering to do it by hand.


class Database:
    """
    Fictional database access class.
    """

    def __init__(self, name):
        """
        Constructor.
        :param name: The database name.
        """
        self.name = name

    # This function is run when we enter the context manager.  It needs to return self for the with construct to work.
    def __enter__(self):
        """
        Context initialization.
        :return: self
        """

        # You'd make a conntection to the database here, and get it ready for access.
        print('Make the connection to', self.name)
        return self

    # This function is run after the code in the with block is done.  You don't worry about the extra arguments for
    # now, but they do need to be there.
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context closure.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """

        # You'd actually close out the database conntection here, and clean things up.
        print('Close the connection to', self.name)

    # Typically, you'll have a number of functions that do some actual work.
    def stuff(self):
        """
        An example function that does work in a database, assuming that it's opened and ready.
        :return:
        """
        print('Do stuff in the database')


if __name__ == '__main__':
    # Open the database context manager, do some stuff.  The context functions __enter__() and __exit__() are called
    # automatically by Python.
    with Database('My awesome database') as d:
        d.stuff()
