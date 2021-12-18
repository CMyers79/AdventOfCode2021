with open('input15.txt') as file:
    lines = file.readlines()
    risk = []
    for line in lines:
        risk.append([int(char) for char in line.strip()])

    position = [0, 0]
    adj = [-1, 1]
    stack = []

    padj = [[position[0], position[1] + j] for j in adj if 0 <= position[1] + j <= 99]
    padj += [[position[0] + i, position[1]] for i in adj if 0 <= position[0] + i <= 99]
    stack.append([[coord, risk[coord[0]][coord[1]]] for coord in padj])
    djikstras