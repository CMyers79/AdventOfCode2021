from queue import PriorityQueue

with open('input15.txt') as file:
    lines = file.readlines()
    risk = []
    cumrisk = []
    for i in range(5):
        for line in lines:
            risk.append([int(char) + i + j for j in range(5) for char in line.strip()])
            for k in range(len(risk[-1])):
                if risk[-1][k] > 9:
                    risk[-1][k] = risk[-1][k] % 10 + 1

            cumrisk.append([float('inf') for num in risk[-1]])

    pathlist = PriorityQueue()
    visited = set()
    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pathlist.put((0, (0, 0)))
    cumrisk[0][0] = 0
    risk[0][0] = 0
    while not pathlist.empty():
        cur = pathlist.get()
        visited.add(cur)
        for pair in adj:
            i = cur[1][0] + pair[0]
            j = cur[1][1] + pair[1]
            if 0 <= i < len(risk[0]) and 0 <= j < len(risk) and (i, j) not in visited:
                newrisk = risk[i][j] + cumrisk[cur[1][0]][cur[1][1]]
                if newrisk < cumrisk[i][j]:
                    cumrisk[i][j] = newrisk
                    pathlist.put((newrisk, (i, j)))

    print(cumrisk[len(risk[0]) - 1][len(risk) - 1])
    print(risk)