import statistics

with open('input7.txt') as file:
    string = file.readlines()
    position_strings = string[0].split(",")
    positions = [int(p) for p in position_strings]
    mean = int(round(statistics.mean(positions)))

    mean_fuel = sum([sum([i for i in range(1, abs(p - mean) + 1)]) for p in positions])
    plus_fuel = sum([sum([i for i in range(1, abs(p - (mean + 1)) + 1)]) for p in positions])
    minus_fuel = sum([sum([i for i in range(1, abs(p - (mean - 1)) + 1)]) for p in positions])

    while mean_fuel > plus_fuel:
        mean_fuel = plus_fuel
        mean += 1
        plus_fuel = sum([sum([i for i in range(1, abs(p - (mean + 1)) + 1)]) for p in positions])

    while mean_fuel > minus_fuel:
        mean_fuel = minus_fuel
        mean -= 1
        minus_fuel = sum([sum([i for i in range(1, abs(p - (mean - 1)) + 1)]) for p in positions])

    print(mean_fuel)
