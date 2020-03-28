#!/usr/bin/env python3


if __name__ == '__main__':
    # This is the basic form a while statement.  This particular example is better suited to a for loop, though, since
    # you know how many times round the loop you're going to go.
    n = 0
    while n < 5:
        print(n)
        n += 1

    # This is a better example of using a while loop, since we don't know how many times round the loop we need to go.
    numbers = [1, 4, 3, 6, 7]

    i = 0
    while numbers[i] != 3:
        i += 1
    if i == len(numbers):
        print('Did not find number')
    else:
        print('Number is in position', i)
