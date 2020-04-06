#!/usr/bin/env python3


if __name__ == '__main__':
    # Text in Python is represented as things called strings.  You can use single or double quotes to assign a string.
    #
    a = 'This is a string.'
    b = "This is also a string."
    c = "So's this, and it has an appostrophe."
    d = str()
    print(a, b, c)

    # You can use strings with for loops, and get a character at a time.
    for c in 'I am a string':
        print(c)

    # There are a number of things you can do to manipulate strings.  Here are some of them.
    print('This is a string'.split())  # Split into a list.  You can choose what you split on as a parameter to split()
    print('This is a string'.replace('string', 'line of text'))  # You can replace things in the string.
    print('string' in 'This is a string')  # Checking if something is in there.