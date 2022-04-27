#!/usr/bin/env python3

import numpy as np

## Practice using numpy basics
#
# First thing is to write, by hand, a simple filter that replaces any zeros with the average from either side
#  Making an assumption here that there are not two (or more) zeros in a row, and no zeros at the ends of the arrays
# Note that there are tools in numpy/scipy to do this sort of thing; we're just using this as practice here

# Get some data to play with
file_name = "Data/proxy_test_grasp.csv"
data_from_csv = np.loadtxt(file_name, dtype="float", delimiter=",")

# First step: Calculate a new matrix of data where each column is the average of the column to the left and the
# column to the right
def avg_left_right(data):
    """Average the left column with the right
      Doing this as a function so you can practice on a small array and then do it on the big one
      @param data the input data, as a matrix"""

    # Step 1 -
    avg_data = 0.5 * (data[:, 0:-2] + data[:, 2:])
    return avg_data

# test data
#  Step 1, get this to work with data with one row, 4 columns
#    You will need data slicing. Conceptually, get columns 0, n-2 and add it to columns 2, n
#         hint: data[0:-2] gets items 0 through the 3rd to last
data_test_one_row = np.array([[1, 7, 3, 5]])
print(f"Test one row {avg_left_right(data_test_one_row)}")
# answer should be a 1x2 array with the values 2, 6

#  Step 2, modify your answer to the above to have it do the same calculation for all rows
#    hint: data[:, 0] gets all rows, 0th column
data_test_three_rows = np.array([[1, 7, 3], [2, 8, 6], [3, 9, 9]])
# Answer should be a 3x1 array, with 2, 4, 6 in it
print(f"Test three rows: {avg_left_right(data_test_three_rows)}")

#  Step 3, compute for the full data set
#    Note: this array should have the same number of rows as the original, but 2 fewer columns
filter_csv_data = avg_left_right(data_from_csv)

# Step 4, fill in the zeros with the filtered data
bool_fix_array = data_from_csv == 0
find_zero_data = np.where(bool_fix_array == 0)
for i, j in zip(find_zero_data[0], find_zero_data[1]):
    print(f"Indices of where data is zero {i}, {j}")

data_from_csv[data_from_csv == 0] = filter_csv_data[bool_fix_array[:, 1:-1]]
for i, j in zip(find_zero_data[0], find_zero_data[1]):
    print(f"Indices of where data is zero {i}, {j}")
