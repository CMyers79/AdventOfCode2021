with open('input.txt') as file:
    counter = 0
    strings = file.readlines()
    prev = 10000
    prev2 = 10000
    prev3 = 10000
    for string in strings:
        num = int(string)
        if num > prev3:
            counter += 1
        prev3 = prev2
        prev2 = prev
        prev = num

print(counter)
