#!/usr/bin/env python3

# Make sure numpy is available

# Problem 1: Read data
#  Read in both the data file and the file that describes what's *in* the data file.

data = ...
data_description = ...

# Problem 2: Prints stats for each channel
# Notes for problem 2
#   Do this with a for loop and with the names from the data_description variable - do NOT do this by copying
#   the print statement. Do NOT copy stuff in data.
# Sub tasks: Looping over the elements of the dictionary in data_description, numpy array slicing, using variables
#  to control numpy array slicing, using numpy stats methods.
# Recommended order of implementation:
#   Set up a for loop to loop over the dictionary in data_description, printing out each channel's name
#   Change the print statement to also print out the index of the channel
#   Change the print statement to print out the first value for each channel for the first row
#     Check this against the spreadsheet by making sure the values in the first row match what you printed out
#   Change the print statement to print out ALL of the values for that channel for the first row
#     Check this against the spreadsheet
#   Now print out the minimum, maximum, mean for each channel for the first row using the array slicing you just set up
#   Now make one more change to get ALL rows for each channel
#
# For each data channel, print out the following:
print("Channel name {}, minimum {}, maximum {}, mean {}")

# Problem 3: Find the rows with the smallest and largest peaks in the ?? channel
# Notes for problem 3
#   No for loops - do this with np.where.
#   We should be able to change channel_to_search to a different text string and it still works (prints out at least
#     one minimum index - see extra credit below). No "hard-wiring" the channel name
#   No copying the data
#   There are fancier ways to do this with other numpy functions - you are welcome to try them AFTER you get where
#   working
# Recommended order of implementation:
#  Use your code from above to slice the data for the channel you want and print out the minimum value
#  Store the min value for that channel in a variable
#  Use "where" and print out the results - what do you notice about them?
#  Two options: Use where on sliced data OR search where for the right columns. The latter is harder
channel_to_search = ""
print("Smallest value {}, row {}, column {}")
print("Largest value {}, row {}, column {}")

# Problem 3: Extra credit - deal correctly when there are multiple places with the same min value (use data channel ??)
#
