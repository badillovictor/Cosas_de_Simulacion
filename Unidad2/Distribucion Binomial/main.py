import random

import matplotlib.pyplot as plt


def function():
    x = 0
    for i in range(n):
        if random.random() < p:
            x += 1
    print(x)
    return x


if __name__ == '__main__':
    n = 40
    p = 0.5
    x = [function() for e in range(100)]
    fig, ax = plt.subplots()
    ax.hist(x, color='darkorchid', rwidth=0.8)
    plt.show()
