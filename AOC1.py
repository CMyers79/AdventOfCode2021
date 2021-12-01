with open('input.txt') as file:
    counter = 0
    strings = file.readlines()
    prev = 10000
    for string in strings:
        num = int(string)
        if num > prev:
            counter += 1
        prev = num

print(counter)