#!/usr/bin/env python3


# JSON is a data format that is popular for web-delivered data, and the json module lets you unpack it easily
# See json-data.py for an example of opening up a json file from the web (instead of just a file)
import json


if __name__ == '__main__':
    # this file has a mapping from colors to rgb values. This file can be found on the web, but
    # we've copied it here to show *just* the json read
    data_file = "data/colors.json"

    # Open the file. Putting this in a with block means it gets tidied up automatically when you're done with it.
    with open(data_file, 'r') as fid:
        # Get the data from the file.  read() grabs the page and decode() take any strange characters and
        # reformats them so that Python will deal better with them.  loads() takes the result of this, and
        # parses out the data into a set of nested dictionaries.
        json_data = json.load(fid)

        # The dicionaries are defined by the {} in the json file. Here, we'll iterate over the
        # elements in the top level dictionary. In this case there's only one key, value
        # pair, key "colors" and value all the stuff in the [] in the file
        #
        print('Top level dictionary, items in dictionary: {0}'.format(len(json_data)))
        for k, v in json_data.items():
            print("Dictionary key: {0} has value: {1}, type {2}".format(k, v, type(v)))

        # Knowing that the value in the first dictionary is my list of colors, I can
        # get the list itself out using the key "colors"
        my_colors = json_data["colors"]
        print("List of colors has {0} colors in it".format(len(my_colors)))

        # Print out all of the elements in the first color. Looking at the text file (or the print out
        # of the first dictionary value) I can see that each color is a dictionary.
        print("First element of the list is:")
        for k, v in my_colors[0].items():
            print("Dictionary key: {0} has value: {1}, type {2}".format(k, v, type(v)))

        # Looking at what gets printed out, I see that the dictionary has a key that is the code,
        # which in turn is a dictionary with an rgba key which has the rgb value... I can
        # now write out a bit of code that prints out the color name and the corresponding rgba value
        # for each color
        print("RGBA values for each color in the list")
        for col in my_colors:
            print("Color name: {0}, RGBA value: {1}".format(col['color'], col['code']['rgba']))



