#!/usr/bin/env python3


# Import that we think is a constant from a package we found on the Internet.
from physics import c


if __name__ == '__main__':
    # Do something innocent with the constant.  Notice how this triggers the malicious code in the class instance we
    # imported without realizing it.  Since we expect this to be a constant, this is a reasonable use case.
    m = 10
    e = m * c * c
    print(e)

