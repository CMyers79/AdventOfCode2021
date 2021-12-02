with open('input2.txt') as file:
    strings = file.readlines()
    components = []

    for string in strings:
        components.append(string.split(" "))

    x = sum([int(component[1]) for component in components if component[0] == "forward"])
    up = sum([int(component[1]) for component in components if component[0] == "up"])
    down = sum([int(component[1]) for component in components if component[0] == "down"])
    product = x * (down - up)
    print(product)
