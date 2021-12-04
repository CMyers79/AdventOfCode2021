with open('input4.txt') as file:
    strings = file.readlines()
    squares = strings[0].split(",")
    linei = 2
    boardi = 0
    boards = []
    winners = []

    while linei + 4 < len(strings):
        for i in range(5):
            boards.append([])
            boards[boardi].append((strings[linei + i].split()))
            for string in boards[boardi][i]:
                boards[boardi][i][boards[boardi][i].index(string)] = int(string)
        boardi += 1
        linei += 6

    for square in squares:
        for board in boards:
            for line in board:
                for num in line:
                    if num == int(square):
                        line[line.index(num)] = -num

                if len([num for num in line if num < 0]) == 5:
                    if not boards.index(board) in winners:
                        winners.append(boards.index(board))
                        if len(winners) == 100:
                            print(sum([sum([num for num in row if num > 0]) for row in board]) * int(square))

            for i in range(5):
                if len([row[i] for row in board if row[i] < 0]) == 5:
                    if not boards.index(board) in winners:
                        winners.append(boards.index(board))
                        if len(winners) == 100:
                            print(sum([sum([num for num in row if num > 0]) for row in board]) * int(square))
