#!/usr/bin/env python3

import numpy as np

# --------------------
# Lecture goals
#  1) Understand the benefit of numpy (over lists) for operating over lists of numbers
#  2) Introduction to numpy-style array operations
#  3) Dictionaries for data encapsulation
#  4) Functions for functionality encapsulation

# Functions: Functions enable encapsulation of, well, functionality.
# They're also a useful mental tool for organizing and structuring your thoughts on how to solve a given problem
#  1) Clearly define a bit of code that takes in some inputs, does some computation, then outputs some data
#  2) Makes it easier to test that code with different inputs
#  3) Practicalities: Prevents one of the most common sources of errors - re-using variable names
#
# It's almost never wrong to encapsulate a bit of code in a function. It can slow down (a tiny bit) computation
#  time, but can greatly reduce debugging time, so it's usually worth it.
# Python's function syntax is beautifully designed to make it easy to set default values for parameters and pass
#  back as much data as you want. We'll see more of that later; for this assignment we'll use the power of dictionaries
#  to pass back "labeled" data.

#
def calc_stats_from_list(in_list):
    """ Calculate mean of positive numbers, mean of negatives numbers
    Separate the list into positive and negative numbers. Calculate the mean of each. Return those means, along with
     how many positive/negative numbers there were
    @param in_list : any list type
    @return - A dictionary with the desired stats"""

    # These are the stats we're calculating. This is more elegant/useful than creating four variables - it keeps all
    #  of the values in the same place and assigns a meaningful label (key) to them
    dict_ret_stats = {"Mean positive": 0, "Mean negative": 0, "Count positive": 0, "Count negative": 0}

    # BEGIN SOLUTION
    # Note that I would normally do this with 4 variables, and then create the dictionary at the end and return it,
    #   (which would save a lot of dictionary accesses) but doing this way because it makes setting up the automatic
    #   grading software easier
    for n in in_list:
        if n < 0:
            dict_ret_stats["Mean negative"] += n
            dict_ret_stats["Count negative"] += 1
        else:
            dict_ret_stats["Mean positive"] += n
            dict_ret_stats["Count positive"] += 1

    if dict_ret_stats["Count negative"] > 0:
        dict_ret_stats["Mean negative"] /= dict_ret_stats["Count negative"]
    dict_ret_stats["Mean negative"]
    # END SOLUTION
    return dict_ret_stats
