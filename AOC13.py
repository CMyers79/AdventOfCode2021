with open('input13.txt') as file:
    lines = file.readlines()
    row = 0
    coords = []
    folds = []
    dots = set()
    newdots = set()
    olddots = set()

    while len(lines[row]) > 2:
        coords.append(lines[row].strip().split(","))
        row += 1
    row += 1

    while row < len(lines):
        folds.append(lines[row].strip().split()[2].split("="))
        row += 1

    for coord in coords:
        dots.add((int(coord[0]), int(coord[1])))
    for fold in folds:
        if fold[0] == "x":
            for dot in dots:
                if dot[0] > int(fold[1]):
                    newdots.add((int(fold[1]) - (dot[0] - int(fold[1])), dot[1]))
                    olddots.add(dot)
            dots |= newdots
            dots -= olddots

        else:
            for dot in dots:
                if dot[1] > int(fold[1]):
                    newdots.add((dot[0], int(fold[1]) - (dot[1] - int(fold[1]))))
                    olddots.add(dot)
            dots |= newdots
            dots -= olddots
    print(dots)

    for i in range(max([dot[1] for dot in dots]) + 1):
        for j in range(max([dot[0] for dot in dots]) + 1):
            if (j, i) in dots:
                print("*", end='')
            else:
                print(" ", end='')
        print("\n")


