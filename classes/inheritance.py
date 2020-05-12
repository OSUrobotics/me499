#!/usr/bin/env python3


from datetime import date


# This example shows class inheritance, and how you might use it to construct classes for faculty and students at OSU.
# In this example, we're going to use it as an abstraction mechanism, to hold information about people.  We're going
# to use inheritance to model the fact that there's a hierarchy of identities (and information) in how we think about
# people.

# This is the base class for our example.  Everyone is a person, and every person has a name.  Everyone also has a
# birthday, but we're going to recognize that we don't know some people's birthdays.
class Person:
    """
    Person base class.
    """
    def __init__(self, name, birthday=None):
        """
        Constructor.
        :param name: The person's name.
        :param birthday: The person's birthday.  Defaults to None.
        """
        self.name = name
        self.birthday = birthday

    # This is the representation of Person.  Not that this is the representation information that developers might be
    # interested in.  For this example, we're going to have these include the class names, and some of the class
    # instance variables.
    def __repr__(self):
        """
        Representation of Person.
        :return:
        """
        return 'Person({0})'.format(self.name)

    # For the string representation, we're just going to print out the person's name.
    def __str__(self):
        """
        String representation.
        :return: The string representation of the class instance.
        """
        return self.name

    def age(self):
        """
        The person's age.
        :return: The person's age, in years, as of the current date.
        """
        # If we don't have a birthday recorded, then return None.
        if not self.birthday:
            return None
        else:
            # If we do have a birthday, then work out the age in years.
            today = date.today()
            return today.year - self.birthday.year - \
                ((today.month, today.day) < (self.birthday.month, self.birthday.day))


# We're going to define an OSU Person.  This class is a person, and inherits from that class, but also has some
# additional information.  In this case, it's an OSU id number.
class OSUPerson(Person):
    """
    OSUPerson example.
    """
    def __init__(self, name, id, birthday=None):
        """
        Constructor.
        :param name: The person's name.
        :param id: The person's ID number.
        :param birthday: The person's OSU ID number.  Defaults to None.
        """
        # The first thing that you should do is call the constructor of the base class.  You get to this by using the
        # super() function.  You could also do Person.__init__(), but using super() discovers the base class
        # dynamically, and is the preferred method.  Here, we're passing the arguments to the base class constructor.
        super(OSUPerson, self).__init__(name, birthday)

        # This is our attribute.
        self.id = id

    def __repr__(self):
        """
        Representation.
        :return: The representation of OSUPerson.
        """
        return 'OSUPerson({0}, {1})'.format(self.name, self.id)

    # The string representation is going to be based on the string representation of the base class.  This sort of
    # hierarchical dependence is really common in inherited classes.
    def __str__(self):
        """
        String representation.
        :return: The string representation of OSUPerson
        """
        return '{0} ({1})'.format(super(OSUPerson, self).__str__(), self.id)


# Students are OSU people.
class Student(OSUPerson):
    """
    Student example.
    """
    def __init__(self, name, id, birthday=None):
        """
        Constructor.
        :param name: Student's name.
        :param id: Student's ID number.
        :param birthday: Student's birthday.  Defaults to None.
        """

        # Call the base class constructor.  This will recursively call the base class of OSUPerson.
        super(Student, self).__init__(name, id, birthday)

        # GPA is specialized to Student.  Make an instance variable that people can manipulate directly.
        self.gpa = None

    def __repr__(self):
        """
        Representation.
        :return: Representation of Student.
        """
        return 'Student({0}, {1})'.format(self.name, self.id)

    # We're not going to define __str__() since we can use the parent class function instead.  Any functions you don't
    # reimplement in the child class use the base class version.  If you define the function, then it overrides the
    # base class version.


# Faculty are also OSU people.
class Faculty(OSUPerson):
    """
    Faculty class example.
    """
    def __init__(self, name, id, department, birthday=None):
        """
        Constructor.
        :param name: Faculty name.
        :param id: Faculty ID number.
        :param department: Faculty department.
        :param birthday: Faculty burthday.
        """
        # Call the base class constructor.
        super(Faculty, self).__init__(name, id, birthday)

        # Set our own information.
        self.department = department

    def __repr__(self):
        """
        Representation
        :return: Representation of Faculty.
        """
        return 'Faculty({0}, {1}, {2})'.format(self.name, self.id, self.department)

    def __str__(self):
        """
        String representation.
        :return: String representation of Faculty.
        """
        return '{0}, {1}'.format(super(Faculty, self).__str__(), self.department)


if __name__ == '__main__':
    # This is just a person.
    a = Person('Jane Doe', date(1969, 8, 10))
    print(a)

    # This is someone from OSU
    b = OSUPerson('John Doe', 123456789)
    print(b)

    # This is a student
    c = Student('Kermit T. Frog', 987654321)
    print(c)

    # This is a faculty member
    d = Faculty('John I.Q. Nerdelbaum Frink', 872231423, 'Advanced Science', date(1960, 2, 12))

    # We can put these four people into a list, and print it out.  Note that this uses __repr__() under the hood, and
    # not __str__()
    people = [a, b, c, d]
    print(people)

    # We can look at everyone's age.  Note that we can treat everyone the same, since age() is defined in the base
    # class.
    print('Ages:')
    for person in people:
        print('  {0}: {1}'.format(person.name, person.age()))

    # Students have a GPA that you can set and access directly.
    c.gpa = 4.0
    print(c, c.gpa)

    # Faculty don't have a gpa.  Well, technically they do, since the got at least one degree at some point, but noone
    # cares what it is now.  Uncomment this line to see it fail.
    # print(d.gpa)
