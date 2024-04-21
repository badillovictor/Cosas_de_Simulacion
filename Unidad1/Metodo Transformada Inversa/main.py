import numpy as np


def f(r):
    return np.log(r) * -1


def sort(num):
    if num < 0.1:
        interval1.append(num)
    elif num < 0.2:
        interval2.append(num)
    elif num < 0.3:
        interval3.append(num)
    elif num < 0.4:
        interval4.append(num)
    elif num < 0.5:
        interval5.append(num)
    elif num < 0.6:
        interval6.append(num)
    elif num < 0.7:
        interval7.append(num)
    elif num < 0.8:
        interval8.append(num)
    elif num < 0.9:
        interval9.append(num)
    elif num < 1.0:
        interval10.append(num)


if __name__ == '__main__':
    source = [
        0.78961,
        0.05230,
        0.10699,
        0.55877,
        0.14151,
        0.76086,
        0.12079,
        0.27738,
        0.65726,
        0.79269,
        0.80548,
        0.82654,
        0.29453,
        0.20852,
        0.42989,
        0.58518,
        0.98611,
        0.34488,
        0.34358,
        0.89898,
        0.57880,
        0.67621,
        0.11537,
        0.05010,
        0.28269,
        0.73059,
        0.70119,
        0.00121,
        0.18284,
        0.49962,
        0.38618,
        0.76910,
        0.79982,
        0.45679,
        0.68334,
        0.21631,
        0.55170,
        0.10850,
        0.87616,
        0.58962,
        0.33216,
        0.03185,
        0.55743,
        0.69623,
        0.17028,
        0.61168,
        0.09264,
        0.29931,
        0.30861,
        0.05475,
        0.91512,
        0.76262,
        0.57410,
        0.26593,
        0.83358,
        0.85903,
        0.51781,
        0.03272,
        0.24000,
        0.65559,
        0.38507,
        0.43308,
        0.35286,
        0.93655,
        0.88809,
        0.90829,
        0.94187,
        0.54325,
        0.62400,
        0.81772,
        0.09133,
        0.36982,
        0.19904,
        0.58244,
        0.85853,
        0.41678,
        0.33954,
        0.23949,
        0.53559,
        0.88752,
        0.33729,
        0.15506,
        0.19962,
        0.65002,
        0.33381,
        0.49383,
        0.75103,
        0.19147,
        0.40644,
        0.74579,
        0.79113,
        0.63458,
        0.22287,
        0.07281,
        0.08128,
        0.64183,
        0.73435,
        0.22724,
        0.44267,
        0.72102,
    ]
    xList = [f(source[i]) for i in range(len(source))]
    interval1 = []
    interval2 = []
    interval3 = []
    interval4 = []
    interval5 = []
    interval6 = []
    interval7 = []
    interval8 = []
    interval9 = []
    interval10 = []
    convenience = [
        interval1,
        interval2,
        interval3,
        interval4,
        interval5,
        interval6,
        interval7,
        interval8,
        interval9,
        interval10
    ]
    for e in xList:
        sort(e)
    li = 0.0
    ls = 0.1
    for i in convenience:
        print('Intervalo {0} a {1}:'.format(round(li, 1), round(ls, 1)), len(i))
        li += 0.1
        ls += 0.1
