with open('input5.txt') as file:
    strings = file.readlines()
    coords = [string.split() for string in strings]

    x1 = [coord[0].split(",")[0] for coord in coords]
    x2 = [coord[2].split(",")[0] for coord in coords]
    y1 = [coord[0].split(",")[1] for coord in coords]
    y2 = [coord[2].split(",")[1] for coord in coords]

    hvs = []
    diags = []

    for i in range(len(strings)):
        if x1[i] == x2[i] or y1[i] == y2[i]:
            hvs.append([int(x1[i]), int(y1[i]), int(x2[i]), int(y2[i])])
        else:
            diags.append([int(x1[i]), int(y1[i]), int(x2[i]), int(y2[i])])

    points = []

    for line in hvs:
        if line[0] == line[2]:
            for i in range(line[1], line[3], (line[3] - line[1]) // abs(line[3] - line[1])):
                points.append([line[0], i])
        else:
            for i in range(line[0], line[2], (line[2] - line[0]) // abs(line[2] - line[0])):
                points.append([i, line[1]])

        points.append([line[2], line[3]])

    for line in diags:
        j = 0
        for i in range(line[1], line[3], (line[3] - line[1]) // abs(line[3] - line[1])):
            points.append([line[0] + j * (line[2] - line[0]) // abs(line[2] - line[0]), i])
            j += 1

        points.append([line[2], line[3]])

    points.sort()
    multis = [None]

    for i in range(len(points) - 1):
        if points[i] == points[i + 1] and multis[-1] != points[i]:
            multis.append(points[i])

print(len(multis) - 1)
