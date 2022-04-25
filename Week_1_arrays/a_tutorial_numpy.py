#!/usr/bin/env python3


# What is numpy?
#
# Numpy (and scipy) are python libraries for doing numerical and scientific calculations. Pretty much any mathematical
#   or signal processing operation you would find in a text book is implemented in one of those libraries. Much of the
#   functionality of MatLab is here, along with plotting (see matplotlib and the tutorial on matplotlib)
#
# The heart of numpy is the numpy array data structure. These are n-dimensional arrays, all of the same data type with
#   every element in a dimension the same size (unlike python lists, which can mix and match data types and array
#   dimension sizes),
#
# Because numpy arrays are all of the same type/size, it's possible to do the same operation to all of the elements
#   of an array really, really fast. This is the heart of using numpy; instead of explicitly writing for loops,
#   numpy "overrides" operations (like *, +, <, > ==) so that they happen to the entire array (all n dimensions of it)
#   all at once, in one line of code. There's still for loops in there, it's just Python is doing it for you. If you
#   find yourself writing a for loop with a numpy array, btw, chances are you shouldn't be. Not that it's wrong, it's
#   just really, really slow.
#
# Finally, there are all of the operations (min, max, sum, filter, etc) in numpy/scipy that use numpy arrays as input.
#  These are very powerful, but it can be challenging to set up data and function parameters correctly to get them
#  to work the way you want. We'll cover basics here, and more in-depth later.

# This is the way I like to import numpy. All numpy operations will start with np. I just find it easier (when reading
#   the code) to have this visual cue that this function/operation came from numpy. It also prevents name conflicts -
#   for example, if you accidentally name a variable "min" you won't "overwrite" numpy's min. Also, if you cut and
#   paste your code somewhere else, it's easier to get it working without name conflicts.
import numpy as np

# If you use this import, then you don't need the np. in front. Saves typing, but it means that ALL of the names/
#   functions etc in numpy are now in your list of variables.
# import numpy

# If you want to do a mix of the above, but just bring in the variables/data structures that you need, you can
#   use one of the following. If you're using a lot of numpy operations/variables than it can get annoying to have to
#   include all of them, though
# from numpy import array as nparray
# from numpy import array

############ Making a numpy array #############
#
# There are three main approaches to/reasons for making a numpy array
#  1) You have data in a file - spreadsheet, csv, image, etc
#  2) You need a "blank" array of data that you fill in with some default value
#  3) You're combining data from existing numpy arrays
#
# We will go over each in turn

## From a file
# There are two cases here
#   1) a single file with all the data (and no extra stuff like headers), eg, a csv file of numbers, an image
#   2) a spreadsheet with headers and other data that you don't necessarily need
#
#  For 1) there's almost always a numpy function that will do the data reading and return a numpy array. For 2),
#   the best approach is to read the data into a python list and then create the numpy array from the list. This avoids
#   the problem of needing to know the data sizes in advance.
#    If you know the data size in advance then you can use the "blank" approach above to create the numpy array and
#    read data into it.
#  Whatever you do, avoid creating and destroying numpy arrays over and over again (think list append); list data
#    structures are setup to handle this a lot better than numpy arrays.

# Example 1: Reading in a csv file of numbers directly into a numpy array
file_name = "Data/proxy_test_grasp.csv"
# This is a first example of the fun of numpy/scipy function parameters. Google numpy loadtxt to get a list of
#   all possible parameters - all of which have default values, except the file name.
#   Here, we override specific parameters (what type of data it is and what the delimiter is)
data_from_csv = np.loadtxt(file_name, dtype="float", delimiter=",")

print("Example 1: Data from a csv file")
print(f"Data dimensions: {data_from_csv.shape}, total number of elements: {data_from_csv.size}")

# Example 2: Converting a list to a numpy array (note, we'll cover advanced file reading later)
my_list = [[0,1], [2.0, 4.0], [5.0, 10.0]]
data_from_list = np.array(my_list)

print("Example 2: Create a list then convert a list to a numpy array")
print("Original list, notice flat format")
print(my_list)
print("List as numpy array, notice matrix format")
print(data_from_list)
print(f"Data dimensions: {data_from_list.shape}, total number of elements: {data_from_list.size}")

# Example 3: Creating a "blank" array, either of zeros, ones, or random numbers
#  dtype is optional - you can set it to int for integers, bool for booleans, etc
#  A 3 X 5 X 2  array of zeros
print("Example 3: Zeros, ones, and random - making numpy arrays from scratch")
data_zeros = np.zeros([3, 5, 2], dtype=float)
print(f"Number of dimensions: {data_zeros.ndim}, dimension sizes: {data_zeros.shape}, total number of elements: {data_zeros.size}")

# Making an array of ones of the same size as data_from_list
#  .shape contains the dimensions of the array - number of rows, columns, etc
#  It is a tuple, so you can't change it
data_ones = np.ones(data_from_csv.shape)
print(f"Data dimensions: {data_ones.shape}, total number of elements: {data_ones.size}")

# Making an array of random numbers
#  Don't be confused by the parameter being called size - it can take a tuple of dimensions
data_random = np.random.uniform(low=-1, high=1, size=(3, 10))
print(f"Random uniform data, size {data_random.shape}")
print(data_random)

## Operations with numpy arrays
# There are two concepts here, one easy, one hard
#  Concept 1: operators (+, -, <, etc) are all automatically done on all elements (for loops)
#     All arrays in the equation have to have the same dimensions
#  Concept 2: If statements are accomplished using boolean indexing [if statement]
#     Using [] selects a part of the array - so the dimensions may be different
#  Operations usually create new arrays.

# Simplest example - apply 2 * x + 1 to all elements of the array, and store in a new array
data_new_csv = 2 * data_from_csv + 1
#  min/max are numpy operations that do the min/max across ALL of the dimension - see below for how to do min/max
#    across just one dimension
print(f"Original minimum: {np.min(data_from_csv)} and maximum: {np.max(data_from_csv)}")
print(f"New minimum: {np.min(data_new_csv)} and maximum: {np.max(data_new_csv)}")

# A more complicated example - shift and scale the entire data set so that the min is zero, the max is one
min_all_data = np.min(data_from_csv)
max_all_data = np.max(data_from_csv)
shift_amount = min_all_data
scale_amount = 1.0 / (max_all_data - min_all_data)
data_new_csv = scale_amount * (data_from_csv - shift_amount)
print(f"Shifted minimum: {np.min(data_new_csv)} and maximum: {np.max(data_new_csv)}")

# Now for the if statement. There are a handful of places in the data where there are zeros. These are places where
#  there wasn't any valid data, so they shouldn't be included when doing a mean calculations.
mean_including_zeros = np.mean(data_from_csv)
mean_not_including_zeros = np.mean(data_from_csv[data_from_csv != 0])
print(f"Means with {mean_including_zeros} and without {mean_not_including_zeros} zeros")
