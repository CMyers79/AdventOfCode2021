with open('input6.txt') as file:
    string = file.readlines()
    age_strings = string[0].split(",")
    ages = [int(p) for p in age_strings]
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(ages)):
        fish[ages[i]] += 1

    for i in range(256):
        fish = [fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + fish[0], fish[8], fish[0]]

    print(sum(fish))
