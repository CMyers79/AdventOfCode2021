with open('input2.txt') as file:
    strings = file.readlines()
    components = []
    x = 0
    depth = 0
    aim = 0

    for string in strings:
        components.append(string.split(" "))

    for component in components:
        if component[0] == "down":
            aim += int(component[1])
        elif component[0] == "up":
            aim -= int(component[1])
        else:
            x += int(component[1])
            depth += int(component[1]) * aim

    product = x * depth
    print(product)
