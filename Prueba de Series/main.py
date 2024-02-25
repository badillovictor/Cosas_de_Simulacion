def getGridLocation(coordinates):
    x = 0
    y = 0
    if coordinates[0] < 0.2:
        x = 0
    elif coordinates[0] < 0.4:
        x = 1
    elif coordinates[0] < 0.6:
        x = 2
    elif coordinates[0] < 0.8:
        x = 3
    else:
        x = 4

    if coordinates[1] < 0.2:
        y = 4
    elif coordinates[1] < 0.4:
        y = 3
    elif coordinates[1] < 0.6:
        y = 2
    elif coordinates[1] < 0.8:
        y = 1
    else:
        y = 0

    return x, y

if __name__ == "__main__":
    n = 5
    certainty = 36.4
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
    pairNumber = len(source) - 1
    grid = [[0 for i in range(n)] for j in range(n)]
    for index in range(pairNumber):
        x, y = getGridLocation([source[index], source[index+1]])
        grid[y][x] += 1
    for row in grid:
        print(row)
    expectedFrequency = pairNumber / n**2
    chi = 0
    for row in grid:
        for cuadrant in row:
            chi += (expectedFrequency - cuadrant)**2 / expectedFrequency
    print("Chi =", chi)
    if chi < certainty:
        print("{0} is smaller than {1}, therefore the numbers are random".format(chi, certainty))
    else:
        print("{0} is greater than {1}, therefore the numbers are not random")