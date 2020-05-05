#!/usr/bin/env python3


class Student:
    """
    A simple class that collects data about students.
    """
    def __init__(self, name, id):
        """
        Constructor for the Student class.
        :param name: Student name.
        :param id: Student ID number.
        """

        # Take the arguments and store them in instance variables for the class.  Notice that these are prefaced
        # by self.
        self.name = name
        self.id = id

        # We're going to start by assuming that students haven't selected a major.
        self.major = None

    def __repr__(self):
        """
        The representation of the Student class.
        :return: A string representation of the class instance.
        """

        # Return a string representation of the class used for printing out.  This is going to be the student's name
        # and ID number.
        return '{0} ({1})'.format(self.name, self.id)

    def __str__(self):
        """
        String representation of the Student class.
        :return:
        """

        # Usually, __str__ and __repr__ return the same thing.
        return self.__repr__()

    def print_summary(self):
        """
        Print out a summary of the student.
        :return:
        """

        # This just prints out a summary of the information in the class
        print('Name:', self.name)
        print('  ID:', self.id)

        # If a major is declared, then this prints it out.  If self.major is None, then it prints out Undeclared
        # instead.  Note the use of or and short-circuit evaluation to do this.
        print('  Major:', self.major or 'Undeclared')


if __name__ == '__main__':
    # We initialize classes like this.
    s = Student('John Doe', 12345)
    t = Student('Jane Doe', 54321)

    # Since we have __str__ defined, we can pass an instance of the class to the print function.
    print(s)

    # We can access the class functions using the dot syntax.
    t.print_summary()

    # We can also access, and set, the instance variables the same way.
    t.major = 'Mechanical Engineering'
    t.print_summary()