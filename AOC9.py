with open('input9.txt') as file:
    lines = file.readlines()
    floor = []
    for i in range(len(lines)):
        floor.append([])
        for char in lines[i].strip():
            floor[i].append(int(char))

    risk = 0
    lowpoints = []
    for i in range(len(floor)):
        for j in range(len(floor[i])):
            adj = [[-1, 1], [-1, 1]]
            if i == 0:
                adj[0].remove(-1)
            elif i == len(floor) - 1:
                adj[0].remove(1)

            if j == 0:
                adj[1].remove(-1)
            elif j == len(floor[i]) - 1:
                adj[1].remove(1)

            adjsquares = [floor[i + k][j] for k in adj[0]] + [floor[i][j + l] for l in adj[1]]

            if floor[i][j] < min(adjsquares):
                risk += floor[i][j] + 1
                lowpoints.append((i, j))

    print(risk)
    basinsizes = []

    for point in lowpoints:
        basin = {point}
        i = point[0]
        j = point[1]
        adj = [[-1, 1], [-1, 1]]
        if i == 0:
            adj[0].remove(-1)
        elif i == len(floor) - 1:
            adj[0].remove(1)

        if j == 0:
            adj[1].remove(-1)
        elif j == len(floor[i]) - 1:
            adj[1].remove(1)

        adjcoords = {(i + k, j) for k in adj[0] if floor[i + k][j] != 9} | {(i, j + l) for l in adj[1] if floor[i][j + l] != 9}

        while adjcoords != set():
            basin |= adjcoords
            tempcoords = set()
            for coord in adjcoords:
                i = coord[0]
                j = coord[1]
                adj = [[-1, 1], [-1, 1]]
                if i == 0:
                    adj[0].remove(-1)
                elif i == len(floor) - 1:
                    adj[0].remove(1)

                if j == 0:
                    adj[1].remove(-1)
                elif j == len(floor[i]) - 1:
                    adj[1].remove(1)

                tempcoords |= {(i + k, j) for k in adj[0] if floor[i + k][j] != 9} | {(i, j + l) for l in adj[1] if
                                                                                    floor[i][j + l] != 9}
            adjcoords = {coord for coord in tempcoords if coord not in basin}

        basinsizes.append(len(basin))
    basinsizes.sort()
    basinsizeproduct = basinsizes.pop()
    basinsizeproduct *= basinsizes.pop()
    basinsizeproduct *= basinsizes.pop()
    print(basinsizeproduct)

