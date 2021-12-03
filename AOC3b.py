with open('input3.txt') as file:
    strings = file.readlines()


def majority_filter(strings, position):
    total = sum([int(string[position]) for string in strings])
    if total >= len(strings) / 2:
        outlist = [string for string in strings if string[position] == "1"]
    else:
        outlist = [string for string in strings if string[position] == "0"]

    if len(outlist) == 1:
        return outlist[0][:-1]
    else:
        return majority_filter(outlist, position + 1)


def minority_filter(strings, position):
    total = sum([int(string[position]) for string in strings])
    if total < len(strings) / 2:
        outlist = [string for string in strings if string[position] == "1"]
    else:
        outlist = [string for string in strings if string[position] == "0"]

    if len(outlist) == 1:
        return outlist[0][:-1]
    else:
        return minority_filter(outlist, position + 1)


O2 = int(majority_filter(strings, 0), 2)

CO2 = int(minority_filter(strings, 0), 2)

print(O2 * CO2)


    