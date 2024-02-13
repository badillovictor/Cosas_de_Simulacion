def formula(seed):
    return (553 * seed + 421) % 843


if __name__ == '__main__':
    results = []
    controlResults = set()
    seed = 600
    for i in range(100):
        newSeed = formula(seed)
        results.append(newSeed)
        controlResults.add(newSeed)
        if len(results) != len(controlResults):
            print('ERROR: ' + str(newSeed))
            break
        print("NO.{0} 553 x {1} + 421 mod 997 = {2}".format(i+1, seed, newSeed))
        seed = newSeed
