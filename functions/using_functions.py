#!/usr/bin/env python3


# We can import functions from other files we wrote, just like we can import things from other Python modules.  Notice
# that, when we do this, the tests in the areas.py file are not run.
from areas import circle_area


if __name__ == '__main__':
    # Print out the areas of circles of radius from 0 to 4.
    for r in range(5):
        print('{0}: {1}'.format(r, circle_area(r)))