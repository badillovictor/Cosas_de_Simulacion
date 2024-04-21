import math
import random
import matplotlib.pyplot as plt


def function():
    l = math.exp(-lmda)
    p = 1
    k = 0

    k += 1
    p *= random.random()
    while p > l:
        k += 1
        p *= random.random()

    return k - 1


if __name__ == '__main__':
    lmda = 10
    x = [function() for n in range(100)]
    fig, ax = plt.subplots()
    ax.hist(x, color='darkorchid', rwidth=0.8)
    plt.show()
