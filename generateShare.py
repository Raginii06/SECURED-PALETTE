# Program Description
# This program generates the share 1 & share 2 randomly for each pixel.
import numpy as np

def generateShare(a, b):
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]
    in_ = np.array([a, b])
    out = np.zeros(in_.shape)
    randNumber = int(np.floor(1.9 * np.random.rand()))
    if randNumber == 0:
        out = in_
    elif randNumber == 1:
        a[0] = a2
        a[1] = a1
        b[0] = b2
        b[1] = b1
        out = np.array([a, b])
    return out
