import math
import matplotlib.pyplot as plt


def function(x, y, a=0, b=0.5, c=1):
    if check(x, a, b, c):
        return a + (b - a) * math.sqrt(y)
    else:
        return c - (c - b) * math.sqrt(y)


def check(x, a, b, c):
    if x < ((b - a) / (c - a)):
        return True
    else:
        return False


if __name__ == '__main__':
    numbers = [0.78961, 0.76086, 0.80548, 0.58518, 0.89898, 0.28269, 0.38618, 0.79982, 0.58962, 0.69623,
               0.29931, 0.57410, 0.24000, 0.93655, 0.54325, 0.58244, 0.23949, 0.19962, 0.19147, 0.22287,
               0.05230, 0.12079, 0.82654, 0.98611, 0.57880, 0.73059, 0.76910, 0.45679, 0.33216, 0.17028,
               0.30861, 0.26593, 0.65559, 0.88809, 0.62400, 0.85853, 0.53559, 0.65002, 0.40644, 0.07281,
               0.10699, 0.27738, 0.29453, 0.34488, 0.67621, 0.70119, 0.68334, 0.21631, 0.03185, 0.05475,
               0.83358, 0.85903, 0.38507, 0.81772, 0.09133, 0.88752, 0.33381, 0.74579, 0.08128, 0.64183,
               0.55877, 0.65726, 0.20852, 0.34358, 0.05010, 0.18284, 0.55170, 0.87616, 0.61168, 0.91512,
               0.51781, 0.43308, 0.90829, 0.36982, 0.41678, 0.33729, 0.49383, 0.79113, 0.73435, 0.44267,
               0.14151, 0.79269, 0.42989, 0.11537, 0.00121, 0.49962, 0.10850, 0.55743, 0.09264, 0.76262,
               0.03272, 0.35286, 0.94187, 0.19904, 0.33954, 0.15506, 0.75103, 0.63453, 0.22724, 0.72102]

    x = []
    for i in range(0, len(numbers), 2):
        x.append(function(numbers[i], numbers[i+1]))
    fig, ax = plt.subplots()
    ax.hist(x, color='darkorchid', rwidth=0.8, bins=3)
    plt.show()
