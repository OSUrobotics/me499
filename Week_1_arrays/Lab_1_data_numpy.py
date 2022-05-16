#!/usr/bin/env python3

# Anything numpy-ish will start with np.
import numpy as np

# Overall objectives, weeks 1 & 2
#   Simple statistical analysis of data
#
# Motivation: Whether you're in engineering or business or health care - almost any field nowadays - you need to be
#  able to work with data. Just about every thing that touches a computer now has the ability to store data. Most
#  of this data will be numbers, but sometimes it will be qualitative data (think 3 people like this, 10 people don't).
#  You can do a lot of data analysis with spreadsheets, but at some point it's almost always easier to write some code
#  to either *put* data into a spread sheet in a form that's useful, to *pull* specific data from one (or more)
#  spreadsheets, or to automate some processes (like creating six custom plots from this month's data showing price
#  trends). Being able to write a bit of code to clean up or re-purpose data is really useful, and not too difficult.
#
# Lab week 1:
#   Read in data, re-arrange it, and use it to do (text-based) statistical analysis
# Lab week 2:
#   Plot the data you worked with in lab week 1
# Homework weeks 1 & 2:
#   Use a separate file to read in information about the first file in order to do more complicated re-arrangement of data
#   Plot that data
#
# Some notes on the data you'll be working with. This is real data captured by a robotic hand designed to pick fruit.
#  the hand is instrumented with a couple sensors (IMUs in the fingers, force and torque information at the wrist and
#  information from the motors driving the three fingers. More information here:
#
# Big picture: We want to know if we can detect if the apple was picked or not from the sensor data. Each row of
#  the Data/proxy_pick_data.csv file is data from a single picking trial. Each group of n columns represents one
#  time step.

# Learning objectives, week

# Read in the data. First step, read in the data from Data/proxy_pick_data.csv and put it in a numpy array
#  - see numpy loadtxt and a_tutorial_numpy.py
#
# Read the data in and put it in the pick_data variable
pick_data = np.loadtxt("Data/proxy_pick_data.csv")

# The format of the spreadsheet data is given in Data/data_format.json. Open up the file and

print("Number of picks {}, number of data channels {}, number of time steps {}")

print("Starting {} and ending {} value of wrist force-torque chanel")


