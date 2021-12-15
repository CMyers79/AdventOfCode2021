with open('input11.txt') as file:
    lines = file.readlines()
    energy = []
    for line in lines:
        nums = line.strip()
        energy.append([int(char) for char in nums])
    flashes = 0
    simult = False
    steps = 0

    # for _ in range(100)
    while not simult:
        secondaries = set()
        done = True

        for i in range(len(energy)):
            vadj = [-1, 1]
            if i == 0:
                vadj.remove(-1)
            elif i == len(energy) - 1:
                vadj.remove(1)

            for j in range(len(energy[i])):
                hadj = [-1, 1]
                if j == 0:
                    hadj.remove(-1)
                elif j == len(energy[i]) - 1:
                    hadj.remove(1)

                energy[i][j] = (energy[i][j] + 1)
                if energy[i][j] == 10:
                    flashes += 1
                    adj = [(i, j + l) for l in hadj] + [(i + k, j) for k in vadj] + [(i + k, j + l) for k in vadj for l in hadj]

                    for oct in adj:
                        energy[oct[0]][oct[1]] = energy[oct[0]][oct[1]] + 1
                        if energy[oct[0]][oct[1]] == 10:
                                flashes += 1
                                secondaries.add(oct)
                                done = False

        while not done:
            done = True
            temp = set()
            for oct in secondaries:
                i = oct[0]
                j = oct[1]
                vadj = [-1, 1]
                if i == 0:
                    vadj.remove(-1)
                elif i == len(energy) - 1:
                    vadj.remove(1)

                hadj = [-1, 1]
                if j == 0:
                    hadj.remove(-1)
                elif j == len(energy[i]) - 1:
                    hadj.remove(1)

                adj = [(i, j + l) for l in hadj] + [(i + k, j) for k in vadj] + [(i + k, j + l) for k in vadj
                                                                                         for l in hadj]

                for oc2 in adj:
                    energy[oc2[0]][oc2[1]] = energy[oc2[0]][oc2[1]] + 1
                    if energy[oc2[0]][oc2[1]] == 10:
                        flashes += 1
                        temp.add(oc2)
                        done = False

            secondaries = {pair for pair in temp}

        simult = True

        for i in range(len(energy)):
            for j in range(len(energy)):
                if energy[i][j] > 9:
                    energy[i][j] = 0
                else:
                    simult = False

        steps += 1

    # print(flashes)
    print(steps)
