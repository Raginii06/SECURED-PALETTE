import numpy as np

def visCrypt(inImg):
    s = inImg.shape
    share1 = np.zeros((s[0], 2 * s[1]))
    share2 = np.zeros((s[0], 2 * s[1]))

    # White Pixel Processing
    print('White Pixel Processing...')
    s1a = np.array([1, 0])
    s1b = np.array([1, 0])
    x, y = np.where(inImg == 1)
    len = len(x)
    for i in range(len):
        a = x[i]
        b = y[i]
        if (a < s[0]) and (b < s[1]):
            pixShare = generateShare4(s1a, s1b)
            share1[a, 2 * b - 1:2 * b] = pixShare[0, 0:2]
            share2[a, 2 * b - 1:2 * b] = pixShare[1, 0:2]
        else:
            print('Warning: Index ({}, {}) is out of bounds.'.format(a, b))

    # Black Pixel Processing
    print('Black Pixel Processing...')
    s0a = np.array([1, 0])
    s0b = np.array([0, 1])
    x, y = np.where(inImg == 0)
    len = len(x)
    for i in range(len):
        a = x[i]
        b = y[i]
        if (a < s[0]) and (b < s[1]):
            print('1.....')
            pixShare = generateShare4(s0a, s0b)
            print('2.....')
            share1[a, 2 * b - 1:2 * b] = pixShare[0, 0:2]
            print('3.....')
            share2[a, 2 * b - 1:2 * b] = pixShare[1, 0:2]
            print('4.....')
        else:
            print('Warning: Index ({}, {}) is out of bounds.'.format(a, b))

    share12 = np.bitwise_or(share1, share2)
    share12 = np.logical_not(share12)
    print('Share Generation Completed.')
    return share1, share2, share12
