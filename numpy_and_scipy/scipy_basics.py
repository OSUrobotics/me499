#!/usr/bin/env python3

from scipy.io import wavfile
from scipy import fft
import numpy as np


def f(a=(0, 3)):
    print(a)
    a[0] = 12
    #return a[0] * a[1]

if __name__ == '__main__':

    fname = 'foo.wav'
    (sf, data) = wavfile.read('data/sinewave1000hz.wav')

    magic_fft = fft(data)
    print(magic_fft)

    a = np.array([1, 3, 5, 6])
    check = a < 5
    a[check] = 0
    print( a[check])
    a = [0, 3]
    f(a)
    f(a)


