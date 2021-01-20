#!/usr/bin/env python3


if __name__ == '__main__':
    # Text in Python is represented as things called strings.  You can use single or double quotes to assign a string.
    #
    a = 'This is a string.'
    b = "This is also a string."
    c = "So's this, and it has an appostrophe."
    d = str()  # makes an empty string
    print(a, b, c, d)

    # You can use strings with for loops, and get a character at a time.
    for c in 'I am a string':
        print(c)

    # Strings are immutable - you can't change elements or the string
    # If you uncomment this line, you'll get an error
    # a[0] = 't'

    # If you want to change a string, you need to break it apart
    # and put it back together. There are multiple ways to do this
    str_to_change = "foo_a_bar"

    # Separate the string into sub strings by splitting on a
    #  specific character - makes a list of sub strings WITHOUT the
    #  split character
    sub_strs = str_to_change.split('_')
    # + glues the strings together
    new_str = sub_strs[0] + "_A_" + sub_strs[2]

    # You can also grab the first set of characters, add in the
    #  _A_, then grab the last set of characters
    #   Notice the 5: which says the 5th character to the end
    #     remember that 0:4 will get characters 0 through 3
    new_str_v2 = str_to_change[0:4] + "A" + str_to_change[5:]

    #  This assumes you've counted to find the parts of the string
    #  you want to remove - you can also use find() to find a
    #  specific character
    #     Notice the +1 on the second string to "skip" the a
    index_a = str_to_change.find('a')
    new_str_v3 = str_to_change[0:index_a] + "A" + str_to_change[index_a+1:]

    print(str_to_change)
    print(new_str)
    print(new_str_v2)
    print(new_str_v3)

    # There are a number of things you can do to manipulate strings.  Here are some of them.
    print('This is a string'.split())  # Split into a list.  You can choose what you split on as a parameter to split()
    print('This is a string'.replace('string', 'line of text'))  # You can replace things in the string.
    print('string' in 'This is a string')  # Checking if something is in there.

    # If you want to edit a string, you can convert back and
    #  forth from a list
    #   These are not strings - they're lists of characters
    list_of_chars_manual = [c for c in str_to_change]
    # Uses casting to do the same thing
    list_of_chars_cast = list(str_to_change)

    # To go from a list of characters to a string...
    # This doesn't do quite what you want
    convert_list_to_str_oops = str(list_of_chars_manual)
    # Instead use join
    convert_list_to_str = "".join(list_of_chars_manual)

    print(convert_list_to_str_oops)
    print(convert_list_to_str)
