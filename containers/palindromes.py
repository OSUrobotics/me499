#!/usr/bin/env python3


def palindrome1(x):
    """
    Determine if the argument is a palindrome, using a recursive solution.
    :param x: An iterable.
    :return: True if the argument is a palindrome, False otherwise.
    """

    # Arguments of length 0 or 1 are always palindromes.
    if len(x) < 2:
        return True

    # If the first and last elements are not the same, it's not a palindrome.
    if x[0] != x[-1]:
        return False

    # Otherwise, strip the first and last elements and recurse
    return palindrome1(x[1:-1])


def palindrome2(x):
    """
    Determine if the argument is a palindrome, using a recursive solution.
    :param x: An iterable.
    :return: True if the argument is a palindrome, False otherwise.
    """

    # We can make the recursive formulation a little more compact.
    return len(x) < 2 or (x[0] == x[-1] and palindrome1(x[1:-1]))


def palindrome3(x):
    """
    Determine if the argument is a palindrome, using an iterative solution.
    :param x: An iterable.
    :return: True if the argument is a palindrome, False otherwise.
    """

    # Count up from the start of the iterable, comparing to the corresponding elements from the end.  We only need to
    # go halfway through.  Use integer division here.
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            return False

    # If we get to here, there are no mismatches, so it's a palindrome.
    return True


def palindrome4(x):
    """
    Determine if the argument is a palindrome, using a slice-based solution.
    :param x: An iterable.
    :return: True if the argument is a palindrome, False otherwise.
    """

    # Compare the iterable to it's reversed version.
    return x == x[::-1]


if __name__ == '__main__':
    from random import randint, random

    # Make a list of guaranteed palindromes.
    palindromes = []
    for _ in range(100):
        q = [randint(1, 1000) for _ in range(randint(1, 100))]
        r = q[::-1]

        # Do we have an odd number of elements?
        if random() > 0.5:
            q += [randint(1, 1000)]
        q += r

        palindromes.append(q)

    # Make a list of guaranteed not palindromes
    not_palindromes = []
    while len(not_palindromes) < 100:
        q = [randint(1, 1000) for _ in range(randint(2, 100))]
        if q != q[::-1]:
            not_palindromes.append(q)

    functions = [palindrome1, palindrome2, palindrome3, palindrome4]
    for f in functions:
        print('testing', f.__name__)
        for p in palindromes:
            if not f(p):
                print('  failed on palindrome')
                break
        for np in not_palindromes:
            if f(np):
                print('  failed on non-palindrome')
                break
    print('testing complete')
