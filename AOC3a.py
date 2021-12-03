import math

with open('input3.txt') as file:
    strings = file.readlines()
    totals = []
    for i in range(len(strings[0]) - 1):  # do not total trailing newlines
        totals.append(sum([int(string[i]) for string in strings]))

    bits = [min(1, math.trunc(total / (len(strings) / 2)), 1) for total in totals]
    gamma = int("".join([str(bit) for bit in bits]), 2)
    epsilon = int("".join([str(bit ^ 1) for bit in bits]), 2)
    print(gamma * epsilon)
