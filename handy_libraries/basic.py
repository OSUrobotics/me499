#!/usr/bin/env python3


# Random number generation
from random import uniform, gauss, randint
# Clock time
from time import time
# For checking random distributions
from numpy import mean, var

if __name__ == '__main__':
    # Ask what time it is
    my_start_time = time()

    # Generate a list of 1000 random numbers between 0 and 1, inclusive
    my_list = []
    for _ in range(0, 1000):  # The underscore lets you not provide a name for the variable
        my_list.append(uniform(0, 1))

    # Should be mean around 0.5 with a big variance (around 0.1)
    print("Mean {0} and variance {1}".format(mean(my_list), var(my_list)))

    # Take the same list and shift it over and scale it up
    start_value = 3.5
    end_value = 10.2
    my_list_shift_and_scale = [t * (end_value - start_value) + start_value for t in my_list]
    # mean and variance shifted
    print("Mean {0} and variance {1}".format(mean(my_list_shift_and_scale), var(my_list_shift_and_scale)))

    # Generate a list of integers
    my_random_integer = randint(10, 100)
    print("Random number between 10 and 100 is {0}".format(my_random_integer))

    # Gaussian distribution
    my_random_gauss = []
    for _ in range(0, 1000):
        # Mean and standard deviation
        my_random_gauss.append(gauss(2.0, 0.2))

    # 2.0 mean, 0.2 SD (sqrt(.2) variance)
    print("Mean {0} and variance {1}".format(mean(my_random_gauss), var(my_random_gauss)))

    # Ask what time it is
    my_end_time = time()

    print("That took {0} seconds".format(my_end_time - my_start_time))

